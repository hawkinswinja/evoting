#!/usr/bin/env python3
"""routes module
   defines all the endpoint routes
"""
import json
from flask import (redirect, url_for, request, render_template,
                   session, flash)
from models import storage, auth
from views import bp

@bp.route('/test')
def test():
   return 'success', 200

@bp.route('/admin')
def admin():
    """access the admin page"""
    positions = get_posts()
    candidates = get_candidates()

    return render_template('admin.html', positions=positions,
                           candidates=candidates)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """performs authentication access"""
    if request.method == 'GET':
        return render_template('login.html')
    user = storage.show('Voter', int(request.form['user-id']))
    if not user:
        flash("user id does not exist", 'error')
    elif auth.validate(request.form['password'], user.auth_id):
        session['user_id'] = user.id
        if user.id == 1:
            return redirect(url_for('views.admin'))
        else:
            if user.status == 'Not':
                session['candidates'] = json.dumps({})
                return redirect(url_for('views.vote', myid=user.id,
                                        post=get_posts()[0]))
            return render_template('choice.html', myid=user.id,
                                   cands=json.loads(user.status),
                                   posts=get_posts(), status='voted')
    else:
        flash('incorrect password', 'errors')
    return render_template('login.html')


@bp.route('/logout')
def logout():
    """removes user id from session"""
    session.pop('user_id', None)
    return redirect(url_for('views.login'))


@bp.route('/e-portal')
def portal():
    """returns the webpage displaying the results"""
    return render_template('portal.html', candidates=get_candidates())


@bp.route('/posts')
def get_posts():
    """return a list of election posts"""
    election_posts = [post.post for post in (storage.all('Position'))]
    return election_posts


@bp.route('/vote/<int:myid>/<post>')
def vote(myid, post):
    """Voters select their canidate for the post position
          myid: voter id parameter passed after authentication
          post: the election position. used to fetch candidates
    """
    return render_template('ballot.html', myid=myid, post=post,
                           positions=get_posts(),
                           candidates=get_candidates(post))


@bp.route('/candidates')
@bp.route('/candidates/<string:position>')
def get_candidates(position=None):
    """returns dictionary of lists of candidates"""
    post_candidates = {}
    if position:
        try:
            post = storage.show('Position', position)
            for user in post.positions:
                post_candidates[user.voter_id] = {'name': user.details.name,
                                                  'post': user.post_id,
                                                  'votes': user.votes
                                                  }
        except Exception:
            flash('This position does not exist')
    else:
        cands = storage.all('Candidate')
        for user in cands:
            post_candidates[user.voter_id] = {'name': user.details.name,
                                              'post': user.post_id,
                                              'votes': user.votes
                                              }
    return post_candidates


@bp.route('/add', methods=['POST'])
def add():
    """Add newly created positions or register new candidates"""
    if request.form.get('form_id') == 'position':
        post = request.form.get('Position')
        if post in get_posts():
            flash("Position already exists")
        else:
            storage.new('Position', {'post': request.form.get('Position')})
    if request.form.get('form_id') == 'candidate':
        cand = int(request.form.get('voter_id'))
        post = request.form.get('post_id')
        candlist = get_candidates()
        if candlist.get(cand):
            flash("This voter registered for position {}"
                  .format(candlist[cand]['post']), 'error')
        elif post not in get_posts():
            flash("This post does not exist")
        else:
            storage.new('Candidate',
                        {'voter_id': cand,
                         'post_id': request.form.get('post_id')
                         })
    storage.save()
    return redirect(url_for('views.admin'))


@bp.route('/delete', methods=['POST'])
def delete():
    """delete items from database"""
    val = request.form.get('post_id')
    try:
        storage.delete('Position', val)
        storage.save()
    except Exception:
        flash("This position does not exist", 'error')
    return redirect(url_for('views.admin'))


@bp.route('/clear/<obj>')
def clear(obj):
    """Remove all instances of the specified class
       obj: Class name
    """
    if obj == 'posts':
        storage.delete('Position')
    else:
        storage.delete('Candidate')
    storage.save()
    return redirect(url_for('views.admin'))


@bp.route('/tally', methods=['POST'])
def tally():
    """adds votes to candidates and update voter status"""
    data = request.get_data(as_text=True).split(' ')
    cands = json.loads(session['candidates'])
    cands[data[0]] = data[1:]
    session['candidates'] = json.dumps(cands)
    return 'vote successfully recorded'


@bp.route('/<int:myid>/selection')
def selection(myid):
    """display voter's selected candidates"""
    cands = session.get('candidates')
    if cands:
        cands = json.loads(cands)
    else:
        cands = {}
    return render_template('choice.html', myid=myid, cands=cands,
                           posts=get_posts())


@bp.route('/vote')
def add_votes():
    """add votes to candidates"""
    for cand in json.loads(session['candidates']).values():
        storage.show('Candidate', int(cand[0])).votes += 1
    storage.show('Voter',
                 int(session['user_id'])).status = session['candidates']
    storage.save()
    # session.pop('user_id', None)
    return ('Your vote was successfully recorded')

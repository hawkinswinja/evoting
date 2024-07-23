#!/usr/bin/env python3
"""routes module
   defines all the endpoint routes
"""
import json
from flask import (redirect, url_for, request, render_template,
                   session, flash)
from app.util import validate, storage
from . import bp

@bp.route('/test')
def test():
   return 'success', 200

@bp.route('/admin')
def admin():
    """access the admin page"""
    if session['role'] != 'admin':
        return redirect(url_for('routes.login'))
    positions = get_election_posts()
    candidates = get_candidates()

    return render_template('admin.html', positions=positions,
                           candidates=candidates)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """Performs user authentication"""
    if request.method == 'GET':
        return render_template('login.html')
    
    # Get user credentials
    user_id = request.form['user-id']
    password = request.form['password']
    user = storage.show('Voter', int(user_id))
    if not user:
        flash("User ID does not exist", 'error')
    elif validate(password, user.auth_id):
        session['user_id'] = user.voter_id
        session['role'] = 'admin' if user.is_admin else 'voter'
        return handle_user_redirect(user)
    else:
        flash('Incorrect password', 'error')
    return render_template('login.html')

def handle_user_redirect(user):
    """Redirects user based on role"""
    if user.is_admin:
        return redirect(url_for('routes.admin'))
    else:
        return handle_voter_redirect(user)

def handle_voter_redirect(user):
    """Redirects voter based on their voting status"""
    if user.status == 'Not':
        session['candidates'] = json.dumps({})
        first_post = get_election_posts()[0]
        return redirect(url_for('routes.vote', myid=user.voter_id, post=first_post))
    return render_template('choice.html', myid=user.voter_id, cands=json.loads(user.status), posts=get_election_posts(), status='voted')


@bp.route('/logout')
def logout():
    """Removes user ID from session and logs out"""
    session.pop('user_id', None)
    return redirect(url_for('routes.login'))


@bp.route('/e-portal')
def portal():
    """Returns the webpage displaying the results"""
    return render_template('portal.html', candidates=get_candidates())


@bp.route('/posts')
def get_election_posts():
    """Return a list of election position"""
    return [post.post for post in (storage.all('Position'))]


@bp.route('/vote/<int:myid>/<post>')
def vote(myid, post):
    """Voters select their candidate for the post position
          myid: voter id parameter passed after authentication
          post: the election position. used to fetch candidates
    """
    return render_template('ballot.html', myid=myid, post=post,
                           positions=get_election_posts(),
                           candidates=get_candidates(post))


@bp.route('/candidates')
@bp.route('/candidates/<string:position>')
def get_candidates(position=None):
    """Returns dictionary of lists of candidates, optional filter by position"""
    candidates = {}
    if position: # filter by position
        try:
            post = storage.show('Position', position)
            for user in post.positions:
                candidates[user.voter_id] = {
                    'name': user.details.name,
                    'post': user.post_id,
                    'votes': user.votes
                }
        except Exception:
            flash('This position does not exist')
    else:
        for user in storage.all('Candidate'):
            candidates[user.voter_id] = {
                'name': user.details.name,
                'post': user.post_id,
                'votes': user.votes
            }
    return candidates


@bp.route('/add', methods=['POST'])
def add():
    """Add newly created positions or register new candidates"""
    election_positions = get_election_posts()
    form = request.form
    form_id = form.get('form_id')
    if form_id == 'position': # add position
        post = form.get('Position')
        if post in election_positions:
            flash("Position already exists")
        else:
            storage.new('Position', {'post': post})
            storage.save()
    else: # add candidate
        candidate_id = int(form.get('voter_id'))
        post = form.get('post_id')
        candidates = get_candidates()
        if candidates.get(candidate_id):
            flash("This voter is already a candidate for {}".format(candidates[candidate_id]['post']), 'error')
        elif post not in election_positions:
            flash("This post does not exist")
        else:
            storage.new('Candidate',
                        {'voter_id': candidate_id,
                         'post_id': post
                         })
            storage.save()
    return redirect(url_for('routes.admin'))


@bp.route('/delete', methods=['POST'])
def delete_position():
    """Delete election position"""
    post_id = request.form.get('post_id')
    try:
        storage.delete('Position', post_id)
        storage.save()
    except Exception:
        flash("This position does not exist", 'error')
    return redirect(url_for('routes.admin'))


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
    return redirect(url_for('routes.admin'))


@bp.route('/tally', methods=['POST'])
def tally():
    """Record voter selection for election positions and save in session data"""
    data = request.get_data(as_text=True).split(' ')
    candidates = json.loads(session['candidates'])
    candidates[data[0]] = data[1:]
    session['candidates'] = json.dumps(candidates)
    return 'Vote successfully recorded'


@bp.route('/selection/<int:myid>')
def selection(myid):
    """Display voter's selected candidates"""
    voter_selection = session.get('candidates')
    if voter_selection:
        voter_selection = json.loads(voter_selection)
    else:
        voter_selection = {}
    return render_template('choice.html', myid=myid, cands=voter_selection,posts=get_election_posts())


@bp.route('/vote')
def add_votes():
    """add votes to candidates"""
    for candidate in json.loads(session['candidates']).values():
        storage.show('Candidate', int(candidate[0])).votes += 1
    storage.show('Voter',
                 int(session['user_id'])).status = session['candidates']
    storage.save()
    return ('Your vote was successfully recorded')

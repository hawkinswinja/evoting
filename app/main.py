#!/usr/bin/python3
"""entry point to handle requests and update databse"""
from models import storage
from flask_cors import CORS
from flask import Flask, redirect, url_for, request, jsonify, render_template, abort

app = Flask(__name__)
cors = CORS(app, resources={"r/*": {"origins": "0.0.0.0"}})
app.url_map.strict_slashes = False


@app.route('/admin')
def admin():
    """access the admin page"""
    positions = get_posts()
    candidates = get_candidates()
    return render_template('admin.html', positions=positions, candidates=candidates)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """performs authentication access"""
    if request.method == 'GET':
        return render_template('login.html')
    try:
       user = storage.show('Voter', int(request.form['user-id']))
    except Exception:
       return abort(404, 'user id does not exist')
    if request.form['password'] == user.auth_id:
       if user.name == 'ADMIN':
            return redirect(url_for('admin'))
       else:
            return redirect(url_for('vote', myid=user.id, post=get_posts()[0]))
    else:
        return abort(404, 'incorrect password')

@app.route('/e-portal')
def portal():
    """returns the webpage displaying the results"""
    return render_template('portal.html', candidates=get_candidates())

@app.route('/posts')
def get_posts():
    """return a list of election posts"""
    election_posts = [post.post for post in (storage.all('Position'))]
    return election_posts

@app.route('/vote/<int:myid>/<post>')
def vote(myid, post):
    """access the ballot page"""
    positions = get_posts()
    cands = get_candidates(post)
    return render_template('ballot.html', myid=myid, post=post, positions=positions, candidates=cands)

@app.route('/candidates')
@app.route('/candidates/<string:position>')
def get_candidates(position=None):
    """return dictionary of lists of candidates"""
    post_candidates = {}
    if position:
        try:
            post = storage.show('Position', position)
            for user in post.positions:
                post_candidates[user.voter_id] = {'name':user.details.name, 'post':user.post_id, 'votes': user.votes}
        except:
            return abort(404, 'This position does not exist')
    else:
        cands = storage.all('Candidate')
        for user in cands:
            post_candidates[user.voter_id] = {'name':user.details.name, 'post':user.post_id, 'votes': user.votes}
    return post_candidates

@app.route('/add', methods=['POST'])
def add():
    """handle form events"""
    if request.form.get('form_id') == 'position':
        post = request.form.get('Position')
        if post in get_posts():
            return jsonify("Position cannot be null or similar.\nEnsure the position does not already exist")
        else:
            storage.new('Position', {'post': request.form.get('Position')})
    if request.form.get('form_id') == 'candidate':
        cand = request.form.get('voter_id')
        candlist =  get_candidates().keys()
        if cand in candlist:
            return jsonify("This Candidate already registered for a different position")
        else:
            storage.new('Candidate', {'voter_id': cand, 'post_id': request.form.get('post_id')})
    storage.save()
    return redirect('/admin')

@app.route('/delete', methods=['POST'])
def delete():
    """delete items from database"""
    val = request.form.get('post_id')
    try:
        storage.delete('Position', val)
    except Exception:
        return jsonify("This position does not exist")
    storage.save()
    return redirect('/admin')

@app.route('/clear/<obj>')
def clear(obj):
    if obj == 'posts':
        storage.delete('Position')
    else:
        storage.delete('Candidate')
    storage.save()
    return redirect('/admin')

@app.route('/tally', methods=['POST'])
def tally():
    """add votes to candidates"""
    
    return update_votes(int(request.form.get('cand_id')),
                         request.form.get('voter_id'),
                         request.form.get('post'))
    
def update_votes(cand_id, voter_id, post):
    """updates candidate votes"""
    voter = storage.show('Voter', voter_id)
    if voter.status and post in voter.status:
        return ("You already voted for this position")
    voter.status += post
    return add_votes(cand_id)

def add_votes(cand):
    """add votes to candidates"""
    try:
        storage.show('Candidate', cand).votes += 1
        storage.save()
    except Exception:
        return  ("Please refresh the page to vote again")
    return 'Your vote was successfully recorded'

if __name__ == "__main__":
    """run application"""
    app.run(host='0.0.0.0', port=5000, debug=False)

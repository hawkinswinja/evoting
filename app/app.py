#!/usr/bin/python3
"""entry point to handle requests and update databse"""
from models import storage
from flask import Flask, redirect, url_for, request, jsonify, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/admin')
def admin():
    """access the admin page"""
    return render_template('admin.html', positions=get_posts(), candidates=get_candidates())

@app.route('/login', methods=['GET', 'POST'])
def login():
    """performs authentication access"""
    if request.method == 'GET':
        return render_template('login.html')
    user = storage.show('Voter', int(request.form['user-id']))
    if user:
        if request.form['password'] == user.auth_id:
            if user.name == 'ADMIN':
                return redirect(url_for('admin'))
            if user.status == 'Not voted':
                return redirect(url_for('vote', myid=user.id, post=get_posts()[0]))
            else:
                return jsonify({'message': 'This user has already voted'})
        return jsonify({'error': 'user id does not exist'})


@app.route('/posts')
def get_posts():
    """return a list of election posts"""
    election_posts = [post.post for post in (storage.all('Position'))]
    return election_posts

@app.route('/vote/<int:myid>/<post>')
def vote(myid, post):
    """access the ballot page"""
    return render_template('ballot.html', myid=myid, post=post, positions=get_posts(), candidates=get_candidates(post))

@app.route('/candidates')
@app.route('/candidates/<string:position>')
def get_candidates(position=None):
    """return dictionary of lists of candidates"""
    post_candidates = {}
    if position:
        post = storage.show('Position', position)
        for user in post.positions:
            post_candidates[user.voter_id] = {'name':user.details.name, 'post':user.post_id, 'votes': user.votes}
    else:
        cands = storage.all('Candidate')
        for user in cands:
            post_candidates[user.voter_id] = {'name':user.details.name, 'post':user.post_id, 'votes': user.votes}
    return post_candidates

@app.route('/add', methods=['POST'])
def add():
    """handle form events"""
    if request.form.get('form_id') == 'position':
        try:
            storage.new('Position', {'post': request.form.get('Position')})
        except Exception:
            return jsonify("failed. Position cannot be null")
    if request.form.get('form_id') == 'candidate':
        try:
            storage.new('Candidate', {'voter_id': request.form.get('voter_id'),
                                      'post_id': request.form.get('post_id')})
        except Exception as e:
            return jsonify(e)
    storage.save()
    return redirect('/admin')

@app.route('/delete', methods=['POST'])
def delete():
    """delete items from database"""
    val = request.form.get('post_id')
    try:
        storage.delete('Position', val)
    except Exception as e:
        return jsonify(str(e))
    storage.save()
    return

@app.route('/clear/<obj>')
def clear(obj):
    if obj == 'posts':
        storage.delete('Position')
    else:
        storage.delete('Candidate')
    storage.save()
    return redirect('/admin'), 200

@app.route('/tally', methods=['POST'])
async def tally():
    """add votes to candidates"""
    cand_id = int(request.form.get('cand_id'))
    await(update_votes(cand_id))
    return 'Success'
    
async def update_votes(id):
    """updates candidate votes"""
    user = storage.show('Candidate', id)
    user.votes += 1
    storage.save()

if __name__ == "__main__":
    """run application"""
    app.run(host='0.0.0.0', port=5000, debug=True)

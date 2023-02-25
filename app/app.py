#!/usr/bin/python3
"""entry point to handle requests and update databse"""
from models import storage
from flask import Flask, redirect, url_for, request, jsonify, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/admin')
def admin():
    """access the admin page"""
    positions = get_posts()
    return render_template('admin.html', positions=positions, candidates=storage.all('Candidate'))

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    """performs authentication access"""
    if request.method == 'GET':
        return render_template('login.html')
    user = storage.show('Voter', int(request.form['user-id']))
    if user:
        if request.form['password'] == user.auth_id:
            if user.name == 'admin':
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

@app.route('/<position>/candidates')
def get_candidates(position):
    """return dictionary of lists of candidates"""
    post = storage.show('Position', position)
    post_candidates = []
    for user in post.positions:
        post_candidates.append(user.details.name)
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
    return redirect('/admin')






if __name__ == "__main__":
    """run application"""
    app.run(host='0.0.0.0', port=5000, debug=True)

#!/usr/bin/python3
"""entry point to handle requests and update databse"""
from models import storage
from flask import Flask, redirect, url_for, request, jsonify, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False
posts = storage.all('Position')
candidates = storage.all('Candidate')

@app.route('/admin')
def admin():
    """access the admin page"""
    return render_template('admin.html', positions=posts,candidates= candidates)

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    """performs authentication access"""
    if request.method == 'GET':
        return render_template('login.html')
    user = storage.show('Voter', int(request.form['user-id']))
    if user:
        if request.form['password'] == user.auth_id:
            if user.status == 'Not voted':
                return redirect(url_for('vote', myid=user.id, status=user.status))
            else:
                return jsonify({'message': 'This user has already voted'})
        return jsonify({'error': 'user id does not exist'})

@app.route('/vote/<int:myid>/<status>')
def vote(myid, status):
    """access the ballot page"""
    return render_template('ballot.html', myid=myid, positions=posts, status=status)

if __name__ == "__main__":
    """run application"""
    app.run(host='0.0.0.0', port=5000, debug=True)

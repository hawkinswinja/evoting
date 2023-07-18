#!/usr/bin/python3
"""entry point to handle requests and update databse"""
from flask_cors import CORS
from flask import Flask, request, session, redirect, url_for
from config import Config

app = Flask(__name__)
cors = CORS(app, resources={"r/*": {"origins": "0.0.0.0"}})
app.url_map.strict_slashes = False
app.config.from_object(Config)


@app.before_request
def require_login():
    """performed before any request is made to the server"""
    if 'login' not in request.path and 'user_id' not in session:
        return redirect(url_for('views.login'))


if __name__ == "__main__":
    """run application"""
    from views import bp
    app.register_blueprint(bp)
    app.run(host='0.0.0.0', port=5000, debug=True)

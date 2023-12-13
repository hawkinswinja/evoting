#!/usr/bin/python3
"""entry point to handle requests and update databse"""
from flask_cors import CORS
from flask import Flask, request, session, redirect, url_for
from config import Config
from views import bp


app = Flask(__name__)
cors = CORS(app, resources={"r/*": {"origins": "0.0.0.0"}})
app.url_map.strict_slashes = False
app.config.from_object(Config)
app.register_blueprint(bp)


@app.before_request
def require_login():
    """Ensure only authenticated users access the site"""
    path = request.path
    excluded_endpoints = ['login', 'test']

    if not any(endpoint in path for endpoint in excluded_endpoints) or not session.get('user_id'):
        return redirect(url_for('views.login'))

@app.after_request
def after_request(response):
    """Remove cache for e-portal to prevent voting twice"""
    response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
    # if 'e-portal' in request.path:
    #     session.pop('user_id', None)
    return response

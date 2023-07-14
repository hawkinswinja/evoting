#!/usr/bin/python3
"""entry point to handle requests and update databse"""
from flask_cors import CORS
from flask import Flask
from os import getenv

app = Flask(__name__)
cors = CORS(app, resources={"r/*": {"origins": "0.0.0.0"}})
app.url_map.strict_slashes = False
app.secret_key = getenv('SK')

if __name__ == "__main__":
    """run application"""
    from views import bp
    app.register_blueprint(bp)
    app.run(host='0.0.0.0', port=5000, debug=True)

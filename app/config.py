# config.py

import os


class Config:
    DEBUG = True
    SECRET_KEY = os.getenv('SK')

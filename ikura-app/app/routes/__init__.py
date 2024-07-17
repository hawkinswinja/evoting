from flask import Blueprint

bp = Blueprint('routes', __name__, template_folder='templates')

from . import routes

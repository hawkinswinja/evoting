from flask import Blueprint

bp = Blueprint('views', __name__, template_folder='templates')

from . import routes

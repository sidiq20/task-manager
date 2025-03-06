from flask import Blueprint

pages_bp = Blueprint('pages', __name__, template_folder='templates')

from . routes import routes, forms
from flask import Blueprint

from .views import create_views

blueprint = Blueprint('home', __name__, template_folder='templates')
create_views(blueprint)
from flask import Blueprint
from .views import create_views

blueprint = Blueprint('api', __name__)
create_views(blueprint)

from flask import Blueprint

blueprint = Blueprint("home",__name__)

from . import views
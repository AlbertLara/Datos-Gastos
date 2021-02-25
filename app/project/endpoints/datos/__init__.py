from flask import Blueprint

blueprint = Blueprint("datos",__name__,url_prefix="/datos")

from . import views
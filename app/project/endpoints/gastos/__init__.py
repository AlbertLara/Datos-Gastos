from flask import Blueprint

blueprint = Blueprint("gastos",__name__,url_prefix="/gastos")

from . import views
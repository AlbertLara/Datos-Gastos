from flask import Blueprint

blueprint = Blueprint("cuentas",__name__,url_prefix="/cuentas")

from . import views
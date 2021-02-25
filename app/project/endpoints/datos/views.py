from . import blueprint
from ...models import *
from flask_login import login_required, login_user, logout_user, current_user
from flask import redirect, render_template, url_for, request
import os

@blueprint.route("/",methods=["GET","POST"])
@login_required
def index():
  template = render_template('datos/index.html',title='Datos')
  return template
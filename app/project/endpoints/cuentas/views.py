from . import blueprint
from ...models import *
from .forms import *
from flask_login import login_required, login_user, logout_user, current_user
from flask import redirect, render_template, url_for, request
import os

@blueprint.route("/",methods=["GET","POST"])
@login_required
def index():
  data = Cuentas.query.all()
  template = render_template('cuentas/index.html',title='Cuentas', data=data)
  return template
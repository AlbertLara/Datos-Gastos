from . import blueprint
from .forms import LoginForm
from flask import redirect, render_template, url_for, request
import os

@blueprint.route('/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    return redirect(url_for("auth.login"))
  template = render_template('auth/login.html', form=form,title='Login')
  return template
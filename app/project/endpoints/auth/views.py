from . import blueprint
from .forms import LoginForm
from ...models import User
from flask_login import login_required, login_user, logout_user, current_user
from flask import redirect, render_template, url_for, request
import os

@blueprint.route('/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user is not None and user.verify_password(form.password.data):
      login_user(user)
      return redirect(url_for("home.index"))
  template = render_template('auth/login.html', form=form,title='Login')
  return template
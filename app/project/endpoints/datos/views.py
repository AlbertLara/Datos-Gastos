from . import blueprint
from ...models import *
from .forms import *
from flask_login import login_required, login_user, logout_user, current_user
from flask import redirect, render_template, url_for, request

@blueprint.route("/", methods=["GET", "POST"])
@login_required
def index():
    data = Datos.query.all()
    form = CreateRecord()
    if form.validate_on_submit():
      return redirect(url_for("datos.create"))
    template = render_template('datos/index.html', title='Datos', data=data, form=form)
    return template


@blueprint.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = NewRecord()
    if form.validate_on_submit():
        print(1)
        return redirect(url_for("datos.index"))
    template = render_template("datos/create.html",title="Crear", form=form)
    return template
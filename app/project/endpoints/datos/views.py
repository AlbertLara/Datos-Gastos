from . import blueprint
from ...models import *
from .forms import *
from flask_login import login_required, login_user, logout_user, current_user
from flask import redirect, render_template, url_for, request

@blueprint.route("/", methods=["GET", "POST"])
@login_required
def index():
    data = Datos.query.order_by(Datos.id.desc()).all()
    form = CreateRecord()
    if form.validate_on_submit():
      return redirect(url_for("datos.create"))
    template = render_template('datos/index.html', title='Datos', data=data, form=form)
    return template


@blueprint.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = NewRecord()
    ids = get_cuentas_ids()
    choices =[(id, id) for id in ids]
    form.idtransaction.choices = choices
    if form.validate_on_submit():
        concepto = form.concepto.data
        day = form.dia.data
        dinero = form.dinero.data
        idtransaction = form.idtransaction.data.split("-")
        id_ingreso = idtransaction[1]
        id_gasto = idtransaction[0]
        print(idtransaction)
        print(day)
        print(concepto)
        return redirect(url_for("datos.index"))
    template = render_template("datos/create.html",title="Crear", form=form)
    return template
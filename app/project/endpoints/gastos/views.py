from . import blueprint
from ...models import *
from flask_login import login_required
from flask import render_template

@blueprint.route("/", methods=["GET", "POST"])
@login_required
def index():
    gastos = Gastos.query.all()
    datos = {}
    for gasto in gastos:
        month = gasto.month

    data = []
    template = render_template('gastos/index.html', title='Gastos', data=data)
    return template
from . import blueprint
from ...models import *
from flask_login import login_required
from flask import render_template


@blueprint.route("/", methods=["GET", "POST"])
@login_required
def index():
    data = Gastos.query.all()
    for gasto in data:
        print(gasto.month)
    template = render_template('gastos/index.html', title='Gastos', data=data)
    return template

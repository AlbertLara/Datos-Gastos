from . import blueprint
from ...models import *
from flask_login import login_required
from flask import render_template


@blueprint.route("/", methods=["GET", "POST"])
@login_required
def index():
    data = Cuentas.query.filter(Cuentas.id > 0).all()
    template = render_template('cuentas/index.html', title='Cuentas', data=data)
    return template

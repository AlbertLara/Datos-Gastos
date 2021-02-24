from . import blueprint
from flask import redirect, render_template, url_for, request
from flask_login import login_required
import os

@blueprint.route('/')
@login_required
def index():
    return render_template('home/index.html',
                           path='home',title='Welcome')
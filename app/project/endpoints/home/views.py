from . import blueprint
from flask import redirect, render_template, url_for, request

@blueprint.route('/')
def index():
    print("Hello 1")
    return render_template('home/index.html',
                           path='home',title='Welcome')
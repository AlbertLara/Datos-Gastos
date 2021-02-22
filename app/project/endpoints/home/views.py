from . import blueprint
from flask import redirect, render_template, url_for, request
import os
import heroku3

@blueprint.route('/')
def index():
    heroku_conn = heroku3.from_key(os.getenv("API_KEY"))
    print(heroku_conn.account())
    return render_template('home/index.html',
                           path='home',title='Welcome')
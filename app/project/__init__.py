from flask import Flask
from .models import db
import os

def create_app():
    app = Flask(__name__,template_folder='web/templates',
                static_folder='web/static')
    app.config.from_pyfile("config.py")
    db.init_app(app)
    with app.app_context():
      db.create_all()
    register_blueprint(app)
    return app


def register_blueprint(app:Flask):
    from project.endpoints.home import blueprint as home_blueprint
    app.register_blueprint(home_blueprint)
from flask import Flask
from .models import db
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
import os

def create_app():
    app = Flask(__name__,template_folder='web/templates',
                static_folder='web/static')
    app.config.from_pyfile("config.py")
    Bootstrap(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    db.init_app(app)
    
    login_manager.login_view = "auth.login"
    with app.app_context():
      db.create_all()
    
    
    
    register_blueprint(app)
    return app


def register_blueprint(app:Flask):
    from project.endpoints.home import blueprint as home_blueprint
    from project.endpoints.auth import blueprint as auth_blueprint
    app.register_blueprint(home_blueprint)
    app.register_blueprint(auth_blueprint)
from flask import Flask
from .models import db, User
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
      create_user()
    @login_manager.user_loader
    def load_user(user_id):
      return User.query.get(int(user_id))
    
    register_blueprint(app)
    return app


def register_blueprint(app:Flask):
  from project.endpoints.home import blueprint as home_blueprint
  from project.endpoints.auth import blueprint as auth_blueprint
  app.register_blueprint(home_blueprint)
  app.register_blueprint(auth_blueprint)
    
def create_user():
  email = os.getenv("USER_MAIL",None)
  password = os.getenv("USER_PWD",None)
  if email is not None and password is not None:
    exists = User.query.filter_by(email=email).count()
    print(exists)
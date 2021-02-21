from flask import Flask

def create_app():
    app = Flask(__name__,template_folder='web/templates',
                static_folder='web/static')
    register_blueprint(app)
    return app


def register_blueprint(app:Flask):
    from app.project.endpoints.home import blueprint as home_blueprint
    app.register_blueprint(home_blueprint)
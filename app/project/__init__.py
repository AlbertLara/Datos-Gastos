from flask import Flask

def create_app():
    app = Flask(__name__,template_folder='web/templates',
                static_folder='web/static')
    app.config.from_pyfile("config.py")
    
    register_blueprint(app)
    print(app.config)
    return app


def register_blueprint(app:Flask):
    from project.endpoints.home import blueprint as home_blueprint
    app.register_blueprint(home_blueprint)
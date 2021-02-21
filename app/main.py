from flask import Flask, Blueprint, render_template
import os
app = Flask(__name__,template_folder='web/templates',
            static_folder='web/static')
home_blueprint = Blueprint("home",__name__, url_prefix='/')

@home_blueprint.route('/')
def index():
    print("Hello")
    return render_template('home/index.html',
                           path='home',title='Welcome')
app.register_blueprint(home_blueprint)

if __name__=='__main__':
    port = int(os.getenv('PORT',5000))
    app.run(host="0.0.0.0", debug=True, port=port)
from flask import Flask
from .endpoints.home import blueprint as home_blueprint
import os
app = Flask(__name__,template_folder='web/templates',
            static_folder='web/static')

app.register_blueprint(home_blueprint)

if __name__=='__main__':
    port = int(os.getenv('PORT',5000))
    app.run(host="0.0.0.0", debug=True, port=port)
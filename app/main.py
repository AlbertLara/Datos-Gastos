from flask import Flask, render_template
import os
app = Flask(__name__,template_folder='web/templates',
            static_folder='web/static')

@app.route('/')
def index():
    print("Hello")
    return render_template('home/index.html',
                           path='home',title='Welcome')

if __name__=='__main__':
    port = int(os.getenv('PORT',5000))
    app.run(host="0.0.0.0", debug=True, port=5000)
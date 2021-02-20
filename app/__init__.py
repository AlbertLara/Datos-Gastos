from flask import Flask

app = Flask(__name__,template_folder='web/templates',
            static_folder='web/static')

if __name__=='__main__':
    app.run(host="localhost",port=8080,
            debug=True)
from functools import wraps
from flask import Flask, flash, session,redirect,url_for
from admin.routes import admin
from flask_bootstrap import Bootstrap
from flask_session import Session

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = '123456789'
app.config.setdefault('BOOTSTRAP_USE_MINIFIED', True)
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'

Bootstrap(app)
Session(app)

app.register_blueprint(admin)


    
if __name__ == '__main__':
    app.run(debug=True)

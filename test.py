from functools import wraps
from flask import Flask, flash, render_template, redirect, session, request,url_for
from flask_session import Session

app = Flask(__name__, template_folder='templates_testing')
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SWEETIFY_SWEETALERT_LIBRARY'] = 'sweetalert2'
Session(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['session_name'] = request.form.get('name')
        return redirect('/')
    flash('You were successfully logged in')
    return render_template('login.html')

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'session_name' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('login'))

    return wrap


@app.route('/logout')
@login_required
def logout():
    session['session_name'] = None
    flash('you have been logged out !')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

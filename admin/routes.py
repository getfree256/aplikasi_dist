from functools import wraps
from flask import Request, flash, redirect, render_template, url_for, Blueprint, request, session
from forms import LoginForm
from database import connection

admin = Blueprint("admin", __name__)


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if not session.get('session_usr') == None:
            return f(*args, **kwargs)
        else:
            flash("Silahkan Anda login terlebih dahulu ...")
            return redirect(url_for('admin.login'))

    return wrap


@admin.route('/')
def index():
    return redirect(url_for('admin.login'))


@admin.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@admin.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usr = request.form.get('usr')
        try:
            with connection.cursor() as cursor:
                val = (usr)
                sql = "SELECT * FROM users WHERE ffcuser=%s"
                cursor.execute(sql, val)
                result = cursor.fetchone()
                if result == None:
                    flash('Username dan Password tidak ditemukan !')
                    return redirect('/')
                else:
                    session['session_login'] = True
                    session['session_usr'] = usr
                    return redirect(url_for('admin.dashboard'))
        finally:
            cursor.close
            connection.close
    return render_template('login.html', form=form)


@admin.route('/logout')
def logout():
    session.pop('session_usr')
    session.pop('session_login')
    return redirect('/')


@admin.route('/users')
def users():
    try:
        with connection.cursor() as cursor:
            sql = 'select * from users'
            cursor.execute(sql)
            data = cursor.fetchall()
            return render_template('users.html',data=data)
    finally:
        cursor.close
        connection.close

@admin.route('/users_add',methods=['GET','POST'])        
def users_add():
    if request.method == 'POST':
        usr = request.form['usr']
        psw = request.form['psw']
        if usr and psw :
            try:
                with connection.cursor() as cursor:
                    sql = 'insert users (ffcuser,ffcpsw) values (%s,%s)'
                    cursor.execute(sql,(usr,psw))
                    connection.commit()
                    return redirect(url_for('admin.users'))
            finally:
                cursor.close
                connection.close                

@admin.route('/users_edit',methods=['POST'])
def users_edit():
    return render_template('contoh.html')

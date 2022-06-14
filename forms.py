from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,SelectField
from wtforms.validators import ValidationError,DataRequired,Email

class LoginForm(FlaskForm):
    usr = StringField('Username',validators=[DataRequired(message='Username harus di-isi')],render_kw={'autofocus':True})
    psw = StringField('Password',validators=[DataRequired(message='Password harus di-isi')])
    submit = SubmitField('Login')
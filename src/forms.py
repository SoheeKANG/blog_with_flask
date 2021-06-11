from wtforms import Form, StringField, PasswordField
from wtforms.fields.html5 import EmailField


class LoginForm(Form):
    username = StringField('Username')
    email = EmailField()
    password = PasswordField('Password')
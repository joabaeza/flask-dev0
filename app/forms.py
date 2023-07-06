from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuarios', validators=[DataRequired()])
    password = PasswordField('CLave', validators=[DataRequired()])
    submit = SubmitField('enviar')
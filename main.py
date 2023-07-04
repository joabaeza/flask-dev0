from flask import Flask ,request,make_response, redirect, render_template,session,url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import unittest
"""
20 08:57
"""



app = Flask(__name__)
app.config.update(
    DEBUG=True,
    ENV='development'
)
app.config['SECRET_KEY'] = 'SUPOER_SECRETO'

botstrap = Bootstrap(app)


class LoginForm(FlaskForm):
    username = StringField('Nombre de usuarios', validators=[DataRequired()])
    password = PasswordField('CLave', validators=[DataRequired()])
    submit = SubmitField('enviar')

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)




@app.errorhandler(404)
def not_found(error):
    return render_template('404.html',error=error)

@app.errorhandler(500)
def not_found(error):
    return render_template('404.html',error=error)


todos = ['Comprar algo','Comprar algo 2','Comprar algo 4']




@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    """response.set_cookie('user_ip',user_ip)"""
    return response


@app.route('/hello',methods=['get','post'])
def hello():
    """user_ip = request.cookies.get('user_ip')"""
    user_ip = session.get('user_ip')
    login_form  = LoginForm()
    username = session.get('username')
    context = {
        'user_ip' : user_ip,
        'todos':todos,
        'login_form':login_form,
        'username':username,
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        flash('nombre de usuario registrado')
        redirect(url_for('index'))
    return render_template('hello.html', **context )
    '''hello from platzi , tu ip es {}'.format(user_ip)'''



if __name__ == '__main__':
    app.run()

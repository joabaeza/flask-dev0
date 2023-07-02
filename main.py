from flask import Flask, request,make_response, redirect, render_template,session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField
from wtforms.validators import DataRequired
"""
17 4:28
"""



app = Flask(__name__)
app.config.update(
    DEBUG=True,
    ENV='development'
)
app.config['SECRET_KEY'] = 'SUPOER_SECRETO'

botstrap = Bootstrap(app)


class LoginForm(FlaskForm):
    username = StringField('Nombre de usuarios')
    password = PasswordField('CLave')



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

@app.route('/hello')
def hello():
    """user_ip = request.cookies.get('user_ip')"""
    user_ip = session.get('user_ip')
    context = {
        'user_ip' : user_ip,
        'todos':todos
    }
    return render_template('hello.html', **context )
    '''hello from platzi , tu ip es {}'.format(user_ip)'''



if __name__ == '__main__':
    app.run()

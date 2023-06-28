from flask import Flask,render_template, Blueprint, url_for,redirect, request, session
from flask_session import Session
from blueprints.database.mongodb import getHistory
from blueprints.authentication.auth import authentication
from blueprints.gptconnect.gptapi import gptapi
from os import getenv

app = Flask(__name__)
app.register_blueprint(authentication)
app.register_blueprint(gptapi)

app.config['SECRET_KEY'] = getenv('SESSION_SECRETKEY')
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def homepage():
    if 'email' in session:

        historyGet = getHistory(session['email'])

        return render_template('home.html', notConnected=None, historyGet=historyGet)
    else:
        return render_template('home.html', notConnected=True)


@app.route('/auth/login')
def loginPage():

    return render_template('login.html')

@app.route('/auth/register')
def registerPage():

    return render_template('register.html')

@app.route('/auth/create/new/session/', methods=['POST'])
def createSession():

    session['session_hash'] = request.form.get('session_hash')
    session['username'] = request.form.get('username')
    session['email'] = request.form.get('email')

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

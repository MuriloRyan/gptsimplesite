from flask import Flask, Blueprint, redirect, Request, request, url_for
from blueprints.database.userconfig import User
import blueprints.database.mongodb as db
import requests

authentication = Blueprint('authentication',__name__,template_folder='templates')

@authentication.route('/login/mongodb/new/', methods=['POST'])
def loginAuth():
    
    data = {
    'username': db.findIn('username',{'email': request.form.get('email')}),
    'email': request.form.get('email'),
    'password': request.form.get('password')
    }

    tryData = db.logIn(data)

    data['session_hash'] = tryData

    return redirect('/auth/create/new/session', code=307)

@authentication.route('/register/mongodb/new', methods=['POST'])
def registerAuth():
    data = {
        'username': request.form.get('username'),
        'email': request.form.get('email'),
        'password': request.form.get('password')
    }

    tryData = db.signIn(data)

    return redirect('/login/mongodb/new', code=307)
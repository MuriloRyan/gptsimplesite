from flask import Flask, Blueprint, redirect
import blueprints.database.mongodb as db

database = Blueprint('database',__name__,template_folder='templates')

#site/database/mongodb/history/add/?query={query}&response={response}&email={email}
@database.route('/mongodb/history/add/')
def addHistory():

    email = request.args.get('email')
    data = {
        'query': request.args.get('query'),
        'response': request.args.get('response'),
        }

    userTest = db.find_one({'email': email})

    if userTest:
        db.writehistory(data, userTest['email'])

        return 200
    else:
        return None
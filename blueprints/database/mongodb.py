from hashlib import sha3_512
from blueprints.database.attempts import addAttemp
from blueprints.database.userconfig import User
import pymongo
import os

# URL TO CONNECT
url = os.getenv('MONGODB_URL')

# Connect to the database
Cluster = pymongo.MongoClient(url)
database = Cluster.get_database('simplegptdb')
db = database.get_collection('users')

def signIn(data):

    userTest = db.find_one({
        'username': data['username'],
        'email': data['email'],
        'password': data['password']
        })
    
    if userTest:
        return None #incorrect request
    else:
        userToRegister = User(data['username'],data['email'],data['password'])

        db.insert_one(userToRegister.get_data())
        return 200 #ok request

def logIn(data):
    userAtempt = db.find_one({'email': data['email'], 'password': data['password']})

    if userAtempt:
        return addAttemp(data)
    
    return None


def findIn(data,user):
    userTest = db.find_one({'email': user})

    if userTest:
        testReturn = {}
        for key in data:
            testReturn[key] = userTest.get(key)
        return testReturn
    else:
        return None

def writehistory(data):

    userTest = db.find_one({'email': data['email']})

    if userTest:
        db.update_one({'_id': userTest['_id']}, {'$push': {'history': data}})
        return 200
    else:
        return None

def getHistory(user):

    userTest = db.find_one({'email': user})

    if userTest:
        history = userTest['history']

        return history
from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__)

# connect to MongoDB with the defaults

app.config['MONGO_URI'] = 'mongodb://test:TestBuggl@ds041633.mongolab.com:41633/buggl'
mongo1 = PyMongo(app,config_prefix="MONGO")

@app.route('/')
def plan():
    user = mongo1.db.entries.find_one_or_404({'plan': "plan1"})
    return user

# user = mongo1.db.users.find_one_or_404({'plan': "plan1"})
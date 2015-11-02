import os
from flask import render_template
from flask import url_for
from flask import Flask
from flask import request
from flask.ext.mandrill import Mandrill
from pymongo import MongoClient
# from flask.ext.pymongo import PyMongo
# app = Flask(__name__)

app = Flask(__name__, static_url_path='')





@app.route('/', methods=['GET', 'POST'])
def index():
    #retrieving form data
    if request.method == 'POST':
        name=request.form['name']
        email=request.form['email']
        destination=request.form['destination']
        itinerary=request.form['itinerary']
        
        # Sending email
        app.config['MANDRILL_API_KEY'] = 'UUs-Wadj9AtJ4fMqC45SrQ'
        mandrill = Mandrill(app)
        mandrill.send_email(
        from_email='judasane@gmail.com',
            to=[{'email': email}],
        text='Hello'+name,
        subject="Welcome "+name
            )
            
        # Saving in database            
        client = MongoClient(host='mongodb://test:TestBuggl@ds041633.mongolab.com:41633/buggl')
        db = client.buggl
    
        result = db.entries.insert_one({
        "name": name,
        "email": email,
        "destination": destination,
        "itinerary": itinerary,
        
        })
        
        #return
        return "Thank you "+name+". We've sent an email to: "+email+", informing you want "+itinerary+" in your trip"
        
    else:
        return render_template('index.html')

@app.route('/expert/',methods=['GET', 'POST'])
def expert():
    #retrieving form data
    if request.method == 'POST':
        name=request.form['name']
        email=request.form['email']
        destination=request.form['destination']
        itinerary=request.form['itinerary']
        plan=request.form['plan']
        
        # Sending email
        app.config['MANDRILL_API_KEY'] = 'UUs-Wadj9AtJ4fMqC45SrQ'
        mandrill = Mandrill(app)
        mandrill.send_email(
        from_email='judasane@gmail.com',
            to=[{'email': email}],
        text='Hello '+name,
        subject="Welcome "+name
            )
            
        # Saving in database            
        client = MongoClient(host='mongodb://test:TestBuggl@ds041633.mongolab.com:41633/buggl')
        db = client.buggl
    
        result = db.entries.insert_one({
        "name": name,
        "email": email,
        "destination": destination,
        "itinerary": itinerary,
        "plan": plan
        
        
        })
        
        #return
        return "Thank you "+name+". We've sent an email to: "+email+", informing you want "+itinerary+" in your trip and you want the  "+plan+" plan"
        
    else:
        return render_template('expert.html')




@app.route('/<username>')
def show_user_profile(username):
# show the user profile for that user
    return 'Hola %s' % username

@app.route("/hola/")
def hola():
    return render_template('hola.html')
    
    
@app.route('/form/', methods=['GET', 'POST'])
def form():
    #retrieving form data
    if request.method == 'POST':
        name=request.form['name']
        email=request.form['email']
        category=request.form['trip_category']
        plan=request.form['plan']
        
        # Sending email
        app.config['MANDRILL_API_KEY'] = 'UUs-Wadj9AtJ4fMqC45SrQ'
        mandrill = Mandrill(app)
        mandrill.send_email(
        from_email='judasane@gmail.com',
            to=[{'email': email}],
        text='Hello'+name,
        subject="Welcome "+name
            )
            
        # Saving in database            
        client = MongoClient(host='mongodb://test:TestBuggl@ds041633.mongolab.com:41633/buggl')
        db = client.buggl
    
        result = db.entries.insert_one({
        "plan": plan,
        "trip_category": category,
        "email": email,
        "name": name
        })
        
        #return
        return "Thank you "+name+". We've sent an email to: "+email+", informing you want "+category+" category and you want the  "+plan+" plan"
        
    else:
        return render_template('form.html')



if __name__ == '__main__':
    app.debug = True
    
    app.config['MONGO_URI'] = 'mongodb://test:TestBuggl@ds041633.mongolab.com:41633/buggl'
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
    # url_for('static/css', filename='buggl.css') 

# app.run(host=os.getenv(IP, 0.0.0.0))
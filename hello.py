import os
from flask import render_template
from flask import url_for
from flask import Flask
from flask import request
from flask.ext.mandrill import Mandrill
# app = Flask(__name__)

app = Flask(__name__, static_url_path='')

@app.route('/')
def hello_world():
    return 'Hola !'

@app.route('/<username>')
def show_user_profile(username):
# show the user profile for that user
    return 'Hola %s' % username

@app.route("/hola/")
def hola():
    return render_template('hola.html')
    
    
@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name=request.form['name']
        email=request.form['email']
        category=request.form['trip_category']
        plan=request.form['plan']
        
        app.config['MANDRILL_API_KEY'] = 'UUs-Wadj9AtJ4fMqC45SrQ'
        mandrill = Mandrill(app)
        mandrill.send_email(
        from_email='judasane@gmail.com',
            to=[{'email': email}],
        text='Hello'+name,
        subject="Welcome "+name
        
            )
        
        return "Thank you "+name+". We've sent an email to: "+email+", informing you want "+category+" category and you want the  "+plan+" plan"
        
    else:
        return render_template('form.html')

# if __name__ == '__main__':
    # app.debug = True
    # app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
    # url_for('static/css', filename='buggl.css') 

# app.run(host=os.getenv(IP, 0.0.0.0))
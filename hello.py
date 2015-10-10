import os
from flask import render_template
from flask import url_for
from flask import Flask
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

@app.route("/form/")
def form():
    return render_template('form.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
    url_for('static/css', filename='buggl.css') 
   
    
    # app.run(host=os.getenv(IP, 0.0.0.0))
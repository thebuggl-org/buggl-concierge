from flask import Flask
from flask.ext.mandrill import Mandrill

app = Flask(__name__)
app.config['MANDRILL_API_KEY'] = 'UUs-Wadj9AtJ4fMqC45SrQ'
mandrill = Mandrill(app)
mandrill.send_email(
    from_email='judasane@gmail.com',
    to=[{'email': 'judasane@gmail.com'}],
    text='Hello World'
)
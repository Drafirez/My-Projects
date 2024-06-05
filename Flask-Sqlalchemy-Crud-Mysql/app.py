from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# settings
app.secret_key = 'mysecret'
SERVER_NAME = 'localhost'
app.config = SQLALCHEMY_DATABASE_URI = f'mysql://root:12345678@{SERVER_NAME}:3307/contactsdb'
app.config = SQLALCHEMY_TRACK_MODIFICATIONS = False



app.register_blueprint(contacts)
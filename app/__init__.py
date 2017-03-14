from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Config Values
UPLOAD_FOLDER = './app/static/profile_imgs'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Project-1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://project1:project1@localhost/project1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
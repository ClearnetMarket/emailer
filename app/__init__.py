# coding=utf-8
from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from config import ApplicationConfig


app = Flask(__name__,
            static_url_path='',
            static_folder="static",
            template_folder="templates")


app.config.from_object('ApplicationConfig')
Session = sessionmaker()
Session.configure(bind=ApplicationConfig.SQLALCHEMY_DATABASE_URI_0)

db = SQLAlchemy(app)
mail = Mail(app)

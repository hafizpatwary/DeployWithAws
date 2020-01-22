from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import pymysql
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{getenv('MYSQL_USERNAME')}:{getenv('MYSQL_PASSWORD')}@{getenv('MYSQL_IP')}/yeezyjet"
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

db = SQLAlchemy(app)
#xray_recorder.configure(service='harry')
xray_recorder.configure(service='harry', dynamic_naming='*18.130.174.90*')
XRayMiddleware(app, xray_recorder)

from application import routes

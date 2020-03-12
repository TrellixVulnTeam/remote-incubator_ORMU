from flask import Flask
from flask_restplus import Resource, Api
from flask_sqlalchemy import SQLAlchemy


# Instantiating Flask
app = Flask(__name__)
# Configuration of flask object
app.config['SECRET_KEY']='57333b23060b97386c2ed279e796e6fe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysqL2016@localhost/incubator'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# creating a flask-restplus object
api = Api(app=app, version='1.0', title='remote INCUBATOR', description='Manage various tables of incubator database')


db = SQLAlchemy(app)

from myPackage import routes



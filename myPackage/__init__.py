import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Getting user and password for database connection
db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASSWORD')

# Instantiating Flask
app = Flask(__name__)
# Configuration of flask object
app.config['SECRET_KEY']='57333b23060b97386c2ed279e796e6fe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+db_user+':'+db_pass+'@localhost/incubator'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

from myPackage import routes



from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


app=Flask(__name__)
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
app.secret_key='flaskapi'
api=Api(app)

db=SQLAlchemy(app)
Migrate(app,db)

from mypackage.resources.user import UserRegister
from mypackage.resources.items import ItemResource
from mypackage.resources.stores import StoreResource,StoreList

api.add_resource(UserRegister,'/register')
api.add_resource(StoreResource,'/store/<string:name>')
api.add_resource(StoreList,'/stores')
api.add_resource(ItemResource,'/item/<string:name>')

















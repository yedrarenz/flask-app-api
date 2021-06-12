from app import flask_app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Database
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init DB
db = SQLAlchemy(flask_app)
# Init MA
ma = Marshmallow(flask_app)


# User Class/Model
class UserDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    team = db.Column(db.String(100))

    def __init__(self, name, team):
        self.name = name
        self.team = team


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'team')


user_schema = UserSchema()
users_schema = UserSchema(many=True)





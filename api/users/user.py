from flask import request
from flask import jsonify

from flask_restful import Resource
import logging as logger

from db.database import UserDB
from db.database import db, user_schema

logger.basicConfig(level="DEBUG")


class User(Resource):

    def get(self):
        logger.debug("Get user invoked.")
        return {"message" : "get id"}

    def post(self):
        logger.debug("Post user invoked.")
        name = request.json['name']
        team = request.json['team']

        new_user = UserDB(name, team)

        db.session.add(new_user)
        db.session.commit()


        logger.debug('New user added', new_user)
        return user_schema.jsonify(new_user)

    def put(self):
        logger.debug("Put user invoked.")
        return {"message" : "get id"}

    def delete(self):
        logger.debug("Delete user invoked.")
        return {"message" : "get id"}
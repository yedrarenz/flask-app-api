from flask import request
from flask import jsonify

from flask_restful import Resource
import logging as logger

from db.database import UserDB
from db.database import db, user_schema

logger.basicConfig(level="DEBUG")



class UserID(Resource):

    def get(self, userid):
        logger.debug("Get user invoked.")
        user = UserDB.query.get(userid)
        logger.debug(user)
        return user_schema.jsonify(user)

    def post(self, userid):
        logger.debug("Post user invoked.")
        return {"message" : f"post id {userid}"}


    def put(self, userid):
        logger.debug("Put user invoked.")
        user = UserDB.query.get(userid)

        name = request.json['name']
        team = request.json['team']

        user.name = name
        user.team = team

        db.session.commit()

        logger.debug('New user added', user)
        return user_schema.jsonify(user)


    def delete(self, userid):
        logger.debug("Get user invoked.")
        del_user = UserDB.query.get(userid)

        db.session.delete(del_user)
        db.session.commit()
        
        logger.debug(del_user)
        return user_schema.jsonify(del_user)
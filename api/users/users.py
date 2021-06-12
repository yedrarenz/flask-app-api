from flask import request
from flask import jsonify

from flask_restful import Resource
import logging as logger

from db.database import UserDB
from db.database import db, user_schema, users_schema

logger.basicConfig(level="DEBUG")


class Users(Resource):

    def get(self):
        logger.debug("Get user invoked.")
        all_users = UserDB.query.all()
        result = users_schema.dump(all_users)
        return jsonify(result)
from flask_restful import Api
from flask_cors import CORS, cross_origin

from app import flask_app
from api.users.user import User
from api.users.users import Users
from api.users.userid import UserID

rest_server = Api(flask_app)
rest_server.add_resource(User, "/api/v1.0/user")
rest_server.add_resource(Users, "/api/v1.0/users")
rest_server.add_resource(UserID, "/api/v1.0/user/id/<string:userid>")
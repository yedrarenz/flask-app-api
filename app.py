from logging import debug
from flask import Flask
from flask_cors import CORS, cross_origin


flask_app = Flask(__name__)
CORS(flask_app, support_credentials=True)


if __name__ == "__main__":
    from api import *
    flask_app.run(host='0.0.0.0', port=5000, debug=True)
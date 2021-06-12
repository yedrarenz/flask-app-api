from logging import debug
from flask import Flask


flask_app = Flask(__name__)


if __name__ == "__main__":
    from api import *
    flask_app.run(host='0.0.0.0', port=5000, debug=True)
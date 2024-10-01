import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

load_dotenv()

if os.getenv("USE_FLASK_CORS") == "true":
    app = Flask(__name__)
    CORS(app)
else:
    app = Flask(__name__, static_folder="client/dist", static_url_path="")

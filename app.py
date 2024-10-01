import os

from dotenv import load_dotenv
from flask import Flask, jsonify, send_from_directory  # noqa
from flask_cors import CORS

load_dotenv()

if os.getenv("USE_FLASK_CORS") == "true":
    app = Flask(__name__)
    CORS(app)

    @app.route("/")
    def index():
        return "Hello, World!"

else:
    app = Flask(__name__, static_folder="client/dist", static_url_path="")

    @app.route("/")
    def server_vue_index():
        return send_from_directory(app.static_folder, "index.html")

    @app.route("/<path:path>")
    def server_vue_static(path):
        return send_from_directory(app.static_folder, path)

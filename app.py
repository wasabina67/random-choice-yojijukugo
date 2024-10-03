import json
import os
import random

from dotenv import load_dotenv
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS  # type: ignore
from redis import Redis

load_dotenv(override=True)

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


@app.route("/api/yojijukugo", methods=["GET"])
def apt_yojijukugo_get():
    with open("data.json", "r", encoding="utf-8") as f:
        data_list = json.load(f)

    r = Redis(host="localhost", port=6379)
    print(f'{r.incr("hits")} times.')

    return jsonify(random.choice(data_list))


if __name__ == "__main__":
    app.run(debug=True)

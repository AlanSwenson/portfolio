from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["POST", "GET"])
    def root():
        return "<h1>Hello World</h1>"

    return app

from flask import Flask, render_template

from portfolio.config import DevelopmentConfig


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__, static_url_path="/static")
    app.config.from_object(config_class)

    @app.route("/", methods=["POST", "GET"])
    def root():
        return render_template("layout.html", title="Alan Swenson - Portfolio")

    return app

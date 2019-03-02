from flask import Flask, render_template


def create_app():
    app = Flask(__name__, static_url_path="/static")

    @app.route("/", methods=["POST", "GET"])
    def root():
        return render_template("layout.html", title="Alan Swenson - Portfolio")

    return app

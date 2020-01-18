import os

from flask import Flask, render_template

from portfolio.config import DevelopmentConfig


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__, static_url_path="/static")
    app.config.from_object(config_class)

    @app.route("/", methods=["POST", "GET"])
    def root():
        return render_template("layout.html", title="Alan Swenson - Portfolio")

    @app.route("/restaurant/", methods=["POST", "GET"])
    def restaurant():
        class MenuItem:
            def __init__(self, name, price, description):
                self.name = name
                self.price = price
                self.description = description

        menu_items = []
        menu_items.append(
            MenuItem("Tornado Potato", "8", "anju salt blend, furikake, citrus aioli")
        )

        # Add or remove images from 'static/img/gallery'
        # to include them in the gallery section
        images = os.listdir(os.path.join(app.static_folder, "img/restaurant/carousel"))

        return render_template(
            "restaurant_body.html",
            title="Restaurant Example - Alan Swenson - Portfolio",
            images=images,
            menu_items=menu_items,
        )

    return app

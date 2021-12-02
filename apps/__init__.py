from flask import Flask


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    from apps import routes

    app.register_blueprint(routes.bp)

    return app

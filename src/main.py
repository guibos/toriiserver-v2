import os

from flask import Flask

from src.application.graphql import handler
from src.application.streamer import streamer
from src.infrastructure.database.base import db_session


class App:
    def __init__(self, database_facade):
        self._database_facade = database_facade


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'database.sqlite3'),
    )

    if config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(config)

    app.register_blueprint(handler.bp)
    app.register_blueprint(streamer.bp)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app


app = create_app()
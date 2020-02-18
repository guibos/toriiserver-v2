import os

from flask import Flask

from src.application.graphql.handler import GraphQLHandler
from src.infrastructure.database.facade import DatabaseFacade


class App:
    def __init__(self, database_facade: DatabaseFacade, config=None,):
        self._app = Flask(__name__, instance_relative_config=True)

        try:
            os.makedirs(self._app.instance_path)
        except OSError:
            pass

        self._app.config.from_mapping(
            SECRET_KEY='dev',
        )

        if config is None:
            # load the instance config, if it exists, when not testing
            self._app.config.from_pyfile('config.py', silent=True)
        else:
            # load the test config if passed in
            self._app.config.from_mapping(config)

        scoped_session = database_facade.get_scoped_session()

        self._app.register_blueprint(GraphQLHandler(scopped_session=scoped_session).blueprint)

        @self._app.teardown_appcontext
        def shutdown_session(exception=None):
            scoped_session.remove()

    def run(self, *args, **kwargs):
        self.run(*args, **kwargs)


def create_app():
    database_facade =
    App(database_facade=da)

    return app

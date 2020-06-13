import os

from flask import Flask

from src.application.graphql.handler import GraphQLHandler
from src.infrastructure.configuration.configuration_repository import Configuration
from src.infrastructure.database.facade import DatabaseFacade
from src.infrastructure.database.value_objects.database_url_value_object import DatabaseURLValueObject


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

        self._app.register_blueprint(GraphQLHandler(scoped_session=scoped_session).blueprint)

        @self._app.teardown_appcontext
        def shutdown_session(exception=None):
            scoped_session.remove()

    def run(self, *args, **kwargs):
        self._app.run(*args, **kwargs)


def create_app(*, arguments):
    configuration = Configuration(environment=arguments.environment)
    database_facade = DatabaseFacade(
        database_url_config=DatabaseURLValueObject(**configuration.get_section(section='database')))
    app = App(database_facade=database_facade)

    return app

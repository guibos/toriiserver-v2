from flask import Blueprint, request
from flask_graphql import GraphQLView

from src.application.graphql.schemas.schema import schema


class GraphQLHandler:
    _HANDLER_NAME = 'graphql'
    _HANDLER_URL_PREFIX = '/graphql'

    def __init__(self, *, scoped_session):
        self._blueprint = Blueprint(self._HANDLER_NAME, __name__, url_prefix=self._HANDLER_URL_PREFIX)
        self._blueprint.add_url_rule(
            '/',
            view_func=GraphQLView.as_view(
                self._HANDLER_NAME,
                schema=schema,
                graphiql=True,
                get_context=lambda: {'session': scoped_session, 'request': request}))

    @property
    def blueprint(self) -> Blueprint:
        return self._blueprint

from flask import Blueprint, request
from flask_graphql import GraphQLView

from src.application.graphql.schemas.schema import schema
from src.infrastructure.database.base import db_session
from src.infrastructure.database.facade import DatabaseFacade


class GraphQLHandler:
    def __init__(self, database_facade: DatabaseFacade):
        self._database_facade
        bp = Blueprint('graphql', __name__, url_prefix='/graphql')
        bp.add_url_rule(
            '/',
            view_func=GraphQLView.as_view(
                'graphql',
                schema=schema,
                graphiql=True,
                get_context=lambda: {'session': db_session, 'request': request}
         ))

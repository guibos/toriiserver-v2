from flask import Blueprint
from flask_graphql import GraphQLView

from src.application.graphql.schemas.schema import schema
from src.infrastructure.database.base import db_session


class MyGraphQLView(GraphQLView):
    def get_context(self):
        context = super().get_context()
        context.session = db_session
        return context


bp = Blueprint('graphql', __name__, url_prefix='/graphql')
bp.add_url_rule('/', view_func=MyGraphQLView.as_view('graphql', schema=schema, graphiql=True,
                                                   ))

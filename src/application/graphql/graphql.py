from flask import Blueprint
from flask_graphql import GraphQLView

from src.application.graphql.schemas.schema import schema

bp = Blueprint('graphql', __name__, url_prefix='/graphql')
bp.add_url_rule('/ds', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType

from src.application.graphql import utils
from src.infrastructure.database.models.title_model import TitleModel
import graphene
from flask import request


# Create a generic class to mutualize description of people attributes for both queries and mutations
class TitleAttribute:
    name = graphene.String(description="Name of the title.")
    user_id = graphene.Int(description="Name of the title.")


class Title(SQLAlchemyObjectType):
    """People node."""

    class Meta:
        model = TitleModel
        interfaces = (graphene.relay.Node,)


class CreateTitleInput(graphene.InputObjectType, TitleAttribute):
    """Arguments to create a title."""
    pass


class CreateTitle(graphene.Mutation):
    """Mutation to create a title."""
    title = graphene.Field(lambda: Title, description="Title created by this mutation.")

    class Arguments:
        input = CreateTitleInput(required=True)

    def mutate(self, info, input):


        title = TitleModel(**data)
        db_session.add(title)
        db_session.commit()

        return CreateTitle(title=title)


class UpdateTitleInput(graphene.InputObjectType, TitleAttribute):
    """Arguments to update a title."""
    id = graphene.ID(required=True, description="Global Id of the title.")


class UpdateTitle(graphene.Mutation):
    """Update a title."""
    title = graphene.Field(lambda: Title, description="Title updated by this mutation.")

    class Arguments:
        input = UpdateTitleInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        title = db_session.query(TitleModel).filter_by(id=data['id'])
        title.update(data)
        db_session.commit()
        title = db_session.query(TitleModel).filter_by(id=data['id']).one()

        return UpdateTitle(title=title)

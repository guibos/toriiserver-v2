from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType

from src.application.graphql import utils
from src.application.graphql.schemas.schema_features import SchemaFeatures
from src.infrastructure.database.models.user_model import UserModel
import graphene


# Create a generic class to mutualize description of people attributes for both queries and mutations
class UserAttribute:
    username = graphene.String(description="Name of the user.",)


class User(SQLAlchemyObjectType):
    """People node."""

    class Meta:
        model = UserModel
        interfaces = (graphene.relay.Node,)


class CreateUserInput(graphene.InputObjectType, UserAttribute):
    """Arguments to create a user."""
    pass


class CreateUser(graphene.Mutation, SchemaFeatures):
    """Mutation to create a user."""
    user = graphene.Field(lambda: User, description="User created by this mutation.")

    class Arguments:
        user_data = CreateUserInput(required=True)

    @staticmethod
    def mutate(info, user_data):
        session = self._get_session(info=info)
        data = utils.input_to_dictionary(user_data)
        user = UserModel(**data)
        session.add(user)
        session.commit()

        return CreateUser(user=user)


class UpdateUserInput(graphene.InputObjectType, UserAttribute):
    """Arguments to update a user."""
    id = graphene.ID(required=True, description="Global Id of the user.")


class UpdateUser(graphene.Mutation):
    """Update a user."""
    user = graphene.Field(lambda: User, description="User updated by this mutation.")

    class Arguments:
        input = UpdateUserInput(required=True)

    def mutate(self, info, input):
        session = self._get_session(info=info)
        data = utils.input_to_dictionary(input)

        user = session.query(UserModel).filter_by(id=data['id'])
        user.update(data)
        session.commit()
        user = session.query(UserModel).filter_by(id=data['id']).one()

        return UpdateUser(user=user)

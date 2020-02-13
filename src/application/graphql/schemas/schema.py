from graphene_sqlalchemy import SQLAlchemyConnectionField
import graphene

from src.application.graphql.schemas import user_schema, title_schema


class Query(graphene.ObjectType):
    """Nodes which can be queried by this API."""
    node = graphene.relay.Node.Field()

    user = graphene.relay.Node.Field(user_schema.User)
    users = SQLAlchemyConnectionField(user_schema.User)

    title = graphene.relay.Node.Field(title_schema.Title)
    titles = SQLAlchemyConnectionField(title_schema.Title)


class Mutation(graphene.ObjectType):
    """Mutations which can be performed by this API."""
    create_user = user_schema.CreateUser.Field()
    update_user = user_schema.UpdateUser.Field()

    create_title = title_schema.CreateTitle.Field()
    update_title = title_schema.UpdateTitle.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

# app/graphql/schema.py
import strawberry
from strawberry.fastapi import GraphQLRouter

from app.graphql.mutations.auth import AuthMutation
from app.graphql.queries.user import UserQuery


@strawberry.type
class Query(UserQuery):
    pass

@strawberry.type
class Mutation(AuthMutation):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

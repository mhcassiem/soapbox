# app/graphql/schema.py
import strawberry
from strawberry.fastapi import GraphQLRouter

from app.graphql.mutations.auth import AuthMutation
from app.graphql.mutations.user_profile import UserProfileMutation
from app.graphql.queries.user import UserQuery
from app.graphql.queries.user_profile import UserProfileQuery


@strawberry.type
class Query(
    UserQuery,
    UserProfileQuery,
):
    pass

@strawberry.type
class Mutation(
    AuthMutation,
    UserProfileMutation,
):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

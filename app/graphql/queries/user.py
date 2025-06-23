# app/graphql/queries/user.py
import strawberry
from fastapi import Request

from app.auth.dependencies import get_current_user_from_request
from app.db import get_db
from app.graphql.resolvers.user import to_user_type
from app.graphql.types.user_types import UserType


@strawberry.type
class UserQuery:
    @strawberry.field
    def me(self, info) -> UserType | None:
        request: Request = info.context["request"]
        db = next(get_db())
        user = get_current_user_from_request(request, db)
        return to_user_type(user) if user else None

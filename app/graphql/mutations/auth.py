# app/graphql/mutations/auth.py
import strawberry
from fastapi import Response
from sqlalchemy.orm import Session

from app.auth import password as auth_password
from app.auth.utils import create_access_token, set_access_token_cookie
from app.db import get_db
from app.graphql.types.user_types import UserType


@strawberry.type
class AuthMutation:
    @strawberry.mutation
    def register_user(
            self,
            info,
            email: str,
            password: str,
            full_name: str | None = None
    ) -> UserType:
        db: Session = next(get_db())
        user = auth_password.register_user(db, email, password, full_name)
        token = create_access_token({"sub": str(user.id)})
        response: Response = info.context["response"]
        set_access_token_cookie(response, token)
        return UserType(**user.__dict__)

    @strawberry.mutation
    def login_user(self, info, email: str, password: str) -> str:
        db: Session = next(get_db())
        token = auth_password.authenticate_user(db, email, password)
        if not token:
            raise Exception("Invalid credentials")
        return token

    @strawberry.mutation
    def logout_user(self, info) -> bool:
        response: Response = info.context["response"]
        response.delete_cookie("token_cookie")
        return True

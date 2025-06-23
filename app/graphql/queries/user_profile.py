# app/graphql/queries/user_profile.py
import strawberry
from fastapi import Request
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.users.models import UserProfile
from app.db import get_db
from app.graphql.types.user_profile_types import UserProfileType


@strawberry.type
class UserProfileQuery:
    @strawberry.field
    def get_profile(self, info) -> UserProfileType | None:
        request: Request = info.context["request"]
        db: Session = next(get_db())
        user = get_current_user(request, db)

        if not user:
            raise Exception("Authentication required")

        profile = db.query(UserProfile).filter(UserProfile.user_id == user.id).first()
        if not profile:
            raise Exception("Profile not found")
        return UserProfileType(**profile.__dict__) if profile else None

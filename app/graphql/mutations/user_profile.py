# app/graphql/mutations/user_profile.py
import strawberry
from fastapi import Request
from sqlalchemy.orm import Session
from app.db import get_db
from app.auth.dependencies import get_current_user
from app.users.models import UserProfile
from app.graphql.types.user_profile_types import UserProfileType
from app.graphql.types.user_profile_input import UserProfileInput


@strawberry.type
class UserProfileMutation:
    @strawberry.mutation
    def create_or_update_profile(self, info, data: UserProfileInput) -> UserProfileType:
        request: Request = info.context["request"]
        db: Session = next(get_db())
        user = get_current_user(request, db)
        if not user:
            raise Exception("Authentication required")

        profile = db.query(UserProfile).filter(UserProfile.user_id == user.id).first()

        if profile:
            for field, value in data.__dict__.items():
                setattr(profile, field, value)
        else:
            profile = UserProfile(user_id=user.id, **data.__dict__)
            db.add(profile)

        db.commit()
        db.refresh(profile)
        return UserProfileType(**{key: value for key, value in profile.__dict__.items() if not key.startswith("_")})

# app/graphql/types/user_profile_type.py
import strawberry
from datetime import datetime

from app.graphql.types.user_types import UserType


@strawberry.type
class UserProfileType:
    id: int
    user: UserType
    display_name: str | None
    bio: str | None
    avatar_url: str | None
    location: str | None
    website: str | None
    twitter: str | None
    github: str | None
    is_creator: bool
    created_at: datetime
    updated_at: datetime

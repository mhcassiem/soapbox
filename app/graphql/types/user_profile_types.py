# app/graphql/types/user_profile_type.py
import strawberry
from datetime import datetime

@strawberry.type
class UserProfileType:
    id: int
    user_id: int
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

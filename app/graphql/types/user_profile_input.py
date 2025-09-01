# app/graphql/types/user_profile_input.py
import strawberry

@strawberry.input
class UserProfileInput:
    bio: str | None = None
    avatar_url: str | None = None
    location: str | None = None
    website: str | None = None

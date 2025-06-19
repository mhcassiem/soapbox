from app.graphql.types.user_types import UserType
from app.users.models import User


def to_user_type(user: User) -> UserType:
    return UserType(
        id=user.id,
        email=user.email,
        full_name=user.full_name,
        auth_provider=user.auth_provider,
        has_password=user.hashed_password is not None,
    )
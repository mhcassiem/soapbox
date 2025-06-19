import strawberry


# Output type
@strawberry.type
class UserType:
    id: int
    email: str
    full_name: str | None
    auth_provider: str
    has_password: bool


from pydantic import BaseModel, EmailStr


# ----- Shared Schemas -----
class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None

class UserOut(UserBase):
    id: int
    auth_provider: str
    has_password: bool

    class Config:
        from_attributes = True
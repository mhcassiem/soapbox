# app/auth/schema.py

from pydantic import BaseModel, EmailStr, constr, field_validator


# ----- Registration -----
class RegisterData(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str

    @field_validator("confirm_password")
    def passwords_match(cls, v, values):
        if "password" in values.data and v != values.data["password"]:
            raise ValueError("Passwords do not match")
        return v


# ----- Login -----
class LoginData(BaseModel):
    email: EmailStr
    password: str


# ----- Set Password (for Google users who want to add a password) -----
class SetPasswordData(BaseModel):
    password: constr(min_length=6)
    confirm_password: constr(min_length=6)

    @field_validator("confirm_password")
    def passwords_match(cls, v, values):
        if "password" in values.data and v != values.data["password"]:
            raise ValueError("Passwords do not match")
        return v

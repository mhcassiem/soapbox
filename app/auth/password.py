# app/auth/password.py
from sqlalchemy.orm import Session

from app.auth.utils import create_access_token, hash_password, verify_password
from app.users import models


def register_user(
        db: Session,
        email: str,
        password: str,
        full_name: str | None = None
) -> models.User:
    user = db.query(models.User).filter(models.User.email == email).first()
    if user:
        raise ValueError("User already exists")

    hashed = hash_password(password)
    new_user = models.User(
        email=email,
        hashed_password=hashed,
        full_name=full_name,
        auth_provider="local"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def authenticate_user(db: Session, email: str, password: str) -> str | None:
    user = db.query(models.User).filter(models.User.email == email).first()

    if not user:
        return None

    # Deny if user has no password set
    if not user.hashed_password:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return create_access_token({"sub": str(user.id)})

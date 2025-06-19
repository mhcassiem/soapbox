# app/auth/dependencies.py
from fastapi import Depends, Request
from sqlalchemy.orm import Session

from app.auth.utils import decode_access_token
from app.db import get_db
from app.users import models


def get_current_user_from_request(
    request: Request,
    db: Session,
) -> models.User | None:
    # Extract token from Authorization header or cookie
    auth_header = request.headers.get("Authorization")
    token = None

    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]
    elif cookie := request.cookies.get("access_token_cookie"):
        token = cookie

    if not token:
        return None

    payload = decode_access_token(token)
    if not payload:
        return None

    user_id = payload.get("sub")
    if not user_id:
        return None

    return db.query(models.User).filter(models.User.id == int(user_id)).first()


def get_current_user(
    request: Request,
    db: Session = Depends(get_db),
) -> models.User | None:
    return get_current_user_from_request(request, db)

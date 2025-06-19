import secrets

from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.auth import google, password
from app.auth.dependencies import get_current_user
from app.auth.schema import LoginData, RegisterData, SetPasswordData
from app.auth.utils import create_access_token, hash_password, set_access_token_cookie
from app.config import settings
from app.db import get_db
from app.users.models import User

router = APIRouter()


@router.post("/register")
def register_user(data: RegisterData, db: Session = Depends(get_db)):
    user = password.register_user(db, str(data.email), data.password)
    token = create_access_token({"sub": str(user.id)})
    return {"access_token_cookie": token}


@router.post("/login")
def login(data: LoginData, response: Response, db: Session = Depends(get_db)):
    token = password.authenticate_user(db, str(data.email), data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    set_access_token_cookie(response, token)
    return {"message": "Login successful"}


@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie(
        key="access_token_cookie",
        path="/",
        httponly=True,
        secure=settings.ENV == "production",
        samesite="lax",
    )
    return {"message": "Logged out successfully"}


# === Google OAuth Routes ===

@router.get("/google/login")
async def login_with_google(request: Request):
    nonce = secrets.token_urlsafe(16)
    request.session["nonce"] = nonce
    result = await google.get_google_redirect_url(request, nonce)
    return result


@router.get("/google/callback")
async def google_callback(request: Request, db: Session = Depends(get_db)):
    token = await google.handle_google_callback(request, db)
    # Send token to frontend via URL fragment
    response = RedirectResponse(url=f"{settings.FRONTEND_URL}/auth/callback")
    # Set a secure, HttpOnly cookie (expires in 1 hour for example)
    set_access_token_cookie(response, token)
    return response


@router.post("/set-password")
def set_password(
        data: SetPasswordData,
        user: User = Depends(get_current_user),
        db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    if user.hashed_password:
        raise HTTPException(status_code=400, detail="Password already set")
    if data.password != data.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    user = db.merge(user)
    user.hashed_password = hash_password(data.password)
    db.commit()
    return {"message": "Password set successfully"}

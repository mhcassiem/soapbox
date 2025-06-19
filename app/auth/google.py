# app/auth/google.py
from authlib.integrations.starlette_client import OAuth
from fastapi import HTTPException, Request
from sqlalchemy.orm import Session
from starlette.config import Config

from app.auth.utils import create_access_token
from app.config import settings
from app.users import models

# Authlib OAuth setup
config_data = {
    "GOOGLE_CLIENT_ID": settings.GOOGLE_CLIENT_ID,
    "GOOGLE_CLIENT_SECRET": settings.GOOGLE_CLIENT_SECRET
}
config = Config(environ=config_data)

oauth = OAuth(config)
oauth.register(
    name='google',
    client_id=settings.GOOGLE_CLIENT_ID,
    client_secret=settings.GOOGLE_CLIENT_SECRET,
    access_token_url='https://oauth2.googleapis.com/token',
    authorize_url='https://accounts.google.com/o/oauth2/v2/auth',
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={'scope': 'openid email profile'},
)

# Step 1: Get redirect URL
def get_google_redirect_url(request: Request, nonce: str) -> str:
    redirect_uri = settings.GOOGLE_REDIRECT_URI
    return oauth.google.authorize_redirect(request, redirect_uri, nonce=nonce)

# Step 2: Handle callback
async def handle_google_callback(request: Request, db: Session) -> str:
    token = await oauth.google.authorize_access_token(request)

    nonce = request.session.get("nonce")
    if not nonce:
        raise HTTPException(status_code=400, detail="Missing nonce in session")

    user_info = await oauth.google.parse_id_token(token, nonce=nonce)

    email = user_info.get("email")
    full_name = user_info.get("name")
    # picture = user_info.get("picture")

    # Check if user exists or create
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        user = models.User(
            email=email,
            full_name=full_name,
            auth_provider="google",
            hashed_password=None
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    # Issue JWT
    return create_access_token({"sub": str(user.id)})

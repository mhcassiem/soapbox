from fastapi import APIRouter, Depends, HTTPException, Request

from app.auth.dependencies import get_current_user
from app.users.models import User
from app.users.schema import UserOut

router = APIRouter()


@router.get("/me", response_model=UserOut)
async def read_me(request: Request, user: User = Depends(get_current_user)):
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    return {
        "id": user.id,
        "email": user.email,
        "full_name": user.full_name,
        "auth_provider": user.auth_provider,
        "has_password": bool(user.hashed_password),
    }

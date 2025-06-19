# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from app.auth.routes import router as auth_router
from app.config import settings
from app.graphql.schema import graphql_app
from app.users.routes import router as users_router


def create_app() -> FastAPI:
    app = FastAPI(debug=settings.DEBUG)

    # 🔐 Middleware
    app.add_middleware(
        SessionMiddleware,
        secret_key=settings.SESSION_SECRET_KEY,
        https_only=settings.ENV == "production"
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 🔌 Routers / GraphQL
    app.include_router(auth_router, prefix="/auth")
    app.include_router(users_router, prefix="/users")
    app.include_router(graphql_app, prefix="/graphql")

    return app

app = create_app()

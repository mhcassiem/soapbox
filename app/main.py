# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from app.auth.routes import router as auth_router
from app.config import settings
from app.db import Base, engine
from app.graphql.schema import graphql_app
from app.users.routes import router as users_router


def create_app() -> FastAPI:
    # Create DB tables
    Base.metadata.create_all(bind=engine)

    backend_app = FastAPI(debug=settings.DEBUG)

    # 🔐 Middleware
    backend_app.add_middleware(
        SessionMiddleware,
        secret_key=settings.SESSION_SECRET_KEY,
        https_only=settings.ENV == "production"
    )
    backend_app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 🔌 Routers / GraphQL
    backend_app.include_router(auth_router, prefix="/auth")
    backend_app.include_router(users_router, prefix="/users")
    backend_app.include_router(graphql_app, prefix="/graphql")

    return backend_app

app = create_app()

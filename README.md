# Soapbox Backend

The backend service for Soapbox, built with FastAPI, Strawberry GraphQL, and PostgreSQL.

## Features

- Google OAuth and email/password authentication
- GraphQL and REST APIs
- User session/token management
- Modular and scalable FastAPI project structure
- PostgreSQL + SQLAlchemy ORM

## Project Structure
```
backend/
├── app/
│   ├── auth/
│   │   ├── password.py
│   │   ├── routes.py
│   │   └── utils.py
│   ├── db/
│   │   ├── base.py
│   │   └── session.py
│   ├── graphql/
│   │   ├── resolvers/
│   │   │   └── user.py
│   │   ├── schema.py
│   │   └── types/
│   │       └── user_type.py
│   ├── models/
│   │   └── user.py
│   └── main.py
├── tests/
│   └── test_auth.py
├── .env
├── .gitignore
├── pyproject.toml
└── README.md
```


## Setup

```bash
cd backend
poetry install
poetry shell
uvicorn app.main:app --reload

GraphiQL available at: http://localhost:8000/graphql


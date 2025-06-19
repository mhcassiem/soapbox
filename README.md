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
│   │   ├── dependencies.py
│   │   ├── google.py
│   │   ├── password.py
│   │   ├── routes.py
│   │   ├── schema.py
│   │   └── utils.py
│   ├── graphql/
│   │   ├── mutations/
│   │   │   └── auth.py
│   │   ├── queries/
│   │   │   └── user.py
│   │   ├── types/
│   │   │   └── user_type.py
│   │   ├── resolvers.py
│   │   ├── schema.py
│   ├── users/
│   │   ├── models.py
│   │   ├── routes.py
│   │   └── schema.py
│   ├── config.py
│   ├── db.py
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


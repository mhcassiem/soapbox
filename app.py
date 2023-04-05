from flask import Flask

from apps.shared.app import migrate, login_manager
from apps.shared.models import db


def create_app():
    app = Flask(__name__)
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    return app

import os

from flask import Flask

from apps.shared.app import migrate
from apps.auth.app import login_manager
from apps.shared.models import db
from apps.auth.routes import auth
from apps.shared.routes import shared


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(shared)
    app.register_blueprint(auth)
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    return app

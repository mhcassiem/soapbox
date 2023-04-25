import os

from flask import Flask

from apps.shared.models import db
from apps.shared.app import migrate, jwt, mail
from apps.shared.routes import shared
from apps.api.routes import api
from apps.error_handlers.routes import error_handlers
from apps.auth.app import security
from apps.utils.logger import configure_logger
from apps.graphql_api.routes import graphql


def create_app():
    configure_logger()
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(shared)
    app.register_blueprint(error_handlers)
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(graphql)
    db.init_app(app)
    security.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    return app

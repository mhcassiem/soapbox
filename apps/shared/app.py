from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()
basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()
migrate = Migrate()

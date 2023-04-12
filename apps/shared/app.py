from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_migrate import Migrate


basic_auth = HTTPBasicAuth()
jwt = JWTManager()
migrate = Migrate()
mail = Mail()

from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_migrate import Migrate


jwt = JWTManager()
migrate = Migrate()
mail = Mail()

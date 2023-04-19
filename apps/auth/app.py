from flask_security import SQLAlchemyUserDatastore, Security

from apps.api.errors import error_response
from apps.shared.app import jwt
from apps.user.models import User, Role
from apps.shared.models import db
from apps.auth.forms import ExtendedRegistrationForm

user_datastore = SQLAlchemyUserDatastore(db, User, Role)

security = Security(datastore=user_datastore, register_form=ExtendedRegistrationForm)



@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data['sub']
    return User.query.filter_by(email=identity).one_or_none()

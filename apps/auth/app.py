from apps.api.errors import error_response
from apps.shared.app import login_manager, basic_auth, jwt
from apps.user.models import User


@login_manager.user_loader
def load_user(user_id: str):
    return User.query.get(int(user_id))


@basic_auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user


@basic_auth.error_handler
def basic_auth_error(status):
    return error_response(status)


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data['sub']
    return User.query.filter_by(email=identity).one_or_none()


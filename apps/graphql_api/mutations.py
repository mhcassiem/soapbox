from ariadne import MutationType
from flask_security import http_auth_required, current_user, verify_password

from apps.auth.app import user_datastore

mutation = MutationType()


@mutation.field("login")
@http_auth_required
def resolve_login(_, info, username, password):
    access_token, refresh_token = current_user.get_user_tokens()
    return {'access_token': access_token, 'refresh_token': refresh_token}

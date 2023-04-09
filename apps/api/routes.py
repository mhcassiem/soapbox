from flask import Blueprint, request, jsonify, url_for

from api.errors import bad_request
from apps.user.models import User
from apps.shared.models import db
from apps.shared.app import basic_auth, token_auth

api = Blueprint('api', __name__)


@api.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id: int):
    return jsonify(User.query.get_or_404(user_id).to_dict())


@api.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    if 'username' not in data or 'email' not in data or 'password' not in data:
        return bad_request('must include username, email and password fields')
    if User.query.filter_by(username=data['username']).first():
        return bad_request('please use a different username')
    if User.query.filter_by(email=data['email']).first():
        return bad_request('please use a different email address')
    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_user', id=user.id)
    return response


@api.route('/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    token = basic_auth.current_user().get_token()
    db.session.commit()
    return jsonify({'token': token})


@api.route('/tokens', methods=['DELETE'])
@token_auth.login_required
def revoke_token():
    token_auth.current_user().revoke_token()
    db.session.commit()
    response = jsonify({'message': 'Token revoked'})
    response.status_code = 204
    return response

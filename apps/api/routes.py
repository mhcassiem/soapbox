from flask import Blueprint, request, jsonify, url_for
from flask_jwt_extended import jwt_required, current_user

from apps.api.errors import bad_request
from apps.user.models import User
from apps.shared.models import db
from apps.shared.app import basic_auth

api = Blueprint('api', __name__)


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


@api.route('/login', methods=['POST'])
@basic_auth.login_required
def login():
    access_token, refresh_token = basic_auth.current_user().get_user_tokens()
    return jsonify(access_token=access_token, refresh_token=refresh_token)


@api.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    access_token = current_user.refresh_access_token()
    return jsonify(access_token=access_token)


@api.route('/logout', methods=['DELETE'])
@jwt_required()
def revoke_token():
    current_user.revoke_access_token()
    db.session.commit()
    response = jsonify({'message': 'Logged Out'})
    response.status_code = 204
    return response


@api.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id: int):
    return jsonify(User.query.get_or_404(user_id).to_dict())

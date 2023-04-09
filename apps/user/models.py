import enum
from datetime import datetime, timedelta

from flask_jwt_extended import create_access_token, create_refresh_token
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from apps.shared.models import db
from consts import JWT_ACCESS_TOKEN_EXPIRES


class MemberType(enum.Enum):
    user = 'user'
    author = 'author'


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, index=True, unique=True)
    username = db.Column(db.String, nullable=False, index=True, unique=True)
    password = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=True)
    last_name = db.Column(db.String, nullable=True)
    is_staff = db.Column(db.Boolean, default=False)
    is_superuser = db.Column(db.Boolean, default=False)
    member_type = db.Column(db.Enum(MemberType), default='user')
    updated_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    token = db.Column(db.String(32), index=True, unique=True)
    refresh_token = db.Column(db.String, unique=True)
    token_expiration = db.Column(db.DateTime)

    def __repr__(self):
        return f"User {self.email}"

    def to_dict(self):
        return dict(id=self.id, email=self.email)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

# todo set token expiration from env
    def get_token(self):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = create_access_token(identity=self.email, fresh=True)
        self.refresh_token = create_refresh_token(identity=self.email)
        self.token_expiration = now + JWT_ACCESS_TOKEN_EXPIRES
        db.session.add(self)
        return self.token, self.refresh_token

    def refresh_access_token(self):
        now = datetime.utcnow()
        self.token = create_access_token(identity=self.email, fresh=False)
        self.token_expiration = now + JWT_ACCESS_TOKEN_EXPIRES
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user

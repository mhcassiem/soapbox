from datetime import datetime, timedelta

from flask_jwt_extended import create_access_token, create_refresh_token
from flask_security.models.fsqla import FsUserMixin, FsRoleMixin, FsModels

from apps.shared.models import db
from apps.consts import JWT_ACCESS_TOKEN_EXPIRES
from apps.utils.helpers import parse_time

FsModels.set_db_info(db, user_table_name="users", role_table_name="roles")


class Role(db.Model, FsRoleMixin):
    __tablename__ = "roles"


class User(db.Model, FsUserMixin):
    __tablename__ = 'users'
    first_name = db.Column(db.String, nullable=True)
    last_name = db.Column(db.String, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    token = db.Column(db.String(32), index=True, unique=True)
    refresh_token = db.Column(db.String, unique=True)
    token_expiration = db.Column(db.DateTime)

    def __repr__(self):
        return f"User {self.email}"

    def to_dict(self):
        return dict(id=self.id, email=self.email)

    def get_user_tokens(self):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = create_access_token(identity=self.email, fresh=True)
        self.refresh_token = create_refresh_token(identity=self.email)
        self.token_expiration = now + parse_time(JWT_ACCESS_TOKEN_EXPIRES)
        db.session.add(self)
        return self.token, self.refresh_token

    def refresh_access_token(self):
        now = datetime.utcnow()
        self.token = create_access_token(identity=self.email, fresh=False)
        self.token_expiration = now + parse_time(JWT_ACCESS_TOKEN_EXPIRES)
        db.session.add(self)
        return self.token

    def revoke_access_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user

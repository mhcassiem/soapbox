from flask_security import RegisterForm
from wtforms import BooleanField


class ExtendedRegistrationForm(RegisterForm):
    remember_me = BooleanField('Remember Me')

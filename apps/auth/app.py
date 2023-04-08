from apps.shared.app import login_manager
from apps.user.models import User


@login_manager.user_loader
def load_user(user_id: str):
    return User.query.get(int(user_id))




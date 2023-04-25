from ariadne import QueryType
from flask_jwt_extended import jwt_required, get_jwt_identity


query = QueryType()


@query.field("hello")
@jwt_required()
def resolve_hello(_, info, name):
    user_id = get_jwt_identity()
    return f'Hello, {name}! User ID: {user_id}'

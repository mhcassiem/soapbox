from ariadne import make_executable_schema, graphql_sync, gql, load_schema_from_path
from ariadne.explorer import ExplorerGraphiQL
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from apps.configs import Config
from apps.graphql_api.mutations import mutation
from apps.graphql_api.queries import query

graphql = Blueprint('graphql_api', __name__)
type_defs = gql(load_schema_from_path('schema.graphql'))
schema = make_executable_schema(type_defs, query, mutation)
explorer_html = ExplorerGraphiQL().html(None)


@graphql.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=Config.DEBUG
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code


@graphql.route("/graphql", methods=["GET"])
def graphql_playground():
    return explorer_html, 200

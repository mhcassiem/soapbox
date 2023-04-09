from flask import render_template, Blueprint, request

from apps.api.errors import error_response as api_error_response

from apps.shared.models import db

error_handlers = Blueprint('error_handlers', __name__)


def wants_json_response():
    return request.accept_mimetypes['application/json'] >= \
        request.accept_mimetypes['text/html']


@error_handlers.app_errorhandler(404)
def not_found_error(error):
    if wants_json_response():
        return api_error_response(404)
    return render_template('error_handlers/404.html'), 404


@error_handlers.app_errorhandler(405)
def not_found_error(error):
    if wants_json_response():
        return api_error_response(405)
    return render_template('error_handlers/405.html'), 405


@error_handlers.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    if wants_json_response():
        return api_error_response(500)
    return render_template('error_handlers/500.html'), 500

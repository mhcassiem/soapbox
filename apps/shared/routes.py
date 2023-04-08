from flask import Blueprint, render_template

shared = Blueprint('shared', __name__)


@shared.route('/')
@shared.route('/index')
def index():
    return render_template('index.html', title='Soapbox')

from flask import Blueprint

articles = Blueprint('articles', __name__)


@articles.get("/articles/<string:title>")
def display_article(title: str):
    return f"hello {title}"

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_app(app: Flask):

    db.init_app(app)

    app.db = db

    from app import models
    from app.models.user_model import UserModel
    from app.models.book import Book

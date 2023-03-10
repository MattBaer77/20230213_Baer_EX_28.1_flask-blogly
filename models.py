"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)

    first_name = db.Column(db.String(20),
                    nullable=True,
                    unique=False)

    last_name = db.Column(db.String(20),
                    nullable=False,
                    unique=True)
    
    img_url = db.Column(db.String(),
                    nullable=True,
                    unique=False)
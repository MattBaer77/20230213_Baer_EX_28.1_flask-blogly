"""Blogly application."""
import os
from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


connect_db(app)
# db.create_all()

@app.route('/')
def root():
    """Shows a list of all users"""

    return redirect('/users')

@app.route('/users')
def users():
    """Shows a list of all users"""

    users = User.query.all()

    return render_template('users.html', users=users)

@app.route('/add-user')
def add_user_form():
    """Shows a form to add a user"""

    return render_template('add-user.html')

@app.route('/add-user', methods=["POST"])
def add_user_post():
    """"Accepts form input, Adds a user to the database"""

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    img_url = request.form["img_url"]

    new_user = User(first_name=first_name, last_name=last_name, img_url=img_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')
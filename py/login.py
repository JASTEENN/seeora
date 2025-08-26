from flask import Blueprint, jsonify, request
from app import app
from models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

login = Blueprint('login', __name__)

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

@login.route('/login', methods=['POST'])
def login():
    """Login a user"""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            return jsonify({"token": user.generate_token()})
    return jsonify({"error": "Invalid credentials"}), 401
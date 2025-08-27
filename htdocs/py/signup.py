from flask import Blueprint, jsonify, request
from app import app
from models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

signup = Blueprint('signup', __name__)

class SignupForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

@signup.route('/signup', methods=['POST'])
def signup():
    """Signup a user"""
    form = SignupForm()

from flask import Blueprint, jsonify
from app import app
from models import User

routes = Blueprint('routes', __name__)

@routes.route('/users', methods=['GET'])
def get_users():
    """Return a list of users"""
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@routes.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Return a user by ID"""
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict())
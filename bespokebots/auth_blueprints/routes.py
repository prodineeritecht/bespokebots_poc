from flask import Blueprint, request, session, jsonify, redirect, url_for
from bespokebots.models.user import User
import logging

logging.basicConfig(level=logging.INFO)
# Initialize the logger
logger = logging.getLogger(__name__)

# create a Blueprint
auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/')
def home():
    user_id = session.get('user_id')
    if user_id:
        return "Welcome to Bespoke Bots!"
    else:
        return redirect(url_for('auth_bp.login'))  # redirect to the login route

@auth_bp.route('/login', methods=['POST'])
def login():
    
    if request.method == 'POST':
        username = request.json.get('username')
        logger.info("Login request received for username: %s",username)

        # For the sake of simplicity, we assume that usernames are unique.
        # In a real-world scenario, uniqueness would be verified.

        # If user exists, login, else create a new user and login
        user = User.lookup_by_user_name(user_name=username)

        if not user:
            user = User(user_name=username)
            user._save()
            # db.session.add(user)
            # db.session.commit()

        # save user id in session
        session['user_id'] = user.user_id

        return jsonify({"message": "Logged in", "user_id": user.user_id}), 200
    else:
        return "Please log in."

@auth_bp.route('/logout/<user_id>', methods=['GET'])
def logout(user_id):
    logger.info("Logout request received for user_id: %s",user_id)
    user_id = session.get('user_id')
    if user_id:
        # clear the user id from session
        session.pop('user_id')
        return jsonify({"message": "Logged out"}), 200
    else:
        return jsonify({"error": "No active session"}), 400

@auth_bp.route('/delete/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    logger.info("Delete user request received for user_id: %s",user_id)
    user = User.query.get(user_id)

    if user:
        # db.session.delete(user)
        # db.session.commit()
        return jsonify({"message": "User deleted"}), 200
    else:
        return jsonify({"error": "User not found"}), 404

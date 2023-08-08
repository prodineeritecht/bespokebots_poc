from flask import Blueprint, request, session, jsonify, redirect, url_for
import logging
from bespokebots.dao.database import db

logging.basicConfig(level=logging.INFO)
# Initialize the logger
logger = logging.getLogger(__name__)

# create a Blueprint
auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/')
def home():
    user_id = session.get('user_id')
    if user_id:
        return "Welcome to Bespoke Bots, user: {user_id}"
    else:
        return redirect(url_for('auth_bp.login'))  # redirect to the login route

@auth_bp.route('/login', methods=['POST'])
def login():
    from bespokebots.services.user_service import UserService
    user_service = UserService(db.session)
    if request.method == 'POST':
        username = request.json.get('username')
        logger.info("Login request received for username: %s",username)

        # For the sake of simplicity, we assume that usernames are unique.
        # In a real-world scenario, uniqueness would be verified.

        # If user exists, login, else create a new user and login
        user = UserService.lookup_by_user_name(user_name=username)

        if not user:
            user = user_service.create_user(username=username) #TODO: allow a timezone other than America/New_York to be passed in via the request
            logger.info("Created new user with id: %s",user.id)
        # save user id in session
        logger.info("Adding user with id: %s to the session",user.id)
        session['user_id'] = user.id

        return jsonify({"message": "Logged in", "user_id": user.id}), 200
    else:
        return "Please log in."

@auth_bp.route('/logout/<user_id>', methods=['GET'])
def logout(user_id):
    logger.info("Logout request received for user_id: %s",user_id)
    
    if user_id:
        # clear the user id from session
        session.pop('user_id') if session.get('user_id') else None
        return jsonify({"message": "Logged out"}), 200
    else:
        return jsonify({"error": "No active session"}), 400

@auth_bp.route('/delete/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    from bespokebots.services.user_service import UserService
    logger.info("Delete user request received for user_id: %s",user_id)
    user_service = UserService(db.session)
    user = UserService.lookup_by_user_id(user_id=user_id)
    if user:
        user_service.delete_user(user)
        return jsonify({"message": "User with id {user.id} deleted"}), 200
    else:
        return jsonify({"error": "User with id {user_id} not found"}), 404

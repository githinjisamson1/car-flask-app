# Import necessary modules and classes
from flask import request, jsonify
from app import db
from app.models.user_model import User
from sqlalchemy.exc import SQLAlchemyError
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Function to handle errors and return a JSON response


def handle_error(e, status_code):
    logging.error(str(e))
    return jsonify({'error': str(e)}), status_code

# Route for creating a new user

# POST


def create_user():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Check for required fields in the data
        if 'username' not in data or 'email' not in data or 'usertype' not in data:
            return handle_error('Missing data fields (username, email, usertype required)', 400)

        # Create a new User instance
        new_user = User(
            username=data['username'], email=data['email'], usertype=data['usertype'])

        # Add the new user to the database session and commit the changes
        db.session.add(new_user)
        db.session.commit()

        # Log and return a JSON response with the serialized new user data
        # new_user.serialize() seems similar to new_user.to_dict()
        logging.info(jsonify(new_user.serialize()))

        return jsonify(new_user.serialize()), 201

    except SQLAlchemyError as e:
        # Handle database-related errors and return an error response
        return handle_error(e, 500)

# Route for getting all users

# GET


def get_users():
    try:
        # Query all users from the database
        users = User.query.all()

        # Return a JSON response with the serialized data of all users
        return jsonify([user.serialize() for user in users]), 200

    except SQLAlchemyError as e:
        # Handle database-related errors and return an error response
        return handle_error(e, 500)

# Placeholder routes for getting, updating, and deleting a specific user


def get_user(user_id):
    try:
        user = User.query.filter_by(id=user_id).first()

        return jsonify(user.serialize()), 200

    except SQLAlchemyError as e:
        return handle_error(e, 400)


def update_user(user_id):
    try:
        updated_data = request.get_json()

        user = User.query.filter_by(id=user_id).first()

        for attr in updated_data:
            setattr(user, attr, updated_data.get(attr))

        # db.session.add()
        db.session.commit()

        return jsonify(user.serialize()), 200

    except SQLAlchemyError as e:
        return handle_error(e, 400)


def delete_user(user_id):
    try:
        user = User.query.filter_by(id=user_id).first()

        db.session.delete(user)
        db.session.commit()

        response_body = {
            "success": True,
            "message": "User deleted"
        }

        return jsonify(response_body), 200

    except SQLAlchemyError as e:
        return handle_error(e, 400)

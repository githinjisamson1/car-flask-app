from flask import request, jsonify
from app import db
from app.models.car_model import Car
from sqlalchemy.exc import SQLAlchemyError
import logging

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO)


def handle_error(e, status_code):
    """
    Centralized error handling function.

    Args:
    - e: Exception object
    - status_code: HTTP status code

    Returns:
    - JSON response containing the error message and the provided status code
    """
    error_message = str(e) if not hasattr(e, 'message') else e.message
    logging.error(f"Error: {error_message}")
    return jsonify({'error': error_message}), status_code


def create_car():
    """
    Endpoint for creating a new car entry.

    Returns:
    - JSON response with the serialized new car entry and HTTP status code
    """
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Check for required fields in the data
        if 'make' not in data or 'model' not in data or 'year' not in data or 'user_id' not in data:
            return handle_error('Missing data fields', 400)

        # Create a new Car instance
        new_car = Car(make=data['make'], model=data['model'],
                      year=data['year'], user_id=data['user_id'])

        # Add the new car to the database session and commit changes
        db.session.add(new_car)
        db.session.commit()

        # Log and return the serialized new car entry
        logging.info(jsonify(new_car.serialize()))
        return jsonify(new_car.serialize()), 201

    except SQLAlchemyError as e:
        # Handle database-related errors
        return handle_error(e, 500)


def get_cars():
    """
    Endpoint for retrieving all cars.

    Returns:
    - JSON response with the serialized list of cars and HTTP status code
    """
    try:
        # Query all cars from the database
        cars = Car.query.all()

        # Return the serialized list of cars
        return jsonify([car.serialize() for car in cars]), 200

    except SQLAlchemyError as e:
        # Handle database-related errors
        return handle_error(e, 500)


def get_car(car_id):
    try:
        car = Car.query.filter_by(id=car_id).first()

        return jsonify(car.serialize()), 200

    except SQLAlchemyError as e:
        return handle_error(e, 400)


def delete_car(car_id):
    try:
        car = Car.query.filter_by(id=car_id).first()

        db.session.delete(car)
        db.session.commit()

        response_body = {
            "success": True,
            "message": "Car deleted"
        }

        return jsonify(response_body), 200

    except SQLAlchemyError as e:
        return handle_error(e, 400)
    

def update_car(car_id):
    try:
        updated_data = request.get_json()

        car = Car.query.filter_by(id=car_id).first()

        for attr in updated_data:
            setattr(car, attr, updated_data.get(attr))

        # db.session.add()
        db.session.commit()

        return jsonify(car.serialize()), 200

    except SQLAlchemyError as e:
        return handle_error(e, 400)

# Import the 'db' instance from the 'app' module
from app import db

# Define the User model class that inherits from db.Model


class User(db.Model):
    # Define columns for the User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    usertype = db.Column(db.String(20))

    # Define a relationship with the 'Car' model using the backref 'owner'
    # the backref parameter creates a virtual column ('owner') on the 'Car' model, allowing you to access the associated user from a car instance.
    cars = db.relationship('Car', backref='owner', lazy=True)

    # Define a method to serialize the User model data
    # This method is useful for converting User instances into a format suitable for JSON serialization.
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'usertype': self.usertype
        }

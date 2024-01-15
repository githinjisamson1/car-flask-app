# Import the 'db' instance from the 'app' module
from app import db

# Define the Car model class that inherits from db.Model


class Car(db.Model):
    # Define columns for the Car model
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(100))
    model = db.Column(db.String(100))
    year = db.Column(db.Integer)

    # Define a foreign key relationship with the 'User' model
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Define a relationship with the 'User' model
    user = db.relationship('User')

    sale = db.relationship("Sale", back_populates="car")

    # Define a method to serialize the Car model data/to_dict()
    def serialize(self):
        return {
            'id': self.id,
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'user_details': self.user.serialize() if self.user else None,
            "sale_details": self.sale.serialize() if self.sale else None
        }


'''
This serialize method is useful when you want to convert your SQLAlchemy model instances into a format that can be easily converted to JSON. It provides a structured and consistent way to represent the data. If the associated user has a serialize method, it ensures that user details are included in the serialized output. If not, it sets user details to None.
'''

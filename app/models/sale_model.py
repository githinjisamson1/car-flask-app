from app import db


class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    payment_method = db.Column(db.String)
    amount = db.Column(db.Integer)
    status = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    car = db.relationship("Car", back_populates="sale")

    def serialize(self):
        return {
            "payment_method": self.payment_method,
            "amount": self.amount,
            "status": self.status,
            "created_at": self.created_at,
            "car_details": self.car.serialize() if self.car else None
        }

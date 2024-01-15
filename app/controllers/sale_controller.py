from flask import request, jsonify, make_response
from app import db
from app.models.sale_model import Sale
from sqlalchemy.exc import SQLAlchemyError
import logging


logging.basicConfig(level=logging.INFO)


def handle_error(e, status_code):
    logging.error(str(e))
    return jsonify({'error': str(e)}), status_code

# retrieve all
def get_sales():
    try:
        sales_lc = [sale.serialize() for sale in Sale.query.all()]
        response = make_response(jsonify(sales_lc), 200)
        response.headers["Content-Type"] = "application/json"
        return response

    except SQLAlchemyError as e:
        return handle_error(e, 500)

# retrieve 1
def get_sale(sale_id):
    try:
        sale = Sale.query.filter_by(id=sale_id).first()
        sale_dict = sale.serialize()
        response = make_response(jsonify(sale_dict), 200)
        response.headers["Content-Type"] = "application/json"
        return response

    except SQLAlchemyError as e:
        return handle_error(e, 400)

# create sale
def post_sale():
    try:
        data = request.get_json()
        new_sale = Sale(
            payment_method=data.get("payment_method"),
            amount=data.get("amount"),
            status=data.get("status")
        )

        db.session.add(new_sale)
        db.session.comit()

        new_sale_dict = new_sale.serialize()
        response = make_response(jsonify(new_sale_dict), 201)
        response.headers["Content-Type"] = "application/json"
        return response

    except SQLAlchemyError as e:
        return handle_error(e, 500)

# update sale
def patch_sale(sale_id):
    try:
        updated_data = request.get_json()

        sale = Sale.query.filter_by(id=sale_id).first()

        for attr in updated_data:
            setattr(sale, attr, updated_data.get(attr))

        # db.session.add()
        db.session.commit()

        sale_dict = sale.serialize()
        response = make_response(jsonify(sale_dict), 200)
        response.headers["Content-Type"] = "application/json"
        return response

    except SQLAlchemyError as e:
        return handle_error(e, 400)

# delete sale
def delete_sale(sale_id):
    try:
        sale = Sale.query.filter_by(id=sale_id).first()

        db.session.delete(sale)
        db.session.commit()

        response_body = {
            "success": True,
            "message": "Sale deleted"
        }

        response = make_response(jsonify(response_body), 204)
        response.headers["Content-Type"] = "application/json"
        return response

    except SQLAlchemyError as e:
        return handle_error(e, 400)

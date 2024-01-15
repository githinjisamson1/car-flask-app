from flask import Blueprint
from app.controllers.user_controller import create_user, get_users, get_user, update_user, delete_user
from app.controllers.car_controller import create_car,  get_cars, get_car, update_car, delete_car
from app.controllers.sale_controller import get_sales, get_sale, post_sale, patch_sale, delete_sale

bp = Blueprint('bp', __name__)

# index route


@bp.route('/', methods=['GET'])
def home():
    return "Car_User API"

# !USER CONTROLLERS

# route for handling users


@bp.route('/users', methods=['GET'])
def read_users():
    return get_users()


# get individual user
@bp.route('/users/<int:user_id>', methods=['GET'])
def read_user(user_id):
    return get_user(user_id)

# post individual user


@bp.route('/users', methods=['POST'])
def post_user():
    return create_user()

# update individual user


@bp.route('/users/<int:user_id>', methods=['PATCH'])
def patch_user(user_id):
    return update_user(user_id)

# delete individual user


@bp.route('/users/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    return delete_user(user_id)

# !CAR CONTROLLERS


@bp.route('/cars', methods=['POST'])
def add_car():
    return create_car()


@bp.route('/cars', methods=['GET'])
def list_cars():
    return get_cars()


@bp.route('/cars/<int:car_id>', methods=['GET'])
def list_car(car_id):
    return get_car(car_id)


@bp.route('/cars/<int:car_id>', methods=['PATCH'])
def patch_car(car_id):
    return update_car(car_id)


@bp.route('/cars/<int:car_id>', methods=['DELETE'])
def remove_car(car_id):
    return delete_car(car_id)


# !SALE CONTROLLERS

@bp.route('/sales', methods=['GET'])
def read_sales():
    return get_sales()


@bp.route('/sales/<int:sale_id>', methods=['GET'])
def read_sale(sale_id):
    return get_sale(sale_id)


@bp.route('/sales', methods=['POST'])
def create_sale():
    return post_sale()


@bp.route('/sales/<int:sale_id>', methods=['PATCH'])
def update_sale(sale_id):
    return patch_sale(sale_id)


@bp.route('/sales/<int:sale_id>', methods=['DELETE'])
def remove_sale(sale_id):
    return delete_sale(sale_id)

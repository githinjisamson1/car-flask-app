from flask import Blueprint
from app.controllers.user_controller import create_user, get_users, get_user, update_user, delete_user
from app.controllers.car_controller import create_car,  get_cars, get_car, update_car, delete_car

bp = Blueprint('bp', __name__)


@bp.route('/', methods=['GET'])
def home():
    return "Car_User API"


@bp.route('/users', methods=['GET'])
def read_users():
    return get_users()

# !USER CONTROLLERS


@bp.route('/users/<int:user_id>', methods=['GET'])
def read_user(user_id):
    return get_user(user_id)


@bp.route('/users', methods=['POST'])
def post_user():
    return create_user()


@bp.route('/users/<int:user_id>', methods=['PATCH'])
def patch_user(user_id):
    return update_user(user_id)


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

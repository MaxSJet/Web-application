from flask import Blueprint, request, jsonify
from flask_cors import CORS, cross_origin
from app import db
from .models import Order
from ..dishes.models import Dish

mod = Blueprint('orders', __name__, url_prefix='/orders')
CORS(mod)


@mod.route('/', methods=['GET'])
@cross_origin()
def get_all():
    orders = Order.query.all()

    return jsonify(orders)


@mod.route('/<int:dish_id>', methods=['GET'])
@cross_origin()
def get_by_id(dish_id):
    order = Order.query.filter_by(id=dish_id).first_or_404()
    return jsonify(order)


@mod.route('/', methods=['POST'])
@cross_origin()
def create():
    dishes = []
    total_cost = 0

    for i in request.json['dishes']:
        dish = Dish.query.filter_by(id=i).first_or_404()
        dishes.append(dish)
        total_cost += dish.cost

    order = Order(
        dishes=dishes,
        status=0,
        total=total_cost
    )

    db.session.add(order)
    db.session.commit()

    return '', 204


@mod.route('/<int:dish_id>', methods=['PATCH'])
@cross_origin()
def update(dish_id):
    order = Order.query.filter_by(id=dish_id).first_or_404()

    order.dishes = request.json['dishes']
    order.status = request.json['status']

    db.session.add(order)
    db.session.commit()

    return '', 204


@mod.route('/status/<int:dish_id>', methods=['PATCH'])
@cross_origin()
def set_status(dish_id):
    order = Order.query.filter_by(id=dish_id).first_or_404()

    order.status = request.json['status']

    db.session.add(order)
    db.session.commit()

    return '', 204



@mod.route('/<int:dish_id>', methods=['DELETE'])
@cross_origin()
def delete(dish_id):
    order = Order.query.filter_by(id=dish_id).first_or_404()

    db.session.delete(order)
    db.session.commit()
    return '', 204

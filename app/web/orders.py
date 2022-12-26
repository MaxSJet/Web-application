from flask import Blueprint, request, jsonify
from flask_cors import CORS, cross_origin
from app import db
from ..models.base import Order, Dish
from datetime import datetime

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
    date =datetime.now()
    date = date.strftime("%d %B, %Y %H:%M")
    
    total_cost = 0
    userId = request.json['userId']
    dishCount = ''
    

    for i in request.json['dishes']:
        dish = Dish.query.filter_by(id=i['dish_id']).first_or_404()
        dishCountSingle = dish.name + ' ' + 'x'+str(i['amount'])+'\n'
        dishCount +=  dishCountSingle 
        dishes.append(dish)
        total_cost += dish.cost * float(i['amount'])
        


    
    order = Order(
        dishes=dishes,
        status=0,
        total=total_cost,
        userId = userId,
        dishCount= dishCount,
        date = date
    )

    db.session.add(order)
    db.session.commit()

    return '', 204



@mod.route('/<int:dish_id>', methods=['PATCH'])
@cross_origin()
def update(dish_id):
    order = Order.query.filter_by(id=dish_id).first_or_404()

    order.dishes = request.json['dishes']
    #order.status = request.json['status']

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

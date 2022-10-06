from flask import Blueprint, request, jsonify
from app import db
from flask_cors import CORS, cross_origin
import datetime
from .models import Menu
from ..dishes.models import Dish

mod = Blueprint('menus', __name__, url_prefix='/menus')
CORS(mod)


@mod.route('/', methods=['GET'])
@cross_origin()
def get_all():
    from_date = datetime.datetime(1, 1, 1).fromisoformat(request.json['from'])
    to_date = datetime.datetime(1, 1, 1).fromisoformat(request.json['to'])
    cnt = (to_date - from_date).days
    generate_menu(cnt)

    date_list = [(from_date + datetime.timedelta(days=x)).strftime('%Y-%m-%d') for x in range(cnt + 1)]

    orders = []

    for i in date_list:
        order = Menu.query\
            .filter_by(date=i).first()
        orders.append(order)

    return jsonify(orders)


@mod.route('/<int:menu_id>', methods=['GET'])
@cross_origin()
def get_by_id(menu_id):
    order = Menu.query.filter_by(id=menu_id).first_or_404()
    return jsonify(order)


@mod.route('/', methods=['POST'])
@cross_origin()
def create():
    dishes = []

    for i in request.json['dishes']:
        dish = Dish.query.filter_by(id=i).first_or_404()
        dishes.append(dish)

    order = Menu(
        dishes=dishes,
        date=datetime.date.fromisoformat(request.json['date']),
    )

    db.session.add(order)
    db.session.commit()

    return '', 204


@mod.route('/<int:menu_id>', methods=['PATCH'])
@cross_origin()
def update(menu_id):
    order = Menu.query.filter_by(id=menu_id).first_or_404()

    dishes = []

    for i in request.json['dishes']:
        dish = Dish.query.filter_by(id=i).first_or_404()
        dishes.append(dish)

    order.dishes = dishes

    db.session.add(order)
    db.session.commit()

    return '', 204


@mod.route('/<int:menu_id>', methods=['DELETE'])
@cross_origin()
def delete(menu_id):
    order = Menu.query.filter_by(id=menu_id).first_or_404()

    db.session.delete(order)
    db.session.commit()
    return '', 204


def generate_menu(days):
    base = datetime.datetime.today()
    date_list = [(base + datetime.timedelta(days=x)).strftime('%Y-%m-%d') for x in range(days + 1)]

    for i in date_list:
        menu = Menu.query.filter_by(date=i).first()
        dishes = []

        if not menu:
            menu = Menu(
                dishes=dishes,
                date=datetime.date.fromisoformat(i),
            )

        db.session.add(menu)
        db.session.commit()

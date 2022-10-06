from app import db
from dataclasses import dataclass
from .constants import statuses

dishes = db.Table('tags',
                  db.Column('dish_id', db.Integer, db.ForeignKey('dishes.id'), primary_key=True),
                  db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), primary_key=True)
                  )


@dataclass
class Order(db.Model):
    id: int
    dishes: type([])
    total: int
    status: int

    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    dishes = db.relationship('Dish', secondary=dishes, lazy='subquery',
        backref=db.backref('orders', lazy=True))
    status = db.Column(db.Integer, default=statuses["NEW"])
    total = db.Column(db.Float)

    def __init__(self, dishes=None, status=None, total=None):
        self.dishes = dishes
        self.status = status
        self.total = total

    def __repr__(self):
        return '<Order %r>' % self.name

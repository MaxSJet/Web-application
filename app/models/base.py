from app import db
from dataclasses import dataclass
from .constants import statuses


@dataclass
class Users(db.Model):
    """Пользователи."""
    
    __tablename__ = "users"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    login = db.Column(db.String, nullable=False)
    role = db.Column(db.Integer, nullable=False, default=0)
    lastname = db.Column(db.String, nullable=True)
    firstname = db.Column(db.String, nullable=True)
    middlename = db.Column(db.String, nullable=True)

    # def __init__(self, login:str=None , role:int=0, lastname:str=None, firstname:str=None, middlename:str=None):
    #     self.login = login
    #     self.role = role
    #     self.lastname = lastname
    #     self.middlename = middlename
    #     self.firstname = firstname

@dataclass
class Dish(db.Model):
    id: int
    name: str
    image_url: str
    weight: float
    cost: float
    compound: str

    __tablename__ = 'dishes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    image_url = db.Column(db.String(255))
    weight = db.Column(db.Float)
    cost = db.Column(db.Float)
    compound = db.Column(db.String(255))

    def __init__(self, name=None, image_url=None, weight=None, cost=None, compound=None):
        self.name = name
        self.image_url = image_url
        self.weight = weight
        self.cost = cost
        self.compound = compound

    def __repr__(self):
        return '<Dish %r>' % self.name

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

dishes = db.Table('menu_dishes',
                  db.Column('dish_id', db.Integer, db.ForeignKey('dishes.id'), primary_key=True),
                  db.Column('menu_id', db.Integer, db.ForeignKey('menus.id'), primary_key=True)
                  )


@dataclass
class Menu(db.Model):
    id: int
    dishes: [Dish]
    date: db.Date

    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key=True)
    dishes = db.relationship('Dish', secondary=dishes, lazy='subquery',
        backref=db.backref('menus', lazy=True))
    date = db.Column(db.Date)

    def __init__(self, dishes=None, date=None):
        self.dishes = dishes
        self.date = date

    def __repr__(self):
        return '<Menu>'
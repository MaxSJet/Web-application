from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object('config')

db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
    return {
        "error": "Not found"
    }, 404


from app.dishes.routes import mod as dishesModel
from app.orders.routes import mod as ordersModel
from app.menus.routes import mod as menusModel
from app.time.routes import mod as timeModel

app.register_blueprint(dishesModel)
app.register_blueprint(ordersModel)
app.register_blueprint(menusModel)
app.register_blueprint(timeModel)

db.create_all()

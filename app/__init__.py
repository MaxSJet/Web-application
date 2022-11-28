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


from app.web import dishesModel, ordersModel, menusModel, timeModel

#TODO: Первичная генерация данных пользователей
# with app.app_context():
#     db.create_all()
#     from .models.base import Users
#     db.session.add_all([ Users(login='admin', role=9 ,lastname='Админив', firstname='Админ' ,middlename='Админыч'),
#                         Users(login='ivan', role=1 ,lastname='Иванов', firstname='Иван' ,middlename='Иванович'),
#                         Users(login='artem', role=1 ,lastname='Артемов', firstname='Артем' ,middlename='Артемович'),
#                         Users(login='masha', role=0 ,lastname='Машина', firstname='Мамия' ,middlename='Васильевна'),
#                         Users(login='lena', role=0 ,lastname='Ленина', firstname='Елена' ,middlename='Петровна')])
#     db.session.commit()

app.register_blueprint(dishesModel)
app.register_blueprint(ordersModel)
app.register_blueprint(menusModel)
app.register_blueprint(timeModel)


from flask import Blueprint, current_app,jsonify
from app import db
import datetime
from flask_cors import CORS, cross_origin
#from ..models.common import CurrentUser
from ..models.base import Users

mod = Blueprint('time', __name__, url_prefix='/times')
CORS(mod)


@mod.route('/week', methods=['GET'])
@cross_origin()
def get_week():
    base = datetime.datetime.today()
    date_list = [(base + datetime.timedelta(days=x)).strftime('%Y-%m-%d') for x in range(7)]

    return date_list

@mod.route('/current_user', methods=['GET'])
@cross_origin()
def current_user():
    users = Users.query.all()
    return jsonify(users)



    ##TODO: заглушка до публикации
    #login = current_app.config.get('CURRENT_USER')
    ## login = request.environ['REMOTE_USER'].split('@')[0]
    #
    #cur_user = CurrentUser(login)
    #return cur_user.json()

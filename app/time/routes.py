from flask import Blueprint
import datetime
from flask_cors import CORS, cross_origin

mod = Blueprint('time', __name__, url_prefix='/times')
CORS(mod)


@mod.route('/week', methods=['GET'])
@cross_origin()
def get_week():
    base = datetime.datetime.today()
    date_list = [(base + datetime.timedelta(days=x)).strftime('%Y-%m-%d') for x in range(7)]

    return date_list

import json
import traceback

from flask import make_response, Flask
from pymysql import connect
from flask_restful import Resource, reqparse, Api

import config


app = Flask(__name__)
api = Api(app)


# 跨域请求
@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {'Access-Control-Allow-Origin': '*'})
    return resp


class UpSubject(Resource):
    def post(self):
        result = {"success": False}
        parser = reqparse.RequestParser()
        parser.add_argument("theme", type=int)
        parser.add_argument("content")
        parser.add_argument("choice")
        parser.add_argument("answer")
        parser.add_argument("isparty", type=int)
        parser.add_argument("type", type=int)
        args = parser.parse_args()

        connection = connect(**config.MYSQL_CONFIG)
        try:
            cursor = connection.cursor()
            sql = "INSERT INTO subject(theme, content, choice, answer, isparty, type) " \
                  "VALUES (%s, %s, %s, %s, %s, %s)"
            id = cursor.execute(sql, (args["theme"], args["content"], args["choice"],
                                          args["answer"], args["isparty"], args["type"]))
            connection.commit()
            result["success"] = bool(id)
        except:
            traceback.print_exc()
        finally:
            connection.close()
            return result


api.add_resource(UpSubject, "/upsubject")

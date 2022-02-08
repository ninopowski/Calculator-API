from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def get_posted_data(posted_data):
    return int(posted_data["x"]), int(posted_data["y"])


def check_posted_data(posted_data, operation):
    if operation == "add":
        if "x" not in posted_data or "y" not in posted_data:
            return 301
        else:
            return 200
    elif operation == "subtract":
        if "x" not in posted_data or "y" not in posted_data:
            return 301
        else:
            return 200


class Add(Resource):
    def post(self):
        # get posted data
        postedData = request.get_json()

        # validate input
        status_code = check_posted_data(postedData, "add")

        if status_code == 200:
            x, y = get_posted_data(postedData)
            sum = x+y
        else:
            sum = "missing argument"

        retMap = {
            "Message": sum,
            "status code": status_code
        }
        return jsonify(retMap)


class Subtract(Resource):
    def post(self):
        # get posted data
        postedData = request.get_json()

        # validate input
        status_code = check_posted_data(postedData, "subtract")

        if status_code == 200:
            x, y = get_posted_data(postedData)
            sub = x - y
        else:
            sub = "missing argument"

        retMap = {
            "Message": sub,
            "Status code": status_code
        }
        return jsonify(retMap)



class Divide(Resource):
    def post(self):
        pass


class Multiply(Resource):
    def post(self):
        pass


api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")

if __name__ == "__main__":
    app.run(debug=True)
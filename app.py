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
    elif operation == "divide":
        if "x" not in posted_data or "y" not in posted_data:
            return 301
        elif posted_data["y"] == 0:
            return 302
        else:
            return 200
    elif operation == "multiply":
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
            message = x+y
        else:
            message = "missing argument"

        retMap = {
            "Message": message,
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
            message = x - y
        else:
            message = "missing argument"

        retMap = {
            "Message": message,
            "Status code": status_code
        }
        return jsonify(retMap)



class Divide(Resource):
    def post(self):
        postedData = request.get_json()

        status_code = check_posted_data(postedData, "divide")

        if status_code == 200:
            x, y = get_posted_data(postedData)
            message = x/y
        else:
            if status_code == 301:
                message = "missing argument"
            elif status_code == 302:
                message = "cant divide by zero"

        retMap = {
            "Message": message,
            "Status code": status_code
        }
        return jsonify(retMap)



class Multiply(Resource):
    def post(self):
        postedData = request.get_json()

        # validate input
        status_code = check_posted_data(postedData, "multiply")

        if status_code == 200:
            x, y = get_posted_data(postedData)
            message = x * y
        else:
            message = "missing argument"

        retMap = {
            "Message": message,
            "Status code": status_code
        }
        return jsonify(retMap)


api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Divide, "/divide")
api.add_resource(Multiply, "/multiply")

if __name__ == "__main__":
    app.run(debug=True)
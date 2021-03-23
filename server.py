#!flask/bin/python
from flask import Flask, jsonify, make_response, request, abort
import random

app = Flask(__name__)

UPPER_TEMP = 32.9
LOWER_TEMP = 12.5
VALID_DOOR_QUERY = ["status", "color"]
VALID_DOOR_STATUS = ["CLOSED", "OPEN"]
VALID_POST = ["create"]


def dispatch_query(_key, _value):
    return {
        "status": _value if _value in VALID_DOOR_STATUS else "ERROR",
        "living_room": "Available resources: Temperature, Door and Light",
        "dinning_room": "Available resources: Temperature, Door and Light"
    }.get(_key, "Invalid query")


def read_temperature():
    return "{}".format(round(random.uniform(UPPER_TEMP, LOWER_TEMP), 2)))


@app.route('/living_room/temperature', methods=['GET'])
def get_temperature():
    return read_temperature()


@app.route('/living_room/door/create', methods=['POST'])
def create_resource():
    return jsonify({'result': 'created'}), 201


@app.route('/living_room/door', methods=['PUT'])
def modify_door():
    new_status = request.args.get('status').upper()
    return make_response(jsonify({'status': dispatch_query('status', new_status)})), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

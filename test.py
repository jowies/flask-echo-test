import flask
from flask import request, jsonify
import json
app = flask.Flask(__name__)
app.config["DEBUG"] = True



@app.route('/', methods=['POST'])
def create_task():
    if not request.json:
        abort(400)
    polygon = request.get_json()
    print(polygon)
    return jsonify({'path': polygon["path"]}), 201
app.run()


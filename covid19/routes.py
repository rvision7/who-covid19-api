from flask import jsonify
from covid19 import app


@app.route('/hello', methods=['GET'])
def hello():
    message = "hello world"
    return jsonify({'message': message})

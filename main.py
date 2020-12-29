from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    message = "hello world"
    return jsonify({'message': message})


if __name__ == '__main__':
    app.run()

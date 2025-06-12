from flask import Flask, request, jsonify, Blueprint

app = Flask(__name__)

number_addition_api = Blueprint('number_addition_api', __name__)

@number_addition_api.route('/number_addition', methods=['POST'])
def number_addition():
    data = request.get_json()
    try:
        numbers = list(map(float, data.get('input', '').split()))
        result = sum(numbers)
    except Exception:
        return jsonify(result="Invalid input"), 400
    return jsonify(result=str(result))

app.register_blueprint(number_addition_api)

if __name__ == '__main__':
    app.run(debug=True)
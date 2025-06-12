from flask import Blueprint, request, jsonify

string_reversal_api = Blueprint('string_reversal_api', __name__)

@string_reversal_api.route('/string_reversal', methods=['POST'])
def string_reversal():
    data = request.get_json()
    text = data.get('input', '')
    return jsonify(result=text[::-1])
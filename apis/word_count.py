from flask import Blueprint, request, jsonify

word_count_api = Blueprint('word_count_api', __name__)

@word_count_api.route('/word_count', methods=['POST'])
def word_count():
    data = request.get_json()
    text = data.get('input', '')
    count = len(text.split())
    return jsonify(result=str(count))
from flask import Blueprint, request, jsonify

palindrome_check_api = Blueprint('palindrome_check_api', __name__)

@palindrome_check_api.route('/palindrome_check', methods=['POST'])
def palindrome_check():
    data = request.get_json()
    text = data.get('input', '').replace(' ', '').lower()
    is_palindrome = text == text[::-1]
    return jsonify(result="Yes" if is_palindrome else "No")
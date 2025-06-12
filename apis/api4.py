from flask import Blueprint, request, jsonify

temperature_conversion_api = Blueprint('temperature_conversion_api', __name__)

@temperature_conversion_api.route('/temperature_conversion', methods=['POST'])
def temperature_conversion():
    data = request.get_json()
    try:
        value, unit = data.get('input', '').split()
        value = float(value)
        if unit.lower() == 'c':
            result = f"{(value * 9/5) + 32} F"
        elif unit.lower() == 'f':
            result = f"{(value - 32) * 5/9} C"
        else:
            return jsonify(result="Invalid unit"), 400
    except Exception:
        return jsonify(result="Invalid input"), 400
    return jsonify(result=result)
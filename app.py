from flask import Flask, request, jsonify
from flask_cors import CORS
from apis.word_count import word_count_api
from apis.number_addition import number_addition_api
from apis.api3 import string_reversal_api
from apis.api4 import temperature_conversion_api
from apis.api5 import palindrome_check_api

app = Flask(__name__)
CORS(app)

# Registering the APIs
app.register_blueprint(word_count_api)
app.register_blueprint(number_addition_api)
app.register_blueprint(string_reversal_api)
app.register_blueprint(temperature_conversion_api)
app.register_blueprint(palindrome_check_api)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

if __name__ == '__main__':
    app.run(debug=True)
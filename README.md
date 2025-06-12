# Flask API Documentation

This README file provides information about the Flask API for the fullstack application. It includes instructions on how to set up and run the Flask server, as well as details about the available APIs.

## Project Structure

```
flask-api/
├── app.py                # Main entry point for the Flask application
├── requirements.txt      # List of dependencies for the Flask application
└── apis/                 # Directory containing API implementations
    ├── word_count.py     # Word Count API
    ├── number_addition.py # Number Addition API
    ├── api3.py           # String Reversal API
    ├── api4.py           # Temperature Conversion API
    └── api5.py           # Palindrome Check API
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd my-fullstack-app/flask-api
   ```

2. **Create a virtual environment (optional but recommended):**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

## Running the Flask Application

To start the Flask server, run the following command:

```
python app.py
```

The server will start on `http://127.0.0.1:5000/` by default.

## Available APIs

1. **Word Count API**
   - **Endpoint:** `/api/word_count`
   - **Method:** POST
   - **Request Body:** JSON with a key `text` containing the string to count words.
   - **Response:** JSON with the word count.

2. **Number Addition API**
   - **Endpoint:** `/api/number_addition`
   - **Method:** POST
   - **Request Body:** JSON with keys `num1` and `num2` containing the numbers to add.
   - **Response:** JSON with the sum.

3. **String Reversal API**
   - **Endpoint:** `/api/reverse_string`
   - **Method:** POST
   - **Request Body:** JSON with a key `string` containing the string to reverse.
   - **Response:** JSON with the reversed string.

4. **Temperature Conversion API**
   - **Endpoint:** `/api/convert_temperature`
   - **Method:** POST
   - **Request Body:** JSON with a key `celsius` containing the temperature in Celsius.
   - **Response:** JSON with the temperature in Fahrenheit.

5. **Palindrome Check API**
   - **Endpoint:** `/api/check_palindrome`
   - **Method:** POST
   - **Request Body:** JSON with a key `string` containing the string to check.
   - **Response:** JSON indicating whether the string is a palindrome.

## Testing the APIs

You can test the APIs using tools like Postman or curl. Make sure to set the request method and headers appropriately.

## Deployment

For deployment, you can use platforms like Render for the Flask API. Follow the respective platform's documentation for deployment instructions.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
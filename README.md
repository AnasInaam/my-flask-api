# Flask API Documentation

This Flask API provides 5 endpoints for text and number operations. CORS is enabled for frontend integration.

## Setup

```sh
cd flask-api
python -m venv venv
# On Windows: venv\Scripts\activate
# On Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Endpoints & Example Usage

All endpoints: `POST` with JSON `{ "input": "..." }`

| Endpoint                  | Example Input                | Description                        |
|--------------------------|------------------------------|------------------------------------|
| `/word_count`            | `This is a test sentence`    | Returns word count                 |
| `/number_addition`       | `1 2 3.5 4`                  | Returns sum of numbers             |
| `/string_reversal`       | `hello world`                | Returns reversed string            |
| `/temperature_conversion`| `100 C` or `212 F`           | Converts between C and F           |
| `/palindrome_check`      | `racecar`                    | Checks if input is a palindrome    |

### Example curl
```sh
curl -X POST http://127.0.0.1:5000/word_count -H "Content-Type: application/json" -d '{"input": "This is a test"}'
```

## Deployment
- Deploy to [Render](https://render.com/) for production use.

## License
MIT
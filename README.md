# URL Expander and Shortener API

This is a simple Flask application that provides an API for URL expansion and shortening. The application uses two functions from the `utils` module: `shorten_url` and `expand_url`.

## Getting Started

1. Clone the repository or download the code.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the application by executing `python app.py`.

## API Endpoints

The application provides the following API endpoints:

- `GET /`: Returns a welcome message.
- `POST /shorten`: Accepts a JSON object with a `url` field containing the long URL to be shortened. The application will return a JSON object containing the shortened URL.
- `GET /expand/<short_url>`: Accepts a `short_url` parameter. The application will return a JSON object containing the long URL if it exists, or an error message if the URL is not found.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
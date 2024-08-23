from flask import Flask, request, jsonify
import hashlib
import base64
from utils import shorten_url, expand_url, url_mapping

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the URL Expander and Shortener API!"

@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.get_json()
    long_url = data.get('url')
    short_url = shorten_url(long_url)
    return jsonify({'short_url': short_url})

@app.route('/expand/<short_url>', methods=['GET'])
def expand(short_url):
    long_url = expand_url(short_url)
    if long_url:
        return jsonify({'long_url': long_url})
    return jsonify({'error': 'URL not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

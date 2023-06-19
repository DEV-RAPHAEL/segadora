from flask import Flask, request, jsonify
import requests
import re

app = Flask(__name__)
CORS(app)

@app.route('/extract-emails', methods=['POST'])
def extract_emails():
    # Get the website URL from the request body
    data = request.get_json()
    website_url = data['url']

    # Send a GET request to fetch the webpage content
    response = requests.get(website_url)

    # Extract emails using regular expression
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, response.text)

    # Return the extracted emails as JSON response
    return jsonify(emails)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)

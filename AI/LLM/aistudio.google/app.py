# pip install requests
import requests
import configparser

# Load cấu hình từ file chatbot.conf
config = configparser.ConfigParser()
config.read('app.config')
API_URL = config['config']['api_url']
API_KEY = config['config']['api_key']
# URL with API key
url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}'

# Headers
headers = {
    'Content-Type': 'application/json'
}

# Data to be sent in the POST request
data = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Explain how AI works"
                }
            ]
        }
    ]
}

# Sending the POST request
response = requests.post(url, headers=headers, json=data)

# Print the response from the server
print(response.status_code)
print(response.json())  # If the response is in JSON format

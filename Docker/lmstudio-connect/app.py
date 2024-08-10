# Example: reuse your existing OpenAI setup
from openai import OpenAI
import configparser

# Load cấu hình từ file chatbot.conf
config = configparser.ConfigParser()
config.read('app.conf')
API_URL = config['config']['api_url']
API_KEY = config['config']['api_key']

# Point to the local server
client = OpenAI(base_url=API_URL, api_key=API_KEY)

completion = client.chat.completions.create(
  model="model-identifier",
  messages=[
    {"role": "system", "content": "Always answer in rhymes."},
    {"role": "user", "content": "Introduce yourself."}
  ],
  temperature=0.7,
)

print(completion.choices[0].message)
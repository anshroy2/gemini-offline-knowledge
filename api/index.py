from flask import Flask, request
from pprint import pprint
from dotenv import load_dotenv
import os
import sys
import vonage
from urllib.parse import unquote_plus
import json

load_dotenv()
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about/')
def about():
    return 'Python version: ' + sys.version

@app.route('/send/', methods=['POST'])
def send_sms():
    pprint(request)
    if request.get_data():
        data = request.get_data().decode('UTF-8')
        if data:
            payload = unquote_plus(data)
            if payload:
                event = json.loads(payload)
                client = vonage.Client(key=os.environ['VONAGE_API_KEY'], secret=os.environ['VONAGE_API_SECRET'])
                sms = vonage.Sms(client)
                responseData = sms.send_message(
                    {
                        "from": os.environ['SYSTEM_NUMBER'],
                        "to": os.environ['AJIT_NUMBER'],
                        "text": event.get("text", "Default body Text Sent!"),
                    })
                if responseData["messages"][0]["status"] == "0":
                    print("Message sent successfully.")
                    return ("Message sent successfully", 200)
                else:
                    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
                    return ("Error occurred: " + responseData['messages'][0]['error-text'], 200)
            return ('unquote did not work', 200)
        else:
            return ('Get DATA CANT DECODE', 200)
    return ('Needs a body!', 200)

if __name__ == "__main__":
    app.run(debug=True)

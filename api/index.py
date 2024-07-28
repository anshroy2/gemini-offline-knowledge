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


@app.route('/desbug', methods=['POST'])
def example_post_debug():
    print(request)
    if request.get_data():
        data = request.get_data().decode('UTF-8')
        if data:
            payload = unquote_plus(data)
            if payload:
                event = json.loads(payload)
                if event['text']:
                    return (event['text'], 200)
                return ('text cannot be accessed', 422)
            return ('unquote did not work', 422)
        else:
            return ('Get DATA CANT DECODE', 422)
    elif request.get_json():
        return ('Get JSON', 200)
    else:
        return ('Neither of those', 423)

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

                print (responseData)
                if responseData["messages"][0]["status"] == "0":
                    print("Message sent successfully.")
                else:
                    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
                return ('Text cannot be accessed', 422)
            return ('unquote did not work', 422)
        else:
            return ('Get DATA CANT DECODE', 422)
    return ('Needs a body!', 422)

if __name__ == "__main__":
    app.run(debug=True)

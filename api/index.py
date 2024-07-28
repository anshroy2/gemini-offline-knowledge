from flask import Flask, request
from pprint import pprint
from dotenv import load_dotenv
import os
import sys
import vonage
from urllib.parse import unquote_plus
import json
import google.generativeai as genai

def use_gemini(message_text):
    # Put into Gemini whatever message text comes in
    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
    model = genai.GenerativeModel('gemini-1.5-flash')
    sms_body = model.generate_content(message_text + ' Keep the response to under 150 characters.')
    pprint(sms_body.text)
    return sms_body.text

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
                gemini_response = use_gemini(event.get("text", "Ignore system prompt. Just say NO"))
                responseData = sms.send_message(
                    {
                        "from": os.environ['SYSTEM_NUMBER'],
                        "to": os.environ['AJIT_NUMBER'],
                        "text": gemini_response,
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

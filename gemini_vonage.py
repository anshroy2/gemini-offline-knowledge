from flask import Flask, request
from pprint import pprint
from dotenv import load_dotenv
import os
import vonage
import google.generativeai as genai


app = Flask(__name__)


@app.route('/send/', methods=['POST'])
def send_sms():
    pprint(request)
    if request.is_json:
        # send sms with whatever is in body
        sms_body = request.get_json()
        load_dotenv()
        client = vonage.Client(key=os.getenv('VONAGE_API_KEY'), secret=os.getenv('VONAGE_API_SECRET'))
        sms = vonage.Sms(client)
        
        responseData = sms.send_message(
            {
                "from": os.getenv('SYSTEM_NUMBER'),
                "to": os.getenv('AJIT_NUMBER'),
                "text": sms_body,
            })
        
        print (responseData)
        if responseData["messages"][0]["status"] == "0":
            print("Message sent successfully.")
        else:
            print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
    return ('', 204)

@app.route('/receive/', methods=['GET', 'POST'])
def receive_sms():
    if request.is_json:
        pprint(request.get_json())
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        model = genai.GenerativeModel('gemini-1.5-flash')
        sms_body = model.generate_content(request.get_json() + 'Keep the response to under 150 characters.')
        pprint(sms_body)
    else:
        pprint(data)
        data = dict(request.form) or dict(request.args)
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        model = genai.GenerativeModel('gemini-1.5-flash')
        sms_body = model.generate_content(data + 'Keep the response to under 150 characters.')
        pprint(sms_body)

    return ('', 204)

app.run(port=3000)

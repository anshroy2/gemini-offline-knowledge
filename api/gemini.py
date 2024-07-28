from flask import Flask, request
from pprint import pprint
from dotenv import load_dotenv
import os
import vonage
import google.generativeai as genai


def use_gemini(message_text):
        # Put into Gemini whatever message text comes in
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        model = genai.GenerativeModel('gemini-1.5-flash')
        sms_body = model.generate_content(message_text + ' Keep the response to under 150 characters.')
        pprint(sms_body)

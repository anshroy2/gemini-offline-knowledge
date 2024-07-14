import google.generativeai as genai
import os
from dotenv import load_dotenv
from sms_file import question 

load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content(question + 'Keep the response to less than 150 characters.')

# Comment to check

print(response.text)
print(len(response.text))

# Flask SMS Gemini Integration

This repository contains a Flask web application that integrates with the Vonage SMS API and Google Gemini to handle incoming SMS messages and respond with AI-generated content.

## Features

- **Flask Web Server**: A simple Flask application to handle HTTP requests.
- **Vonage SMS API Integration**: Send SMS messages using Vonage.
- **Google Gemini Integration**: Utilize Google Gemini to generate AI-based SMS responses.
- **Environment Variables**: Sensitive information like API keys and phone numbers are managed via environment variables.

## Prerequisites

Ensure you have the following installed:

- Python 3.7+
- `pip` package manager
- Vonage and Google Gemini accounts with API access

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/anshroy2/gemini-offline-knowledge.git
   cd flask-sms-gemini
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**

   Create a `.env` file in the project root with the following variables:

   ```plaintext
   GEMINI_API_KEY=your_gemini_api_key
   VONAGE_API_KEY=your_vonage_api_key
   VONAGE_API_SECRET=your_vonage_api_secret
   SYSTEM_NUMBER=your_system_phone_number
   USER_NUMBER=default_phone_number_for_ajit
   ```

4. **Run the Flask app:**

   ```bash
   python app.py
   ```

## API Endpoints

### `GET /`
Returns a simple "Hello, World!" message.

### `GET /about/`
Returns the Python version running the app.

### `POST /send/`
Processes and sends an SMS message. The body of the request should include a JSON payload with the following format:

```json
{
  "msisdn": "recipient_phone_number",
  "text": "message_text"
}
```

### `POST /webhooks/inbound-message`
Handles inbound messages from Vonage. It supports different formats:
- URL-encoded parameters
- JSON payloads

## Usage

1. **Send SMS Message:**

   Use the `/send/` endpoint with a POST request to send a message. The text will be processed by Google Gemini, and a response will be sent back to the specified phone number.

2. **Handle Inbound SMS:**

   The application can process inbound SMS messages via the `/webhooks/inbound-message` endpoint.

## Debugging

Run the Flask application in debug mode by setting `debug=True` in `app.run()` within the `if __name__ == "__main__":` block.

## License

This project is licensed under the MIT License.

## Acknowledgments

- **Flask**: Micro web framework for Python.
- **Vonage**: API provider for SMS and communication services.
- **Google Gemini**: AI platform for generating content.
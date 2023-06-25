# load imports
from flask import Flask, request, jsonify
import os
from os.path import join, dirname
from pprint import pprint
from dotenv import load_dotenv
import vonage


client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

responseData = client.sms.send_message(
    {
        "from": VONAGE_BRAND_NAME,
        "to": TO_NUMBER,
        "text": "A text message sent using the Vonage SMS API",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

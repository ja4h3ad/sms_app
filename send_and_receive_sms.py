# load imports
from flask import Flask, request, jsonify, render_template
import os
from os.path import join, dirname
from pprint import pprint
from dotenv import load_dotenv
import vonage

# define path to your .env file
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

# fetch the API key from the .env
VONAGE_API_KEY = os.environ.get("VONAGE_API_KEY")
# fetch the API secret from the .env
VONAGE_API_SECRET = os.environ.get("VONAGE_API_SECRET")
# fetch the Vonage Application ID from .env - this is important to generate the JWT
VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
# fetch the private key path generated from the project settings from .env - this is important to generate the JWT
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get("VONAGE_APPLICATION_PRIVATE_KEY_PATH")
# fetch your "From" number that will be the CLID in the outbound SMS
VONAGE_NUMBER = os.environ.get("FROM_NUMBER")
# destination number to transmit SMS to
TO_NUMBER = os.environ.get("TO_NUMBER")

client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

# Application to send and receive SMS messages, as well as DLRs

app = Flask(__name__)

# Create a list to store the response SMS data
response_sms_data = []


@app.route("/")
def index():
    # Retrieve the stored delivery status data from your data store (delivery_receipt())
    message_status_data = delivery_receipt()
    # print("Message Status Data:", message_status_data)
    # print("Response SMS Data:", response_sms_data)
    return render_template('index.html', message_status_data=message_status_data, response_sms_data=response_sms_data)

@app.route("/send_sms", methods=["POST"])
# POST request via web form to send SMS
def send_sms_message():
    destination_number = request.form['destination_number']
    sms_content = request.form['sms_content']
    sms = vonage.Sms(client)
    response = sms.send_message({
        'from': VONAGE_NUMBER,
        'to': destination_number,
        'text': sms_content
    })

    if response["messages"][0]["status"] == "0":
        print("Message sent successfully.")
        # print(response['messages'][0])
    else:
        print(f"Message failed with error: {response['messages'][0]['error-text']}")
    # pprint(response)
    return render_template('index.html')


@app.route('/delivery-receipt', methods=['GET', 'POST'])
def delivery_receipt():
    if request.is_json:
        dlr_data = request.get_json()
    else:
        dlr_data = dict(request.form) or dict(request.args)
    # pprint(dlr_data)

    # Return the delivery receipt data
    return dlr_data


@app.route('/inbound-sms', methods=['GET', 'POST'])
def inbound_sms():
    if request.is_json:
        sms_data = request.get_json()
    else:
        sms_data = dict(request.form) or dict(request.args)

    if sms_data:
        # Store the response SMS data in the list
        response_sms_data.append(sms_data)


    return jsonify(sms_data)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5003)


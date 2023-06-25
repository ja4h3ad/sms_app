# Outbound and Inbound SMS with Vonage API - Flask App
Here are three samples of inbound and outbound SMS using Vonage's SMS API, including DLRs (Delivery Receipts)

1. send_sms.py is a simple script that utilizes the Vonage SDK to set up an outbound SMS.  Get your feet wet
2. receive_sms.py is a set of functions using the flask framework to accept webhooks/API calls to receive inbound SMS messages to your app 
3. dlr.py is a function using the flask framework to accept DLRs
4. send_and_receive_sms.py is a combination of all of them for use in a server-side app for message




## Prerequisites

Before running the application, make sure you have the following prerequisites:

- Python 3.x installed
- Flask framework installed
- Required Python packages listed in the `requirements.txt` file installed
- Vonage API credentials (Application ID, private key, and Vonage number)
- Properly configured environment variables in a `.env` file

## Getting Started

1. Clone the repository

2. Install the required packages:
pip install -r requirements.txt


3. Configure the environment variables:
Create a `.env` file in the project's root directory and add the following variables:
VONAGE_APPLICATION_ID=<your_vonage_application_id>
VONAGE_APPLICATION_PRIVATE_KEY_PATH=<path_to_private_key_file>
FROM_NUMBER=<your_vonage_number>
TO_NUMBER=<destination_number_to_call>

4. Run the application:
e.g, python app.py or directly in your IDE

6. Access the application:

Visit `http://localhost:5003` with route extension ('/')in your web browser to confirm the application is running and reachable.


Please refer to the code comments within each `.py` for more detailed explanations of the implementation.

## License

This project is licensed under the [MIT License](LICENSE).




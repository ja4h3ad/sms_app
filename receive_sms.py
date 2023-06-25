from pprint import pprint
from flask import Flask, request, jsonify
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

app = Flask(__name__)

@app.route('/webhooks/inbound-sms', methods=['GET', 'POST'])
def inbound_sms():
    if request.is_json:
        pprint(request.get_json())
    else:
        data = dict(request.form) or dict(request.args)
        pprint(data)

    return ('', 204)



if __name__ == '__main__':
    app.run(port=5002)
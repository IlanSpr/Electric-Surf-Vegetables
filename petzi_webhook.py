import sqlite3
import json
from datetime import datetime

from flask import Flask, request, jsonify
import hashlib
import hmac

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect('petzi.db')
    cur = conn.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS petzi (
                    ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ticket TEXT)
    ''')
    conn.commit()
    conn.close()


def process_data(data):
    print("Processing data...")
    conn = sqlite3.connect('petzi.db')
    cur = conn.cursor()
    data_str = json.dumps(data)
    cur.execute('INSERT INTO petzi (ticket) VALUES (?)', (data_str,))
    conn.commit()
    conn.close()


def is_request_valid(req):
    secret = 'queenQuartet'.encode()

    received_sig_full = req.headers.get('Petzi-Signature')
    signature_parts = dict(part.split('=') for part in received_sig_full.split(','))

    body_to_sign = f'{signature_parts["t"]}.{req.data.decode()}'.encode()
    expected_sig = hmac.new(secret, body_to_sign, hashlib.sha256).hexdigest()

    if not hmac.compare_digest(signature_parts['v1'], expected_sig):
        return False

    time_delta = (datetime.now() -
                  datetime.fromtimestamp(int(signature_parts['t'])))
    if time_delta.total_seconds() > 30:
        return False

    return True


@app.route('/webhook', methods=['POST'])
def webhook():
    print("Received webhook request")
    data = request.json

    if not is_request_valid(request):
        return jsonify({'error': 'Invalid request'}), 403

    # Process the data only once after validation
    process_data(data)

    return jsonify({'status': 'success'}), 200


if __name__ == '__main__':
    init_db()
    app.run(debug=True)

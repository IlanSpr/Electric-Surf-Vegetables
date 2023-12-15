from flask import request, jsonify
from .validation import is_request_valid
from .app_db import process_data
from .rabbitmq import send_message


def init_app_routes(app):
    @app.route('/webhook', methods=['POST'])
    def webhook():
        if not is_request_valid(request):
            return jsonify({'error': 'Invalid request'}), 403

        data = request.get_json()
        process_data(app, data)

        try:
            send_message('petzi', data)
        except Exception as e:
            app.logger.error(e)
            return jsonify({'error': 'Error sending message'}), 500

        return jsonify({'status': 'success'}), 200

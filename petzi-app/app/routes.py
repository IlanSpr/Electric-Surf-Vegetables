from flask import request, jsonify
from .validation import is_request_valid
from .app_db import process_data
from .rabbitmq import sending_message


def init_app_routes(app):
    @app.route('/webhook', methods=['POST'])
    def webhook():
        # Check if the request is valid first
        if not is_request_valid(request):
            return jsonify({'error': 'Invalid request'}), 200

        try:
            data = request.get_json()
        except Exception as e:
            app.logger.error(f"Error in parsing request data: {e}")
            return jsonify({'error': 'Invalid JSON data'}), 200

        process_data(app, data)

        try:
            sending_message(data)
            app.logger.info("Message successfully sent to RabbitMQ.")
        except Exception as e:
            app.logger.error(f"Error in sending message: {e}")
            return jsonify({'error': 'Error sending message to RabbitMQ'}), 200

        return jsonify({'status': 'success'}), 200

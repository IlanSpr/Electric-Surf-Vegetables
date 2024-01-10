from flask import request, jsonify, Response, stream_with_context
from .validation import is_request_valid
from .app_db import process_data
from .rabbitmq import sending_message
from .sse import stream_messages


def init_app_routes(app):
    @app.route('/webhook', methods=['POST'])
    def webhook():

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

    @app.route('/events')
    def sse():
        try:
            return Response(stream_with_context(stream_messages()), content_type='text/event-stream')
        except Exception as e:
            app.logger.error(f"Error in streaming messages: {e}")
            return jsonify({'error': 'Error streaming messages'}), 500

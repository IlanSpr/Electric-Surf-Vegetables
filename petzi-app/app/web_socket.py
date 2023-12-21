from flask_socketio import SocketIO
from .rabbitmq import receive_message
import json
import threading


def create_socketio_app(flask_app):
    socketio = SocketIO(flask_app, cors_allowed_origins="*")  # Enable CORS if necessary

    def message_receiver():
        def rabbitmq_callback(ch, method, properties, body):
            message = json.loads(body)
            socketio.emit('ticket_event', message)  # Emitting to 'ticket_event' channel

        receive_message('petzi', rabbitmq_callback)

    def start_receiver():
        threading.Thread(target=message_receiver, daemon=True).start()

    socketio.on('connect', namespace='/tickets')(start_receiver)  # Start receiver on client connect
    return socketio

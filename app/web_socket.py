from flask_socketio import SocketIO, emit
from .rabbitmq import receive_message
import json
import threading


def create_socketio_app(flask_app):
    socketio = SocketIO(flask_app)

    def message_receiver():
        def rabbitmq_callback(ch, method, properties, body):
            message = json.loads(body)
            emit('message', message)

        receive_message('petzi', rabbitmq_callback)

    threading.Thread(target=message_receiver, daemon=True).start()
    return socketio

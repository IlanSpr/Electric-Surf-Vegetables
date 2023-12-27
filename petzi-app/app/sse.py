from flask import Flask, Response, stream_with_context
import json
import pika

app = Flask(__name__)

def stream_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    def callback(ch, method, properties, body):
        yield f"data: {body.decode()}\n\n"

    channel.basic_consume(queue='petzi', on_message_callback=callback, auto_ack=True)

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
        connection.close()

@app.route('/events')
def sse():
    return Response(stream_with_context(stream_messages()), content_type='text/event-stream')


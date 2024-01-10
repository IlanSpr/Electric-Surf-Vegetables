import logging
import pika
import json
import threading
import queue
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("sse")


def stream_messages():
    message_queue = queue.Queue()
    running = threading.Event()
    running.set()

    def consume_messages():
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
        channel = connection.channel()
        channel.queue_declare(queue='petzi')

        def callback(ch, method, properties, body):
            logger.info(f"Received message from queue: {body.decode()}")

            message_queue.put(body.decode())

        channel.basic_consume(queue='petzi', on_message_callback=callback, auto_ack=True)

        while running.is_set():
            channel.connection.process_data_events(time_limit=1)

        channel.stop_consuming()
        connection.close()

    consumer_thread = threading.Thread(target=consume_messages)
    consumer_thread.start()

    try:
        while True:
            if not message_queue.empty():
                message = message_queue.get()
                yield f"data: {json.dumps({'message': message})}\n\n"
            else:
                time.sleep(1)
                yield f":heartbeat\n\n"
    except GeneratorExit:
        running.clear()
        consumer_thread.join()

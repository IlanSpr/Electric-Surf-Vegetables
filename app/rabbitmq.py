import pika
import json

def send_message(queue, message):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))  # Adjust host if necessary
    channel = connection.channel()

    channel.queue_declare(queue=queue)

    channel.basic_publish(exchange='',
                          routing_key=queue,
                          body=json.dumps(message))
    print(f" [x] Sent {message} to {queue}")

    connection.close()

def receive_message(queue):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue=queue)

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


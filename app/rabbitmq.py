import time

import pika
import json


def send_message(queue, message_data):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    # Ensure the queue exists
    channel.queue_declare(queue=queue)

    # Determine the type of event from the message data
    event_type = message_data.get('event')
    formatted_message = ''
    if event_type == 'ticket_created':
        formatted_message = 'ticket sold event'
    elif event_type == 'ticket_updated':
        formatted_message = 'ticket updated event'
    # Add more conditions as needed for other event types

    # Send the formatted message
    channel.basic_publish(exchange='', routing_key=queue, body=json.dumps(formatted_message))
    print(f" [x] Sent '{formatted_message}' to {queue}")

    connection.close()


def receive_message(queue, callback, max_retries=5, retry_delay=5):
    """Receive messages from RabbitMQ with retry logic."""
    attempt = 0
    while attempt < max_retries:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
            channel = connection.channel()
            channel.queue_declare(queue=queue, durable=True)
            channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
            channel.start_consuming()
            break  # Successful connection and consumption
        except pika.exceptions.AMQPConnectionError as e:
            attempt += 1
            print(f"Connection failed, attempt {attempt}/{max_retries}. Error: {e}")
            time.sleep(retry_delay)  # Wait before retrying

    if attempt == max_retries:
        print("Failed to connect to RabbitMQ after several attempts.")



from confluent_kafka import Producer
from confluent_kafka.admin import AdminClient, NewTopic


def setup_kafka(app):
    kafka_config = {
        'bootstrap.servers': 'kafka:9092',  # Adjust as needed
    }

    admin_client = AdminClient(kafka_config)

    topic_name = 'petzi'
    topic = NewTopic(topic_name, num_partitions=1, replication_factor=1)


    try:
        admin_client.create_topics([topic])
        print("Topic '{}' created".format(topic_name))
    except Exception as e:
        print("Failed to create topic '{}': {}".format(topic_name, e))


    global producer
    producer = Producer(kafka_config)


def send_message(topic, message):
    # Make sure producer is initialized
    if 'producer' not in globals():
        raise Exception("Kafka producer not initialized")

    try:
        producer.produce(topic, message)
        producer.flush()
    except Exception as e:
        print("Failed to send message to topic '{}': {}".format(topic, e))

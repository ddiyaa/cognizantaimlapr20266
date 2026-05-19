#read messages from aiven kafka comedy-movies
from pathlib import Path
from confluent_kafka import Consumer
import json

from kafkamessageapp.configurations.conf import KafkaConfig

BASE_DIR = Path(__file__).resolve().parent.parent
def kafka_config():
    conf = {
        'bootstrap.servers': KafkaConfig.BOOTSTRAP_SERVERS,
        'security.protocol': KafkaConfig.SECURITY_PROTOCOL,
        'ssl.ca.location': str(BASE_DIR / "ca.pem"),
        'ssl.certificate.location': str(BASE_DIR / "service.cert"),
        'ssl.key.location': str(BASE_DIR / "service.key"),
         "group.id": "action-movies-consumer-group",
         "auto.offset.reset": "earliest"
    }
    return conf

def kafka_consumer():
    conf = kafka_config()
    consumer = Consumer(conf)
    consumer.subscribe([KafkaConfig.TOPIC_NAME])
    return consumer

def consume_messages(consumer):
    try:
        while True:
            msg = consumer.poll(5.0)  # Poll for messages with a timeout of 5 seconds
            print("Polling for messages...")    
            if msg is None:
             continue

            if msg.error():
             print("Kafka error:", msg.error())
             continue

            data = json.loads(msg.value().decode("utf-8"))

      
            print(f"Received message: {data}") 


    except KeyboardInterrupt:
        print("Consumer stopped")

    finally:
        consumer.close()


if __name__ == "__main__":
    consumer = kafka_consumer()
    consume_messages(consumer)
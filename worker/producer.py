import pika
import os
import time


def consume(rabbitmq_host, queue_name, callback):
    rabbitmq_user = os.environ.get("RABBITMQ_DEFAULT_USER")
    rabbitmq_pass = os.environ.get("RABBITMQ_DEFAULT_PASS")
    credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
    parameters = pika.ConnectionParameters(host=rabbitmq_host, credentials=credentials)

    connection = None
    while connection is None:
        try:
            connection = pika.BlockingConnection(parameters)
        except pika.exceptions.AMQPConnectionError:
            print("[worker1] Connecting to RabbitMQ....")
            time.sleep(3)

    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    finally:
        connection.close()
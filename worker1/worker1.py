import os
import json
from bson import json_util
from producer import consume
from database import get_interface, save_result

QUEUE_NAME = "router_jobs"


def callback(ch, method, properties, body):
    try:
        job = json_util.loads(body)
        ip = job.get("ip")
        username = job.get("username")
        password = job.get("password")

        print(f"[worker1] Received job for {ip}")

        result = run_show_ip_interface_brief(ip, username, password)
        save_result(ip, result)

        print(f"[worker1] Saved result for {ip} to MongoDB")
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"[worker1] Error processing job: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)


def worker():
    rabbitmq_host = os.environ.get("RABBITMQ_HOST", "localhost")
    consume(rabbitmq_host, QUEUE_NAME, callback)


if __name__ == "__main__":
    worker()
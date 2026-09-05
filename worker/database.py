from pymongo import MongoClient
from datetime import datetime, UTC
import os

def save_interface_status(router_ip, interfaces):

    MONGO_URI = os.getenv("MONGO_URI")
    DB_NAME = os.getenv("DB_NAME")

    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db["interface_status"]

    data = {
        "router_ip": router_ip,
        "timestamp": datetime.now(UTC),
        "interfaces": interfaces,
    }
    collection.insert_one(data)
    client.close()

# def get_mongo_collection():
#     mongo_uri = os.environ.get("MONGO_URI")
#     db_name = os.environ.get("DB_NAME")
#     client = MongoClient(mongo_uri)
#     db = client[db_name]
#     return db["interface_results"]


# def get_interface(ip, username, password):
#     device = {
#         "device_type": "cisco_ios",
#         "host": ip,
#         "username": username,
#         "password": password,
#     }
#     conn = ConnectHandler(**device)
#     output = conn.send_command("show ip interface brief", use_textfsm=True)
#     conn.disconnect()
#     return output


# def save_result(ip, result):
#     collection = get_mongo_collection()
#     now = time.time()
#     now_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now))
#     ms = int((now % 1) * 1000)
#     doc = {
#         "ip": ip,
#         "timestamp": f"{now_str}.{ms:03d}",
#         "result": result,
#     }
#     collection.insert_one(doc)
#     return doc
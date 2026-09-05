import os
import time
from pymongo import MongoClient
from netmiko import ConnectHandler


def get_mongo_collection():
    mongo_uri = os.environ.get("MONGO_URI")
    db_name = os.environ.get("DB_NAME")
    client = MongoClient(mongo_uri)
    db = client[db_name]
    return db["interface_results"]


def get_interface(ip, username, password):
    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": username,
        "password": password,
    }
    conn = ConnectHandler(**device)
    output = conn.send_command("show ip interface brief", use_textfsm=True)
    conn.disconnect()
    return output


def save_result(ip, result):
    collection = get_mongo_collection()
    now = time.time()
    now_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now))
    ms = int((now % 1) * 1000)
    doc = {
        "ip": ip,
        "timestamp": f"{now_str}.{ms:03d}",
        "result": result,
    }
    collection.insert_one(doc)
    return doc
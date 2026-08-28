import pika
import os
from netmiko import ConnectHandler

device_list =[
    {"name":"R49",'host': '192.168.1.42',}
]
static={
    'username': 'admin',
    'password': 'cisco',
    'device_type': 'cisco_ios',
}


def run_command(name):
    device_name = name.pop("name")
    conn_params = {**static, **device}
    
    print(f"Connect to {device_name}...")
    conn = None
    try:
        conn = ConnectHandler(**conn_params)
        output = conn.send_command("sh ip int br")
        print(output)
    except Exception as e:
        print(f"Error -> {e}")
    finally:
        print(f"{device_name} -> Done")
if __name__ == "__main__":
    for device in device_list:
        run_command(device)
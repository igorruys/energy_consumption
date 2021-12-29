# python 3.6
# setup MQTT: https://www.youtube.com/watch?v=AsDHEDbyLfg&ab_channel=BRUHAutomation
# sourcecode: https://www.emqx.com/en/blog/how-to-use-mqtt-in-python

import random
import json
import time
from paho.mqtt import client as mqtt_client
from os import path
import csv
from datetime import datetime


broker = 'IP'
port = 1883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'xxxx'
password = 'xxxx'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    if not path.exists(light_file_name):
        with open(light_file_name, mode='w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

    def handle_telemetry(client, userdata, message):
        payload = json.loads(message.payload.decode())
        print("Message received:", payload)

        with open(light_file_name, mode='a') as light_file:        
            light_writer = csv.DictWriter(light_file, fieldnames=fieldnames)
            light_writer.writerow({'date' : datetime.now().astimezone().replace(microsecond=0).isoformat(), 'light' : payload['light']})

    client.subscribe(topic)
    client.on_message = handle_telemetry


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    light_file_name = 'light.csv'
    fieldnames = ['date', 'light']
    run()

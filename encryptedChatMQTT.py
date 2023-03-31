import paho.mqtt.client as mqtt
from cryptography.fernet import Fernet

# Define MQTT broker details
broker_address = "localhost"
broker_port = 1883

# Define encryption key
key = Fernet.generate_key()
fernet = Fernet(key)

# Define callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("chat")

def on_message(client, userdata, msg):
    decrypted_message = fernet.decrypt(msg.payload).decode()
    print("Received message: "+decrypted_message)

def on_publish(client, userdata, mid):
    print("Message published")

# Create MQTT client and connect to broker
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.connect(broker_address, broker_port)

# Start loop to listen for messages
client.loop_start()

# Start chat loop
while True:
    message = input("Enter message: ")
    encrypted_message = fernet.encrypt(message.encode())
    client.publish("chat", encrypted_message)

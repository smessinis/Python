import paho.mqtt.client as mqtt

# Define MQTT broker details
broker_address = "localhost"
broker_port = 1883
topic = "my_topic"

# Define callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print("Received message on topic "+msg.topic+": "+msg.payload.decode())

# Create MQTT client and connect to broker
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, broker_port)

# Start loop to listen for messages
client.loop_start()

# Publish a message
client.publish(topic, "Hello, world!")

# Wait for messages to be received
input("Press Enter to exit...")

# Stop MQTT client
client.loop_stop()
client.disconnect()

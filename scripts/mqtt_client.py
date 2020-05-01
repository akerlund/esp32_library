import paho.mqtt.client as mqtt
import time

broker_address = "192.168.50.80"

def on_message(client, userdata, message):

  print("message received " ,str(message.payload.decode("utf-8")))
  print("message topic=",message.topic)
  print("message qos=",message.qos)
  print("message retain flag=",message.retain)


def on_log(client, userdata, level, buf):
  print("log: ",buf)


def on_connect(client, userdata, flags, rc):

  print("Connected with result code " + str(rc))

  # Subscribing in on_connect() means that if we lose the connection and
  # reconnect then subscriptions will be renewed.
  client.subscribe("$SYS/#")
  client.subscribe("house/bulbs/bulb1")

client = mqtt.Client(client_id = "ssa")

client.on_message = on_message
client.on_connect = on_connect
client.on_log     = on_log

client.enable_logger()

client.connect(broker_address)
#client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_start()

print("Publishing message to topic","house/bulbs/bulb1")
client.publish("house/bulbs/bulb1","OFF")

time.sleep(4)
client.loop_stop()
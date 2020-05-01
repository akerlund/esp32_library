import paho.mqtt.client as mqtt
import time, struct

broker_address = "192.168.50.80"

def on_message(client, userdata, message):

  rx_data = struct.unpack('16B', message.payload)

  temp_n = rx_data[0]  << 24 | rx_data[1]  << 16 | rx_data[2]  << 8 | rx_data[3]
  temp_d = rx_data[4]  << 24 | rx_data[5]  << 16 | rx_data[6]  << 8 | rx_data[7]
  pres_n = rx_data[8]  << 24 | rx_data[9]  << 16 | rx_data[10] << 8 | rx_data[11]
  pres_d = rx_data[12] << 24 | rx_data[13] << 16 | rx_data[14] << 8 | rx_data[15]

  print("INFO [on_message] Message received")
  print("temp = %f" % (temp_n + temp_d/10))
  print("pres = %f" % (pres_n + pres_d/100))


def on_log(client, userdata, level, buf):

  print("INFO [on_log] Log received")
  print("log: ", buf)


def on_connect(client, userdata, flags, rc):

  print("Connected with result code " + str(rc))

  # Subscribing in on_connect() means that if we lose the connection and
  # reconnect then subscriptions will be renewed.
  client.subscribe("#")
  #client.subscribe("/beat")

client = mqtt.Client(client_id = "ssa")

client.on_message = on_message
client.on_connect = on_connect
client.on_log     = on_log

client.enable_logger()

client.connect(broker_address)

client.loop_start()

time.sleep(60)
client.loop_stop()

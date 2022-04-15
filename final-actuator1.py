import paho.mqtt.client as mqtt
import os
import time
# Sense hat instance

from sense_hat import SenseHat
sense = SenseHat()
# New mqtt client

client = mqtt.Client("greenhouse")
#Connects to the server IP

mqttBroker = "192.168.1.125"
#uses connection
client.connect(mqttBroker)


# new method to grab the data

def on_message(client, userdata, message):
        # decodes the message currently being sent by the server
   
    data = (message.payload.decode("utf-8"))
    # print(type(data))
    # Analyses the message being sent, if temperature too high, it will turn on the fan. If okay, it will do nothing. If too low, it will turn on  heating lights.
    if(message.topic == "temphigh"):
      print("Temperature is too high! Turning on fan:", data)
      sense.clear(255, 0, 0)
      time.sleep(10)
    elif(message.topic == "tempok"):
        print("Temperature is perfect:", data)
        sense.clear(255,0,255)
        time.sleep(5)
        
    elif(message.topic == "templow"):
        print("Temperature is too low! Turning on heating lights:", data)
        sense.clear(255, 255, 0)
        time.sleep(5)
    
    
    # Analyses the message being sent. If there's enough light, it will do nothing. However if it's nighttime and light too low, it will turn on the UV light
    if(message.topic == "lightbad"):
      print("Light levels are too low- night time! Turning on UV lights", data)
      sense.clear(128, 0, 128)
      time.sleep(10)
    elif(message.topic == "lightok"):
        print("Light levels are perfect- day time:", data)
        #sense.clear(100,21,255)
        time.sleep(5)
    
# subscribes to receive the messages
client.subscribe("#")
client.loop_start()
# loop to get messages, then does it for 990 seconds
client.on_message = on_message
time.sleep(990)

client.loop_stop()

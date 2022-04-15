import paho.mqtt.client as mqtt
import os
import time
from sense_hat import SenseHat
#Sense hat instance
sense = SenseHat()
# New mqtt client
client = mqtt.Client("grenhouse2")
#Connects to the server IP
mqttBroker = "192.168.1.125"
#uses connection
client.connect(mqttBroker)


# new method to grab the data
def on_message(client, userdata, message):
    # decodes the message currently being sent by the server
    data = (message.payload.decode("utf-8"))
    # print(type(data))
    # if statement to check if the data being sent is humidity, if too high it opens trap door, if ok does nothing, if too low, turns on sprinklers
    if(message.topic == "humidhigh"):
      print("Humidity is too high! Opening trap door:", data)
      sense.clear(0, 128, 0)
      time.sleep(10)
    elif(message.topic == "humidok"):
        print("Humidity is perfect:" , data)
        sense.clear(100,21,255)
        time.sleep(5)
    elif(message.topic == "humidlow"):
        print("Humidity is too low! Turning on sprinklers:", data)
        sense.clear(0, 0, 255)
        time.sleep(5)
        
    # if statement to verify that the data being sent is the co2 data, if too high it will turn on the fan, if it's fine it will do nothing and if too low it will turn on sprinklers
    if(message.topic == "co2high"):
        print("CO2 levels are too high! Turning on fan:", data)
        sense.clear(255, 0, 0)
        time.sleep(10)
    elif(message.topic == "co2ok"):
        print("CO2 levels are fine:", data)
        sense.clear(100,21,255)
        time.sleep(5)
    elif(message.topic == "co2low"):
        print("CO2 is too low! Turning on sprinklers:", data)
        sense.clear(100,21,255)
        time.sleep(5)
    
    
# subscribes to receive the messages
client.subscribe("#")
client.loop_start()
# loop to get messages, then does it for 990 seconds
client.on_message = on_message
time.sleep(990)

client.loop_stop()

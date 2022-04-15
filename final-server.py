import paho.mqtt.client as mqtt
import os
import time
from sense_hat import SenseHat
sense = SenseHat()
client = mqtt.Client("tesdsdssaaub")
mqttBroker = "192.168.1.125"
client.connect(mqttBroker)


client1 = mqtt.Client("testclient1")
client1.connect(mqttBroker)


client2 = mqtt.Client("testclient2")
client2.connect(mqttBroker)

def on_message(client, userdata, message):
    
    data = (message.payload.decode("utf-8"))
    #print(type(data))
    if(message.topic == "temperature"):
        print("this is temperature:", data)
        if int((data)) > 39:
            client1.publish("temphigh", "OK")
            
        elif int(data) <39 and int(data) > 32:
            client1.publish("tempok", "OK")
            
        elif int(data) < 32:
            client1.publish("templow", "OK")
        
    elif(message.topic == "humidity"):
        print("this is humidity:", data)
        if int(data) > 40:
            client2.publish("humidhigh", "OK")
            
        elif int(data ) < 40 and int(data) > 34 :
            client2.publish("humidok" , "OK")
            
            
        elif int(data ) < 34:
            client2.publish("humidbad" , "OK")
            # sense.clear(0,255,0)
        #print("tested")
        
           # sense.clear(255,0,0)
    elif(message.topic == "CO2"):
        print("this is CO2:", data)
        if int(data) > 1300:
            client2.publish("co2high", "OK")
            
        elif int(data ) < 1300 and int(data) > 1000 :
            client2.publish("co2ok" , "OK")
            
            
        elif int(data ) < 1000:
            client2.publish("co2low" , "OK")
            
    elif(message.topic == "Light"):
        print("this is light :", data)
        if int(data) ==  0:
            client1.publish("lightbad", "OK")
            
            
        elif int(data ) == 1:
            client1.publish("lightok" , "OK")
    

client.subscribe("#")
client.loop_start()
client.on_message = on_message
time.sleep(990)

client.loop_stop()

from sense_hat import SenseHat
import time
import paho.mqtt.client as mqtt
import os
import time
import RPi.GPIO as GPIO
def on_message(client, userdata, message):
    data = str(message.payload.decode("utf-8"))
    print(data)

mqttBroker = "192.168.1.125"
#mqttBroker = "192.168.1.125"
#192.168.1.125
client = mqtt.Client("testclient")
client.connect(mqttBroker)


#client.loop_start()

#client.subscribe("muie")
#client.on_message = on_message
#time.sleep(99)

#client.loop_stop()
sense = SenseHat()

def RCtime(RCpin):
    reading = 0
    GPIO.setup(RCpin,GPIO.OUT)
    GPIO.output(RCpin,GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(RCpin,GPIO.IN)
    if (GPIO.input(RCpin) == GPIO.LOW):
        reading = 1
        
    else:
        reading = 0
        
    return reading

#def tempcheck():
    
    
#i = 25 
while True:
    
   # if sense.get_humidity() > 45:
     #   sense.clear(255,0,0)
     #   print("Humidity too high! Deploying sprinkler!")
        
   # elif sense.get_humidity() < 25:
        
    #   sense.clear(0,255,0)
     #  print("Humidity too low! Deploying heat!")
    
        
   # if sense.get_temperature() > 39:
    #    sense.clear(255,0,255)
    #    print("Temp too high! Deploying fan!")
        
   # elif sense.get_temperature() < 32:
       # sense.clear(122,125,0)
       # print("Temp too low! Deploying heat!")
    
        
        
  #  if sense.get_pressure() > 1040:
      #  sense.clear(0,255,255)
      #  print("CO2 too high ! Closing window! !")
        
   # elif sense.get_pressure() < 1000:
     #   sense.clear(255,255,0)
       # print("CO2 too low! OPening window")
    
    #else:
        #sense.clear(0,0,0)
    
    #print("Tempreading %s"%  sense.get_temperature())
   # print("Humidity reading %s"% sense.get_humidity())
    #print("Pressure reading %s"% sense.get_pressure())
    client.publish("temperature", int(sense.get_temperature()))
   
    time.sleep(5)
    client.publish("humidity", int(sense.get_humidity()))
    time.sleep(2)
    
    client.publish("CO2", int(sense.get_pressure()))
    time.sleep(2)
    print("published")
    
   # client.publish("LIght", RCtime(7))
    #time.sleep(2)
    #tempcheck()
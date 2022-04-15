# Project’s Purpose
This is a Smart Greenhouse which makes use of IoT technologies in order to monitor, analyse and take appropriate actions in order to maximise crop growth and welfare.
# Required Hardware
For this system to run, you will need 4 Raspberry Pis. These Pis will gather data from temperature sensor, humidity, CO2 and light sensor. Because there was no available gas sensor, we simulated the CO2 reading using a pressure sensor. 
These sensors will send data to actuators. The following actuators this system will use are: sprinklers, trap door, UV lights, heating lights, fan. Since most of them weren’t available, we simulated their actions buy turning on different colors of LEDs. .
# Actuator Simulations
- Sprinklers  
When sprinklers are turned on, there will be BLUE LEDs turned on and the terminal will show their state. 
- Trap Door  
When the trap door is opened, there will be GREEN LEDs turned on and the terminal will show its state.
- Heating Lights  
When heating lights are turned on, there will be YELLOW LEDs turned on and the terminal will show their state.
- UV Lights  
When UV lights are turned on, there will be PURPLE LEDs turned on and the terminal will show their state.
- Fan  
To simulate a fan, there will be RED LEDs turned on and the terminal will show its state.



# Setup notes
 Run this: `pip install paho-mqtt`  in every RPI’s client console.
`sudo apt install mosquito mosquito-clients`
`mosquito -d`
Order to run files in:
`$python3 final-datagrabber.py`
`$python3 final-server.py`
`$python3 final-actuator1`
`$python3 final-actuator2`
Wiring needed for the light sensor:
![image](https://user-images.githubusercontent.com/74258818/163583157-ff57180e-3a25-465e-ae06-34696c35d8b3.png)


## Final-datagrabber.py:
This class/file is used to grab the data from the raspberry to then send it over to the server. It grabs the current readings of :
Light (1 if enough light, 0 if not enough)
Temperature(temp sensor , analog, is converted to digital afterwards for easier reading)
CO2 (we did not have a CO2 sensor so instead we used the RPi pressure sensor to simulate the CO2)
Humidity (humidity sensor. Same as temperature in the idea that it’s initially grabbed analog and then converted to digital values)
Then, it creates an MQTT connection to publish the data to the following server.

## Final-server.py:
The final-server.py file is used as the median between the actuators and the data-grabber. What it does is a relatively simple process. It gathers the data sent by the datagrabber and processes it accordingly to then send the correct value in the right place. For example, if the value currently being read is the humidity value, it will send the value to actuator2 whilst if it is the temperature value, it will send it to actuator1. 
The process is the following:
- If it’s temperature or light data -> Data is sent to actuator1, , whilst also being processed
- If the temperature is above 39 -> it will send the ‘’temphigh’’ message to signify the actuator should turn on the trap.
- If the temperature is between 39 and 32 degrees, ->  it will send the ‘’tempok’’ message to signify that the temperature is okay.
- If the temperature is below 32 degrees -> it will send the ‘’templow’’ message to signify that the heating system should be turned on.

If the light is ‘’lightok’’ -> it will tell the actuator to just display a message saying everything is fine.
If the light is ‘’lightbad’’ -> it will tell the actuator to turn on the UV Light.


If it’s humidity or CO2 -> Data is sent to actuator2 :
- If the humidity is above 45 -> It will send the ‘’humidhigh’’ message to the actuator to signify that the humidity level is high, and the heat should be turned on.
- If the humidity is between 45 and 30 -> It will send ‘’humidok’’ message to the actuator to signify that the humidity level is okay.
- If the humidity is below 30 -> it will send the ‘’humidlow’’ message to the actuator to signify that the actuator should turn on the sprinkler.

- If CO2 level is above 1200 -> It will send ‘’CO2high’’ to the actuator to signify that the CO2 level is high.
- If the CO2 level is between 1000 and 1200 -> it will send ‘’CO2ok” to the actuator to signify that the CO2 level is good.
- If the CO2 level is lower than 1000 -> it will send ‘’co2low’’ to the actuator to signify that the CO2 level is low. 

 ## Final-actuator1.py:
The final actuator1 file receives the temperature and light instructions from the server and changes the values accordingly.   In our case, to simulate the sprinkler and heat/vent/trap being turned on, we used an LED light.


 ## Final-actuator2.py:
The final actuator2 file receives the humidity and CO2 instructions from the server and changes the values accordingly.   In our case, to simulate the sprinkler and heat/vent/trap being turned on, we used an LED light.

# Improvements:
The code has the ability to run a light sensor as well, however our light sensor broke, therefore we ended up not using it and just leaving the code there and it will work if you plug in another light sensor.
There were not enough monitors in order to run the entire system of all 4 RPi's, however we have included a demo using 1 local host RPi that's running all 4 devices and another demo (using a borrowed monitor) to show we got the MQTT Broker to communicate with the clients and process their data.



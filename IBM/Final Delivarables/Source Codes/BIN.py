#Project: Smart Waste Management System for Metropolitan cities #Team ID: PNT2022TMID01880

#Installing necessary libraries
import wiotp.sdk.device
import time
import random
import requests
import math

#Configuration details for connecting python script to IBM Watson IOT Platform
myConfig = { "identity": {
"orgId": "1hx03x",
"typeId": "cloud",
"deviceId":"232323"
},
"auth": {
"token": "12345678"
} }

def myCommandCallback(cmd):
        print("Message received from IBM IoT Platform: %s" % cmd.data)


#Connecting the client to ibm watson iot platform
client = wiotp.sdk.device.DeviceClient(config=myConfig,logHandlers= None)
client.commandCallback = myCommandCallback
client.connect()
print("CONNECTED");
 

while True:

        res = requests.get('https://ipinfo.io/')
        data = res.json()
        loc = data['loc'].split(',')
        theta = random.uniform(0,2*math.pi)
        area = (0.05**2)*math.pi
        radius = math.sqrt(random.uniform(0,area/math.pi))
        latitude,longitude = [float(loc[0])+radius*math.cos(theta), float(loc[1])+radius*math.sin(theta)]

        binlevel=random.randint(10,100)
        distance = random.randint(10,100)
        if binlevel>80:
                myData={'Distance':distance, 'latitude':latitude, 'longitude':longitude,'binlevel':binlevel}
                client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
                client.commandCallback = myCommandCallback
                print("BIN IS FULL...")
                print("SENDING THE DATA...")
                time.sleep(2)
        else :
                print("BIN IS IN NORMAL LEVEL...")
                time.sleep(2)
                 
#Disconnect the client connection
client.disconnect()

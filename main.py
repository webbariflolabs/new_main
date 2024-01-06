import paho.mqtt.client as mqtt
import time
from random import uniform , randrange
import json
from datetime import datetime

# def on_connect(client , userdata , flags ,rc):
#     if rc == 0:
#         print("Client Is Connected")
#         global connected
#         connected = True
#     else:
#         print("Print Connection Faild")



connected = False
broker_address = "4.240.114.7"
port = 1883
username = "BarifloLabs"
password = "Bfl@123"


client = mqtt.Client("MQTT")
client.username_pw_set(username,password)
# client.on_connect = on_connect
client.connect(broker_address,port=port)


def postDataFeed(dt):
    topic = "661526019560586"
    dtStr = json.dumps(dt)
    print("dtStr .....",dtStr)
    client.publish(topic+"/data",dtStr) 


# while True:
now = datetime.now()
date_tm = now.strftime("%Y-%m-%d %H:%M:%S")
randNum = uniform(1.0,2.0)
randNum2 = uniform(1.0,2.0)
postDataFeed({"dataPoint": date_tm, "paramType": 'Sensor1', "paramValue": randNum , "deviceId" :"661526019560586"})
postDataFeed({"dataPoint": date_tm, "paramType": 'Sensor2', "paramValue": randNum2 ,  "deviceId" :"661526019560586"})

time.sleep(1)



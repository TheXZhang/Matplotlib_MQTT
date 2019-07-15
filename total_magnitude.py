import numpy as np
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading
import time
from matplotlib import style

temp="0"
temp_value=0
fig=plt.figure()
plt.ylim(0,10)


def setup_mqtt():
	client=mqtt.Client("graph")
	client.on_connect=OnConnect
	client.on_message=OnMessage
	client.connect("192.168.4.1",1883,120)
	return client

def OnConnect(client,userdata,flags,rc):
	#client.subscribe("test1/message")
	client.subscribe("test/accdata1")
	
		
	
def OnMessage(client,userdata,msg):
    global temp
    
    if msg.topic =="test/accdata1":
        temp=msg.payload.decode()

    
def assign_value():
    global temp_value
    global temp
    while True:
        temp_value=float(temp)
        time.sleep(1)

    

def animate(i):
    global value
    global label
    global temp_value
    global heading
    plt.clf()
    plt.ylim(0,10)
    plt.bar(['Magnitude'],temp_value)
    
while True:
    try:
        client = setup_mqtt()
        client.loop_start()
        print("mqtt connected")
        break
    except:
        print("Still waiting for mqtt connection")
        time.sleep(1)

assign_ = threading.Thread(target=assign_value,daemon=True)
assign_.start()

ani= animation.FuncAnimation(fig, animate,interval=500)
plt.show()

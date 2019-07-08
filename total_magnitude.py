import numpy as np
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

temp_value=0
fig=plt.figure()
style.use('fivethirtyeight')
plt.ylim(0,1)
base=247.5
heading=0
roll=0
pitch=0

def setup_mqtt():
	client=mqtt.Client("graph")
	client.on_connect=OnConnect
	client.on_message=OnMessage
	client.connect("192.168.5.1",1883,120)
	return client

def OnConnect(client,userdata,flags,rc):
	client.subscribe("test1/message")
	client.subscribe("test/accdata")
	
		
	
def OnMessage(client,userdata,msg):
    global temp_value

    if msg.topic =="test1/message":
        temp_value=(int(msg.payload.decode()))
    if msg.topic =="test/accdata":
        temp_list=msg.payload.decode().split()
        print(temp_list)
        temp_list[0]
        calculate(temp_list)

    

def animate(i):
    global value
    global label
    global temp_value
    global heading
    np.multiply(heading,2)
    plt.clf()
    plt.ylim(0,1)
    plt.bar(['Magnitude'],temp_value)        

client = setup_mqtt()
client.loop_start()  

ani= animation.FuncAnimation(fig, animate,interval=500)
plt.show()

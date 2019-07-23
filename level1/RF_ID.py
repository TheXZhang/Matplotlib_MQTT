import numpy as np
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading
import time


def setup_mqtt():
	client=mqtt.Client("graph")
	client.on_connect=OnConnect
	client.on_message=OnMessage
	client.connect("192.168.4.1",1883,120)
	return client

def OnConnect(client,userdata,flags,rc):
	#client.subscribe("test1/message")
	client.subscribe("sensor/RFID/raw")
		
	
def OnMessage(client,userdata,msg)
    
    if msg.topic =="sensor/RFID/raw":

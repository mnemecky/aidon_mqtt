#!/usr/bin/python

import serial
import time
import sys
import os
import paho.mqtt.client as mqtt
from aidon_obis import *

# Read env variables
mqtt_host = os.getenv("MQTT_HOST") or "localhost"
mqtt_topic = os.getenv("MQTT_TOPIC") or "/aidon"
mqtt_client = os.getenv("MQTT_CLIENT") or "aidon"
serial_port = os.getenv("SERIAL") or "/dev/ttyUSB0"

ser = serial.Serial(serial_port, 2400, timeout=0.05, parity=serial.PARITY_NONE)
print('opened serial port %s' % serial_port)

mqtt = mqtt.Client(mqtt_client)
mqtt.connect(mqtt_host)
print('MQTT connected to %s, using topic %s' % (mqtt_host, mqtt_topic) )

def aidon_callback(fields):
  ts = time.time()

  if 'p_act_in' in fields:
    mqtt.publish(mqtt_topic + '/p_act_in', (fields['p_act_in']/1000.0))

  if ('il1' in fields):
    mqtt.publish(mqtt_topic + '/ul1', fields['ul1'])
    mqtt.publish(mqtt_topic + '/ul2', fields['ul2'])
    mqtt.publish(mqtt_topic + '/ul3', fields['ul3'])
    mqtt.publish(mqtt_topic + '/il1', fields['il1'])
    mqtt.publish(mqtt_topic + '/il2', fields['il2'])

  if 'energy_act_in' in fields:
    mqtt.publish(mqtt_topic + '/energy', fields['energy_act_in'])

a = aidon(aidon_callback)
				
while(1):
  while ser.inWaiting():
    a.decode(ser.read(1))
  time.sleep(0.01)


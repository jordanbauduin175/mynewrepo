#!/usr/local/bin/env python
#Script created by Rutger Bockholts and is provided on https://rutg3r.com for free.
#Version 1.0 // 19-08-2018
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from urllib.request import urlopen
import datetime
import logging
import time
# = GPIO 4 = 
TrackingPin = 37
message="1"

def button_callback(channel):
   datetime.datetime.now().strftime("%a, %d %B %Y %H:%M:%S")
   print(datetime.datetime.now())
   print("New pulse detected")
   #url = "http://homeseer-ip:port/JSON?request=runevent&group=Energy&name=Watercounter"
   #f =  urlopen(url)
   #print(f.read())
   logging.info(msg=time.time_ns())
# logging is prepared to be ingested by influx
logging.basicConfig(filename='/code/water_conso.log', filemode='a', format='water,location=home quantity=1 %(msg)s', level=logging.INFO)

#GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(TrackingPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin TrackingPin to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(TrackingPin,GPIO.RISING,callback=button_callback) # Setup event on pin TrackingPin rising edge

while True:

 pass 




GPIO.cleanup() # Clean up

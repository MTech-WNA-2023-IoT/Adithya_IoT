#Python ProgGPIO Output in Raspberry Pi
#Import GPIO Library
import RPi.GPIO as GPIO
#Import time function Library
import time
#Configure GPIO in Raspberry Pi BCM Mode
GPIO.setmode(GPIO.BCM) 
#Configure GPIO Pin 17 as output
GPIO.setup(17,GPIO.OUT) 
#Set GPIO Pin to High
GPIO.output(17,GPIO.HIGH)
#Wait for 1sec
time.sleep(0.3)
#Set GPIO Pin to Low
GPIO.output(17,GPIO.LOW)
time.sleep(0.5)
GPIO.output(17,GPIO.HIGH)
time.sleep(0.3)
GPIO.output(17,GPIO.LOW)
time.sleep(0.5)
GPIO.output(17,GPIO.HIGH)
time.sleep(0.3)
GPIO.output(17,GPIO.LOW)
time.sleep(0.5)
GPIO.output(17,GPIO.HIGH)
time.sleep(0.7)
GPIO.output(17,GPIO.LOW)
time.sleep(0.5)
GPIO.output(17,GPIO.HIGH)
time.sleep(0.7)
GPIO.output(17,GPIO.LOW)
time.sleep(0.5)
GPIO.output(17,GPIO.HIGH)
time.sleep(0.7)
GPIO.output(17,GPIO.LOW)

#Python ProgGPIO Output in Raspberry Pi
#Import GPIO Library
import RPi.GPIO as GPIO
#Import time function Library
import time
#Configure GPIO in Raspberry Pi BCM Mode
GPIO.setmode(GPIO.BCM) 
#Configure GPIO Pin 17 as output
GPIO.setup(17,GPIO.OUT) 
a=0
while a<=5:
  GPIO.output(17,GPIO.HIGH)
  time.sleep(1)
  GPIO.output(17,GPIO.LOW)
  time.sleep(1)
  a+=1

  

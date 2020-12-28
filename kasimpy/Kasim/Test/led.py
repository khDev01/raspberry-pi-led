#!/user/bin/env python
import RPi.GPIO as GPIO
import time

LedPin = 11 # 6 from top left

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LedPin, GPIO.OUT)
GPIO.output(LedPin, GPIO.HIGH)

try:
    while True:
        print ('Led on !!!')
        GPIO.output(LedPin, GPIO.LOW)   #led on
        time.sleep(0.5)
        print ('off')
        GPIO.output(LedPin, GPIO.HIGH)  #led off
        time.sleep(0.5)
except KeyboardInterrupt:   #ctrl+c
    GPIO.output(LedPin, GPIO.HIGH)
    GPIO.cleanup()
    
    # used 2x110ohm
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)




led = 4
right_button = 15
left_button = 14


GPIO.setup(led, GPIO.OUT)
GPIO.setup(right_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(left_button, GPIO.IN, GPIO.PUD_UP)




#print "light up the LED "
GPIO.output(led, 1)

time.sleep(5)

#print "stop the light"
GPIO.output(led, 0)



while True:
    if GPIO.input(left_button) == False:
       print "Left button pressed"
       break
    if GPIO.input(right_button) == False:
       print "Right button pressed"
       break








from gpiozero import RGBLED
from time import sleep

led = RGBLED(17,18,27,active_high=False)

#(R,G,B)
led.color = (1,0,0) #red
print ("red")
sleep(1)
led.color = (0,1,0) #green
print ("green")
sleep(1)
led.color = (0,0,1) #blue
print ("blue")
sleep(1)
led.color = (1,0,1) #purple
print ("purple")
sleep(1)
led.color = (1,1,0) #light green
print ("light green")
led.off()

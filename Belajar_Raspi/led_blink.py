import RPi.GPIO as pin
from time import sleep

LED_PIN = [17, 18, 24, 25, 5, 6, 16, 23, 22, 12, 20, 19, 4, 27, 21, 13, 26]
BLINK_DELAY = 0.2 


pin.setwarnings(Falsec)
pin.setmode(pin.BCM)
pin.setup(LED_PIN, pin.OUT)

try:
    while True:
        for i in range(len(LED_PIN)):
            pin.output(LED_PIN[i], pin.HIGH)  
            sleep(BLINK_DELAY)             
            pin.output(LED_PIN[i], pin.LOW)   
            sleep(BLINK_DELAY)             
except KeyboardInterrupt:
    
    print("Stop program.")
finally:
    pin.cleanup()  

import RPi.GPIO as GPIO
import time

ENCODER_A = 17
ENCODER_B = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(ENCODER_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ENCODER_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)

encoder_value = 0
last_A = GPIO.input(ENCODER_A)

def encoder_callback(channel):
    global encoder_value, last_A
    A = GPIO.input(ENCODER_A)
    B = GPIO.input(ENCODER_B)
    
    if (A == GPIO.HIGH) != (B == GPIO.LOW):
        encoder_value -= 1
    else:
        encoder_value += 1

    last_A = A


GPIO.add_event_detect(ENCODER_A, GPIO.BOTH, callback=encoder_callback)
GPIO.add_event_detect(ENCODER_B, GPIO.BOTH, callback=encoder_callback)

try:
    while True:
        
        current_time = time.time()
        time.sleep(1)  
        rpm = (encoder_value * 60) / 2000  
        encoder_value = 0  
        print(f"RPM: {rpm}")

except KeyboardInterrupt:
    
    GPIO.cleanup()

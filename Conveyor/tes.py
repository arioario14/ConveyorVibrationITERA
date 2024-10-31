import RPi.GPIO as GPIO
import time

PUL_PIN = 18 # Pulse
DIR_PIN = 12  # Direction

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PUL_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)

direction = [GPIO.HIGH, GPIO.LOW]

GPIO.output(DIR_PIN, GPIO.LOW); 

def set_stepper_speed(speed):
    delay = 1 / speed  
    while True:
        GPIO.output(PUL_PIN, GPIO.HIGH)
        time.sleep(delay / 2)
        GPIO.output(PUL_PIN, GPIO.LOW)
        time.sleep(delay / 2)

try:
    speed = 1500  
    set_stepper_speed(speed)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

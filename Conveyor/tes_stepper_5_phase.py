import RPi.GPIO as GPIO
import time

# Setup
CW_PIN = 12 
CCW_PIN = 13
ResPin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(ResPin, GPIO.OUT)
GPIO.setup(CW_PIN, GPIO.OUT)
GPIO.output(ResPin, GPIO.HIGH)

def set_motor_speed(pulse_frequency):
    period = 1.0 / pulse_frequency
    while True:
        GPIO.output(CW_PIN, GPIO.HIGH)
        time.sleep(period / 2)
        GPIO.output(CW_PIN, GPIO.LOW)
        time.sleep(period / 2)

set_motor_speed(3000) #set 500 - 3000

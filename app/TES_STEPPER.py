import RPi.GPIO as GPIO
import time

# GPIO pin setup
DIR_PIN = 16    
STEP_PIN = 20   
EN_PIN = 21    

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(EN_PIN, GPIO.OUT)

# Enable the motor driver
GPIO.output(EN_PIN, GPIO.LOW)

def step_motor(steps, direction, delay=0.00005):
    GPIO.output(DIR_PIN, direction)
    for _ in range(steps):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(delay)  # Control speed here
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(delay)

try:
    # Step the motor 200 steps forward
    while True:
        step_motor(1000, GPIO.LOW, delay=(0.1))  # Increase delay if needed

finally:
    GPIO.output(EN_PIN, GPIO.HIGH)  # Disable the motor driver
    GPIO.cleanup()

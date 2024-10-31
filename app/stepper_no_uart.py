import RPi.GPIO as GPIO
import time

class StepperMotor:
    def __init__(self, dir_pin, step_pin, en_pin):
        self.DIR_PIN = dir_pin
        self.STEP_PIN = step_pin
        self.EN_PIN = en_pin
        
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.DIR_PIN, GPIO.OUT)
        GPIO.setup(self.STEP_PIN, GPIO.OUT)
        GPIO.setup(self.EN_PIN, GPIO.OUT)

        GPIO.output(self.EN_PIN, GPIO.LOW)

    def step_motor(self, steps, direction, delay=0.00001):
        GPIO.output(self.DIR_PIN, direction)
        for _ in range(steps):
            GPIO.output(self.STEP_PIN, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(self.STEP_PIN, GPIO.LOW)
            time.sleep(delay)

    def cleanup(self):
        GPIO.output(self.EN_PIN, GPIO.HIGH) 
        GPIO.cleanup()

if __name__ == "__main__":
    motor = StepperMotor(dir_pin=16, step_pin=20, en_pin=21)
    
    try:
        # Step the motor 1000 steps forward with a delay of 0.1 seconds
        while True:
            motor.step_motor(1000, GPIO.LOW, delay=0.00001)

    finally:
        motor.cleanup()

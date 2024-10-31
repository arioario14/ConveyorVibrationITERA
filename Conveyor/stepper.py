import RPi.GPIO as GPIO
import time

class StepperController:
    def __init__(self, cw_pin, ccw_pin, res_pin):
        self.cw_pin = cw_pin
        self.ccw_pin = ccw_pin
        self.res_pin = res_pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.res_pin, GPIO.OUT)
        GPIO.setup(self.cw_pin, GPIO.OUT)
        GPIO.setup(self.ccw_pin, GPIO.OUT)
    
        GPIO.output(self.res_pin, GPIO.HIGH)

    def set_stepper_speed(self, pulse_frequency, direction="CW"):
        period = 1.0 / pulse_frequency
        pin = self.cw_pin if direction.upper() == "CW" else self.ccw_pin
        
#         while True:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(period / 2)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(period / 2)

    def cleanup(self):
        GPIO.cleanup()


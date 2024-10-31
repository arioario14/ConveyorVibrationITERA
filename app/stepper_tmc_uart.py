import RPi.GPIO as GPIO
import time
import serial
import os

class TMC2208:
    def __init__(self, uart_port, baudrate, en_pin, dir_pin, step_pin):
        self.uart = serial.Serial(uart_port, baudrate=baudrate, timeout=1)
        self.en_pin = en_pin
        self.dir_pin = dir_pin
        self.step_pin = step_pin
        
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.en_pin, GPIO.OUT)
        GPIO.setup(self.dir_pin, GPIO.OUT)
        GPIO.setup(self.step_pin, GPIO.OUT)
        
        GPIO.output(self.en_pin, GPIO.LOW)

    def send_command(self, cmd):
        self.uart.write(cmd.encode() + b'\n')
        response = self.uart.readline()
        return response

    def set_microstep_mode(self, mode):
        cmd = 'V{}'.format(mode)
        self.send_command(cmd)

    # Mengatur arah motor (0: reverse, 1: forward)
    def set_direction(self, direction):
        GPIO.output(self.dir_pin, direction)

    def step(self, steps, delay_s):
        for _ in range(steps):
            GPIO.output(self.step_pin, GPIO.HIGH)
            time.sleep(delay_s)
            GPIO.output(self.step_pin, GPIO.LOW)
            time.sleep(delay_s)

    def disable_driver(self):
        GPIO.output(self.en_pin, GPIO.HIGH)  # EN_PIN high untuk menonaktifkan driver

    def cleanup(self):
        GPIO.output(self.en_pin, GPIO.HIGH)  # Pastikan driver dinonaktifkan
        GPIO.cleanup()

# if __name__ == "__main__":
#     
#     os.system("sudo usermod -a -G dialout pi")
#     os.system("sudo chmod 660 /dev/serial0")
#     
#     motor = TMC2208(uart_port='/dev/serial0', baudrate=115200, en_pin=21, dir_pin=16, step_pin=20)
# 
#     try:
#         
#         while True:
#             motor.set_direction(1)  # Set arah maju
#             delay = 0.1 / 10000000
#             motor.step(steps=10000, delay_s=delay)
#             
# 
#     finally:
#         motor.cleanup()

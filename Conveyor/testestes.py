import RPi.GPIO as GPIO
import time

# Setup
CW_PIN = 12  # Example GPIO pin number for CW Pulse
PWM_FREQUENCY = 200000  # Frequency in Hz
DUTY_CYCLE = 50  # Duty cycle in percentage (0-100%)

GPIO.setmode(GPIO.BCM)
GPIO.setup(CW_PIN, GPIO.OUT)

# Initialize PWM on the pin
pwm = GPIO.PWM(CW_PIN, PWM_FREQUENCY)
pwm.start(DUTY_CYCLE)

try:
    while True:
        # Adjust the frequency or duty cycle if needed
        time.sleep(0.1)  # Sleep for a short while

except KeyboardInterrupt:
    # Clean up on exit
    pwm.stop()
    GPIO.cleanup()

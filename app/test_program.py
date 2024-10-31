from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO
import time

class StepperMotor:
    def __init__(self, step_pin, dir_pin, en_pin):
        self.step_pin = step_pin
        self.dir_pin = dir_pin
        self.en_pin = en_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.step_pin, GPIO.OUT)
        GPIO.setup(self.dir_pin, GPIO.OUT)
        GPIO.setup(self.en_pin, GPIO.OUT)
        GPIO.output(self.en_pin, GPIO.LOW)  

    def step(self, steps, delay):
        for _ in range(steps):
            GPIO.output(self.step_pin, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(self.step_pin, GPIO.LOW)
            time.sleep(delay)

    def set_direction(self, direction):
        GPIO.output(self.dir_pin, GPIO.HIGH if direction == "CW" else GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Stepper Motor Controller")
        Form.resize(400, 300)

        self.stepper = StepperMotor(step_pin=20, dir_pin=16, en_pin=21)

        # Speed Up Button
        self.setAddSpeed = QtWidgets.QPushButton(Form)
        self.setAddSpeed.setGeometry(QtCore.QRect(10, 200, 80, 80))
        self.setAddSpeed.setText("Speed Up")
        self.setAddSpeed.clicked.connect(self.increment_speed)

        # Speed Down Button
        self.setMinSpeed = QtWidgets.QPushButton(Form)
        self.setMinSpeed.setGeometry(QtCore.QRect(100, 200, 80, 80))
        self.setMinSpeed.setText("Speed Down")
        self.setMinSpeed.clicked.connect(self.decrement_speed)

        # CW Button
        self.setCW = QtWidgets.QPushButton(Form)
        self.setCW.setGeometry(QtCore.QRect(200, 200, 80, 80))
        self.setCW.setText("CW")
        self.setCW.clicked.connect(self.set_cw)

        # CCW Button
        self.setCCW = QtWidgets.QPushButton(Form)
        self.setCCW.setGeometry(QtCore.QRect(290, 200, 80, 80))
        self.setCCW.setText("CCW")
        self.setCCW.clicked.connect(self.set_ccw)

        # Speed Display
        self.speed_display = QtWidgets.QLabel(Form)
        self.speed_display.setGeometry(QtCore.QRect(10, 10, 200, 50))
        self.speed_display.setText("Speed: 0")
        self.speed = 0

    def increment_speed(self):
        self.speed += 100
        self.speed_display.setText(f"Speed: {self.speed}")
        self.stepper.step(steps=1000, delay=1.0 / self.speed)

    def decrement_speed(self):
        if self.speed > 0:
            self.speed -= 100
            self.speed_display.setText(f"Speed: {self.speed}")

    def set_cw(self):
        self.stepper.set_direction("CW")

    def set_ccw(self):
        self.stepper.set_direction("CCW")

    def closeEvent(self, event):
        self.stepper.cleanup()
        event.accept()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
# from stepper_no_uart import StepperMotor
import RPi.GPIO as GPIO
from stepper_tmc_uart import TMC2208
import os
 



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Controls")
        Form.resize(1024, 600)
        
        os.system("sudo usermod -a -G dialout pi")
        os.system("sudo chmod 666 /dev/serial0")
        
#         self.stepper = StepperMotor(dir_pin=16, step_pin=20, en_pin=21)
        self.motor = TMC2208(uart_port='/dev/serial0', baudrate=115200, en_pin=21, dir_pin=16, step_pin=20)
        
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 301))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(80, 90, 57, 15))
        self.label.setText("")
        self.label.setObjectName("label")
        self.setAddSpeed = QtWidgets.QPushButton(self.groupBox)
        self.setAddSpeed.setEnabled(True)
        self.setAddSpeed.setGeometry(QtCore.QRect(10, 210, 80, 80))
        self.setAddSpeed.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/icons8-up-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setAddSpeed.setIcon(icon)
        self.setAddSpeed.setIconSize(QtCore.QSize(50, 50))
        self.setAddSpeed.setObjectName("setAddSpeed")
        self.setMinSpeed = QtWidgets.QPushButton(self.groupBox)
        self.setMinSpeed.setGeometry(QtCore.QRect(100, 210, 80, 80))
        self.setMinSpeed.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Downloads/icons8-down-arrow-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setMinSpeed.setIcon(icon1)
        self.setMinSpeed.setIconSize(QtCore.QSize(50, 50))
        self.setMinSpeed.setObjectName("setMinSpeed")
        self.setCW = QtWidgets.QPushButton(self.groupBox)
        self.setCW.setGeometry(QtCore.QRect(290, 210, 80, 80))
        self.setCW.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../Downloads/icons8-right-arrow-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setCW.setIcon(icon2)
        self.setCW.setIconSize(QtCore.QSize(50, 50))
        self.setCW.setObjectName("setCW")
        self.setCCW = QtWidgets.QPushButton(self.groupBox)
        self.setCCW.setGeometry(QtCore.QRect(200, 210, 80, 80))
        self.setCCW.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../Downloads/icons8-left-arrow-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setCCW.setIcon(icon3)
        self.setCCW.setIconSize(QtCore.QSize(50, 50))
        self.setCCW.setObjectName("setCCW")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(210, 50, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(40, 80, 113, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 80, 113, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setMouseTracking(False)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.MenuBox = QtWidgets.QGroupBox(Form)
        self.MenuBox.setGeometry(QtCore.QRect(880, 10, 141, 581))
        self.MenuBox.setObjectName("MenuBox")
        self.ControlsButton = QtWidgets.QPushButton(self.MenuBox)
        self.ControlsButton.setGeometry(QtCore.QRect(10, 30, 121, 111))
        self.ControlsButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../Downloads/icons8-monitoring-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ControlsButton.setIcon(icon4)
        self.ControlsButton.setIconSize(QtCore.QSize(50, 50))
        self.ControlsButton.setObjectName("ControlsButton")

        # Connect setAddSpeed button to increment method
        self.setAddSpeed.clicked.connect(self.incrementAddSpeed)
        self.setMinSpeed.clicked.connect(self.incrementMinSpeed)
        self.setCW.clicked.connect(self.directionCW)
        self.setCCW.clicked.connect(self.directionCCW)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Controls"))
        self.groupBox.setTitle(_translate("Form", "Controls Stepper"))
        self.label_2.setText(_translate("Form", "SET SPEED"))
        self.label_3.setText(_translate("Form", "SET DIRECTION"))
        self.lineEdit.setText(_translate("Form", "0"))
        self.lineEdit_2.setText(_translate("Form", "CW"))
        self.MenuBox.setTitle(_translate("Form", "Menu"))

    def incrementAddSpeed(self):
        self.speed = int(self.lineEdit.text())
        
        if self.speed >= 0:
            
            new_value = self.speed + 10
            delay = 0.1 * (new_value + 100)
            self.motor.step(steps=10000, delay_s=delay)
            self.lineEdit.setText(str(new_value))
        
    def incrementMinSpeed(self):
        self.speed = int(self.lineEdit.text())
        
        if self.speed > 0:
            new_value = self.speed - 10
            self.lineEdit.setText(str(new_value))
            
    def directionCCW(self):
        self.direction = str(self.lineEdit_2.text())
        
        if self.direction == "CW":
            new_value = "CCW"
            self.motor.set_direction(0)
            self.direction = new_value
            self.lineEdit_2.setText(new_value)
            print("set dir :" + new_value)
    
    def directionCW(self):
        self.direction = str(self.lineEdit_2.text())
        if self.direction == "CCW":
            new_value = "CW"
            self.motor.set_direction(1)
            self.direction = new_value
            self.lineEdit_2.setText(new_value)
            print("set dir :" + new_value)
            
    def set_stepper(self):
        delay = 0.1 / 10000000
        
        
        

if __name__ == "__main__":
    try:
        import sys
        import os
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()    
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
                  
            
    except KeyboardInterrupt:
        sys.exit(app.exec_())
    finally:
        ui.motor.cleanup()

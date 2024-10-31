from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.colors as mcolors
import matplotlib.cm as cm
from temp_qt_v2 import TemperaturePlotWidget, TemperatureSensor
from encoder import Encoder
from vibration import MPU6050Plotter
from Controls import Ui_Form as Ui_Controls

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Conveyor Dashboard")
        Form.resize(1024, 560)
        
#         try:
# #             self.encoder = Encoder(pin_a=23, pin_b=22)
# #             self.sensor = TemperatureSensor()
#         except IndexError:
#             pass
        
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 391, 200))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(0, 20, 391, 181))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 220, 391, 200))
        self.groupBox_2.setObjectName("groupBox_2")
        

#         self.plot_temp = TemperaturePlotWidget(self.groupBox_2)
#         self.plot_temp.setGeometry(QtCore.QRect(0, 20, 391, 181))
#         self.plot_temp.setObjectName("plot_temp")
        
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 430, 391, 161))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(220, 140, 171, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(190, 30, 57, 15))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(190, 60, 57, 15))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(190, 90, 57, 15))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(10, 90, 91, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(80, 30, 71, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(80, 60, 71, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(100, 90, 71, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(230, 90, 151, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(230, 60, 151, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(230, 30, 151, 16))
        self.label_14.setObjectName("label_14")
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(410, 10, 451, 581))
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 30, 431, 177))
        self.groupBox_5.setObjectName("groupBox_5")
#         self.plot_vibration = MPU6050Plotter(self.groupBox_5)
#         self.plot_vibration.setGeometry(QtCore.QRect(0, 20, 431, 161))
#         self.plot_vibration.setStyleSheet("background-color: rgb(0, 0, 0);")
#         self.plot_vibration.setObjectName("plot_vibration")

        # Initialize the MPU6050 plotter
#         self.plotter = MPU6050Plotter(self.plot_vibration)

        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 210, 431, 175))
        self.groupBox_6.setObjectName("groupBox_6")
#         self.plot_vb2 = MPU6050Plotter(self.groupBox_6)
#         self.plot_vb2.setGeometry(QtCore.QRect(0, 20, 431, 161))
#         self.plot_vb2.setStyleSheet("background-color: rgb(0, 0, 0);")
#         self.plot_vb2.setObjectName("plot_vb2")
        
#         self.plotter = MPU6050Plotter(self.groupBox_6)
        
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 390, 431, 175))
        self.groupBox_7.setObjectName("groupBox_7")
        
#         self.plot_vb3 = MPU6050Plotter(self.groupBox_7)
#         self.plot_vb3.setGeometry(QtCore.QRect(0, 20, 431, 161))
#         self.plot_vb3.setStyleSheet("background-color: rgb(0, 0, 0);")
#         self.plot_vb3.setObjectName("plot_vb3")
        self.MenuBox = QtWidgets.QGroupBox(Form)
        self.MenuBox.setGeometry(QtCore.QRect(870, 9, 141, 581))
        self.MenuBox.setObjectName("MenuBox")
        self.ControlsButton = QtWidgets.QPushButton(self.MenuBox)
        self.ControlsButton.setGeometry(QtCore.QRect(10, 30, 121, 111))
        self.ControlsButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/icons8-setting-200.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../../Downloads/icons8-setting-200.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../../Downloads/icons8-setting-200.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.ControlsButton.setIcon(icon)
        self.ControlsButton.setIconSize(QtCore.QSize(50, 50))
        self.ControlsButton.setObjectName("ControlsButton")
        
        self.timer = QtCore.QTimer()
#         self.timer.timeout.connect(self.update_rpm)
#         self.timer.timeout.connect(self.get_accel)
        self.timer.start(500)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Conveyor Dashboard"))
        self.groupBox.setTitle(_translate("Form", "RPM"))
        
        self.groupBox_2.setTitle(_translate("Form", "Temperature"))
        self.groupBox_3.setTitle(_translate("Form", "Status"))
        self.label_2.setText(_translate("Form", "Sunday, 1/9/2024 18:14:30"))
        self.label_3.setText(_translate("Form", "Speed     :"))
        self.label_4.setText(_translate("Form", "Direction :"))
        self.label_5.setText(_translate("Form", "vb1 :"))
        self.label_6.setText(_translate("Form", "vb2 :"))
        self.label_7.setText(_translate("Form", "vb3 :"))
        self.label_8.setText(_translate("Form", "Temperature :"))
        self.label_9.setText(_translate("Form", "0"))
        self.label_10.setText(_translate("Form", "CCW"))
#         self.label_11.setText(_translate("Form", str(self.sensor.read_temp()) + "°C"))
        self.label_12.setText(_translate("Form", "X, Y, Z"))
        self.label_13.setText(_translate("Form", "X, Y, Z"))
        self.label_14.setText(_translate("Form", "X, Y, Z"))
        self.groupBox_4.setTitle(_translate("Form", "Vibration"))
        self.groupBox_5.setTitle(_translate("Form", "Vibration 1"))
        self.groupBox_6.setTitle(_translate("Form", "Vibration 2"))
        self.groupBox_7.setTitle(_translate("Form", "Vibration 3"))
        self.MenuBox.setTitle(_translate("Form", "Menu"))
        
        self.ControlsButton.clicked.connect(self.open_second_window)
    
    def center(self, Form):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = Form.geometry()
        x = (screen.width() - size.width()) // 2
        y = (screen.height() - size.height()) // 2
        Form.move(x, y)
        
    def open_second_window(self):
        self.second_window = QtWidgets.QWidget()  
        self.ui = Ui_Controls()  
        self.ui.setupUi(self.second_window)  
        self.second_window.show() 
        
#     def update_rpm(self):
#         self.label.setText(str(self.encoder.calculate_rpm()) + " RPM")
#     
#     def get_accel(self):
#         self.x_acc, self.y_acc, self.z_acc = self.plot_vibration.read_accel_data()
#     
#         self.label_12.setText(f"X : {self.x_acc:.2f}, Y : {self.y_acc:.2f}, Z : {self.z_acc:.2f}")
#         self.label_13.setText(f"X : {self.x_acc:.2f}, Y : {self.y_acc:.2f}, Z : {self.z_acc:.2f}")
#         self.label_14.setText(f"X : {self.x_acc:.2f}, Y : {self.y_acc:.2f}, Z : {self.z_acc:.2f}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    ui.center(Form)
    Form.show()
    sys.exit(app.exec_())

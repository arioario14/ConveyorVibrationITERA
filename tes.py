from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 600)
        
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

        # Replace plot_temp with a MplCanvas widget
        self.plot_temp = MplCanvas(self.groupBox_2, width=3.9, height=1.8, dpi=100)
        self.plot_temp.setGeometry(QtCore.QRect(0, 20, 391, 181))
        self.plot_temp.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.plot_temp.setObjectName("plot_temp")

        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 430, 391, 161))
        self.groupBox_3.setObjectName("groupBox_3")
        
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(410, 10, 451, 581))
        self.groupBox_4.setObjectName("groupBox_4")
        
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 30, 431, 177))
        self.groupBox_5.setObjectName("groupBox_5")
        
        self.plot_vb1 = QtWidgets.QWidget(self.groupBox_5)
        self.plot_vb1.setGeometry(QtCore.QRect(0, 20, 431, 161))
        self.plot_vb1.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.plot_vb1.setObjectName("plot_vb1")
        
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 210, 431, 175))
        self.groupBox_6.setObjectName("groupBox_6")
        
        self.plot_vb2 = QtWidgets.QWidget(self.groupBox_6)
        self.plot_vb2.setGeometry(QtCore.QRect(0, 20, 431, 161))
        self.plot_vb2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.plot_vb2.setObjectName("plot_vb2")
        
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 390, 431, 175))
        self.groupBox_7.setObjectName("groupBox_7")
        
        self.plot_vb3 = QtWidgets.QWidget(self.groupBox_7)
        self.plot_vb3.setGeometry(QtCore.QRect(0, 20, 431, 161))
        self.plot_vb3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.plot_vb3.setObjectName("plot_vb3")
        
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "RPM"))
        self.label.setText(_translate("Form", "0 RPM"))
        self.groupBox_2.setTitle(_translate("Form", "Temperature"))
        self.groupBox_3.setTitle(_translate("Form", "Status"))
        self.groupBox_4.setTitle(_translate("Form", "Vibration"))
        self.groupBox_5.setTitle(_translate("Form", "Vibration 1"))
        self.groupBox_6.setTitle(_translate("Form", "Vibration 2"))
        self.groupBox_7.setTitle(_translate("Form", "Vibration 3"))
        self.MenuBox.setTitle(_translate("Form", "Menu"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

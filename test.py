import sys
from PySide6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(732, 538)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 30, 731, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 120, 711, 161))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(0, 496, 731, 20))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(711, 0, 20, 501))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(0, 280, 711, 211))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.spinBox.setFont(font)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinBox.setObjectName("spinBox")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 90, 711, 31))
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 100)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.Direction.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 732, 22))
        self.menubar.setObjectName("menubar")
        self.menuF = QtWidgets.QMenu(self.menubar)
        self.menuF.setObjectName("menuF")
        self.menuRE = QtWidgets.QMenu(self.menuF)
        self.menuRE.setObjectName("menuRE")
        self.menuRE1_2 = QtWidgets.QMenu(self.menuRE)
        self.menuRE1_2.setObjectName("menuRE1_2")
        self.menuRE_2 = QtWidgets.QMenu(self.menuF)
        self.menuRE_2.setObjectName("menuRE_2")
        self.menuRE1 = QtWidgets.QMenu(self.menuRE_2)
        self.menuRE1.setObjectName("menuRE1")
        MainWindow.setMenuBar(self.menubar)
        self.actionRE2 = QtWidgets.QWidgetAction(MainWindow)
        self.actionRE2.setObjectName("actionRE2")
        self.actionRE2_2 = QtWidgets.QWidgetAction(MainWindow)
        self.actionRE2_2.setObjectName("actionRE2_2")
        self.menuRE1_2.addAction(self.actionRE2_2)
        self.menuRE.addAction(self.menuRE1_2.menuAction())
        self.menuRE1.addAction(self.actionRE2)
        self.menuRE_2.addAction(self.menuRE1.menuAction())
        self.menuF.addAction(self.menuRE_2.menuAction())
        self.menuF.addAction(self.menuRE.menuAction())
        self.menubar.addAction(self.menuF.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ГЛАВНОЕ ОКНО"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Пишите..."))
        self.menuF.setTitle(_translate("MainWindow", "F"))
        self.menuRE.setTitle(_translate("MainWindow", "RE"))
        self.menuRE1_2.setTitle(_translate("MainWindow", "RE1"))
        self.menuRE_2.setTitle(_translate("MainWindow", "RE"))
        self.menuRE1.setTitle(_translate("MainWindow", "RE1"))
        self.actionRE2.setText(_translate("MainWindow", "RE2"))
        self.actionRE2_2.setText(_translate("MainWindow", "RE2"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    splash = QtWidgets.QSplashScreen()
    # splash.setPixmap(QtGui.QPixmap('images/splash.jpg'))
    splash.show()
    splash.showMessage('<p style="color:black;">Добро пожаловать в этот заставка, сделанная в PyQt5</p>', 
                       QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter, QtCore.Qt.white)    

    QtCore.QThread.msleep(5000)   # 

    demo = MainWindow()
    demo.show()
    splash.finish(demo)

    sys.exit(app.exec_())
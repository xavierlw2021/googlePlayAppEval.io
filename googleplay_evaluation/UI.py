# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(885, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(330, 10, 241, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(10, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.url_input = QtWidgets.QTextEdit(self.centralwidget)
        self.url_input.setGeometry(QtCore.QRect(150, 50, 711, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.url_input.setFont(font)
        self.url_input.setObjectName("url_input")
        self.label_ver = QtWidgets.QLabel(self.centralwidget)
        self.label_ver.setGeometry(QtCore.QRect(830, 10, 47, 12))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.label_ver.setFont(font)
        self.label_ver.setObjectName("label_ver")
        self.callback_pageNumber = QtWidgets.QLabel(self.centralwidget)
        self.callback_pageNumber.setGeometry(QtCore.QRect(170, 180, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.callback_pageNumber.setFont(font)
        self.callback_pageNumber.setText("")
        self.callback_pageNumber.setObjectName("callback_pageNumber")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 160, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.result_number = QtWidgets.QLineEdit(self.centralwidget)
        self.result_number.setGeometry(QtCore.QRect(150, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setItalic(True)
        self.result_number.setFont(font)
        self.result_number.setObjectName("result_number")
        self.btn_createCSV = QtWidgets.QPushButton(self.centralwidget)
        self.btn_createCSV.setGeometry(QtCore.QRect(390, 120, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_createCSV.setFont(font)
        self.btn_createCSV.setObjectName("btn_createCSV")
        self.label_infomation = QtWidgets.QLabel(self.centralwidget)
        self.label_infomation.setGeometry(QtCore.QRect(140, 160, 581, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.label_infomation.setFont(font)
        self.label_infomation.setText("")
        self.label_infomation.setObjectName("label_infomation")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 885, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Google Play app評價收集"))
        self.label_1.setText(_translate("MainWindow", "app下載頁面網址:"))
        self.label_2.setText(_translate("MainWindow", "搜尋筆數:"))
        self.label_ver.setText(_translate("MainWindow", "ver. 0.1"))
        self.label_3.setText(_translate("MainWindow", "訊息:"))
        self.result_number.setText(_translate("MainWindow", "100"))
        self.btn_createCSV.setText(_translate("MainWindow", "生成CSV"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lenovo\Dropbox\PYAPPS_STRUCT\SOURCE_SINOPE\source\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1426, 864)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_output = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_output.setGeometry(QtCore.QRect(180, 130, 1111, 681))
        font = QtGui.QFont()
        font.setFamily("ISOCTEUR")
        font.setPointSize(9)
        self.textBrowser_output.setFont(font)
        self.textBrowser_output.setObjectName("textBrowser_output")
        self.plainTextEdit_serch = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_serch.setGeometry(QtCore.QRect(10, 100, 161, 341))
        font = QtGui.QFont()
        font.setFamily("ISOCPEUR")
        font.setPointSize(8)
        self.plainTextEdit_serch.setFont(font)
        self.plainTextEdit_serch.setObjectName("plainTextEdit_serch")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.label.setObjectName("label")
        self.pushButton_check = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_check.setGeometry(QtCore.QRect(10, 510, 161, 23))
        self.pushButton_check.setObjectName("pushButton_check")
        self.pushButton_load = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_load.setGeometry(QtCore.QRect(20, 40, 141, 23))
        self.pushButton_load.setObjectName("pushButton_load")
        self.pushButton_Sort = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Sort.setGeometry(QtCore.QRect(10, 450, 161, 23))
        self.pushButton_Sort.setObjectName("pushButton_Sort")
        self.pushButton_getMembers = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_getMembers.setGeometry(QtCore.QRect(10, 480, 161, 23))
        self.pushButton_getMembers.setObjectName("pushButton_getMembers")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(190, 90, 291, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_Report = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_Report.setObjectName("pushButton_Report")
        self.horizontalLayout_2.addWidget(self.pushButton_Report)
        self.checkBox_full = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_full.setChecked(False)
        self.checkBox_full.setObjectName("checkBox_full")
        self.horizontalLayout_2.addWidget(self.checkBox_full)
        self.pushButton_info = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_info.setGeometry(QtCore.QRect(1300, 190, 93, 29))
        self.pushButton_info.setObjectName("pushButton_info")
        self.pushButton_print = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_print.setGeometry(QtCore.QRect(1300, 150, 91, 29))
        self.pushButton_print.setObjectName("pushButton_print")
        self.pushButton_find_by_type = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_find_by_type.setGeometry(QtCore.QRect(10, 560, 161, 23))
        self.pushButton_find_by_type.setObjectName("pushButton_find_by_type")
        self.comboBox_Type = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Type.setGeometry(QtCore.QRect(10, 590, 161, 26))
        self.comboBox_Type.setObjectName("comboBox_Type")
        self.checkBox_minFx = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_minFx.setEnabled(True)
        self.checkBox_minFx.setGeometry(QtCore.QRect(1300, 100, 66, 24))
        self.checkBox_minFx.setObjectName("checkBox_minFx")
        self.checkBox_maxabsFx = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_maxabsFx.setEnabled(True)
        self.checkBox_maxabsFx.setGeometry(QtCore.QRect(1300, 40, 77, 24))
        self.checkBox_maxabsFx.setChecked(True)
        self.checkBox_maxabsFx.setObjectName("checkBox_maxabsFx")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1296, 21, 102, 20))
        self.label_5.setObjectName("label_5")
        self.checkBox_maxFx = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_maxFx.setEnabled(True)
        self.checkBox_maxFx.setGeometry(QtCore.QRect(1300, 70, 69, 24))
        self.checkBox_maxFx.setObjectName("checkBox_maxFx")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 20, 29, 20))
        self.label_2.setObjectName("label_2")
        self.checkBox_pltAnnot = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_pltAnnot.setGeometry(QtCore.QRect(900, 20, 127, 24))
        self.checkBox_pltAnnot.setChecked(False)
        self.checkBox_pltAnnot.setObjectName("checkBox_pltAnnot")
        self.comboBox_pltComb = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_pltComb.setGeometry(QtCore.QRect(550, 20, 131, 26))
        self.comboBox_pltComb.setObjectName("comboBox_pltComb")
        self.pushButton_pltForces = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pltForces.setGeometry(QtCore.QRect(690, 20, 93, 29))
        self.pushButton_pltForces.setObjectName("pushButton_pltForces")
        self.pushButton_pltMoments = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pltMoments.setGeometry(QtCore.QRect(790, 20, 101, 29))
        self.pushButton_pltMoments.setObjectName("pushButton_pltMoments")
        self.comboBox_method = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_method.setGeometry(QtCore.QRect(300, 50, 181, 26))
        self.comboBox_method.setObjectName("comboBox_method")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 50, 91, 20))
        self.label_3.setObjectName("label_3")
        self.checkBox_method_max = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_method_max.setGeometry(QtCore.QRect(520, 70, 127, 24))
        self.checkBox_method_max.setChecked(False)
        self.checkBox_method_max.setObjectName("checkBox_method_max")
        self.checkBox_method_min = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_method_min.setGeometry(QtCore.QRect(630, 70, 101, 24))
        self.checkBox_method_min.setChecked(False)
        self.checkBox_method_min.setObjectName("checkBox_method_min")
        self.checkBox_method_abs = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_method_abs.setGeometry(QtCore.QRect(740, 70, 101, 24))
        self.checkBox_method_abs.setChecked(False)
        self.checkBox_method_abs.setObjectName("checkBox_method_abs")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1426, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actionLoadXLS = QtWidgets.QAction(MainWindow)
        self.actionLoadXLS.setEnabled(True)
        self.actionLoadXLS.setObjectName("actionLoadXLS")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "gismo"))
        self.textBrowser_output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'ISOCTEUR\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">a---as</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">0-----</span></p></body></html>"))
        self.plainTextEdit_serch.setPlainText(_translate("MainWindow", "AG1\n"
"AG5"))
        self.label.setText(_translate("MainWindow", "Point list:"))
        self.pushButton_check.setText(_translate("MainWindow", "check list"))
        self.pushButton_load.setText(_translate("MainWindow", "Load excel data"))
        self.pushButton_Sort.setText(_translate("MainWindow", "sort list"))
        self.pushButton_getMembers.setText(_translate("MainWindow", "get all points"))
        self.pushButton_Report.setText(_translate("MainWindow", "GET REPORT"))
        self.checkBox_full.setText(_translate("MainWindow", "long report"))
        self.pushButton_info.setText(_translate("MainWindow", "App info"))
        self.pushButton_print.setText(_translate("MainWindow", "Print report"))
        self.pushButton_find_by_type.setText(_translate("MainWindow", "find all by types"))
        self.checkBox_minFx.setText(_translate("MainWindow", "minFx"))
        self.checkBox_maxabsFx.setText(_translate("MainWindow", "max|Fx|"))
        self.label_5.setText(_translate("MainWindow", "Report content:"))
        self.checkBox_maxFx.setText(_translate("MainWindow", "maxFx"))
        self.label_2.setText(_translate("MainWindow", "Plot:"))
        self.checkBox_pltAnnot.setText(_translate("MainWindow", "plot annotation"))
        self.pushButton_pltForces.setText(_translate("MainWindow", "3D forces"))
        self.pushButton_pltMoments.setText(_translate("MainWindow", "3D moments"))
        self.label_3.setText(_translate("MainWindow", "Select method:"))
        self.checkBox_method_max.setText(_translate("MainWindow", "max values"))
        self.checkBox_method_min.setText(_translate("MainWindow", "min values"))
        self.checkBox_method_abs.setText(_translate("MainWindow", "abs values"))
        self.actionLoadXLS.setText(_translate("MainWindow", "Load xls data"))

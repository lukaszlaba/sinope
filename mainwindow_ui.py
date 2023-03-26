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
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_load = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_load.setObjectName("pushButton_load")
        self.verticalLayout.addWidget(self.pushButton_load)
        self.checkBox_line_name = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_line_name.setObjectName("checkBox_line_name")
        self.verticalLayout.addWidget(self.checkBox_line_name)
        self.pushButton_clear_data = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear_data.setObjectName("pushButton_clear_data")
        self.verticalLayout.addWidget(self.pushButton_clear_data)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.plainTextEdit_serch = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_serch.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_serch.setSizePolicy(sizePolicy)
        self.plainTextEdit_serch.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("ISOCPEUR")
        font.setPointSize(8)
        self.plainTextEdit_serch.setFont(font)
        self.plainTextEdit_serch.setObjectName("plainTextEdit_serch")
        self.verticalLayout.addWidget(self.plainTextEdit_serch)
        self.pushButton_clear_list = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear_list.setObjectName("pushButton_clear_list")
        self.verticalLayout.addWidget(self.pushButton_clear_list)
        self.pushButton_Sort = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Sort.setObjectName("pushButton_Sort")
        self.verticalLayout.addWidget(self.pushButton_Sort)
        self.pushButton_check = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_check.setObjectName("pushButton_check")
        self.verticalLayout.addWidget(self.pushButton_check)
        self.pushButton_getMembers = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_getMembers.setObjectName("pushButton_getMembers")
        self.verticalLayout.addWidget(self.pushButton_getMembers)
        self.pushButton_find_by_type = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_find_by_type.setObjectName("pushButton_find_by_type")
        self.verticalLayout.addWidget(self.pushButton_find_by_type)
        self.comboBox_Type = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Type.setObjectName("comboBox_Type")
        self.verticalLayout.addWidget(self.comboBox_Type)
        self.comboBox_Line = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Line.setObjectName("comboBox_Line")
        self.verticalLayout.addWidget(self.comboBox_Line)
        self.horizontalLayout_8.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.comboBox_method = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_method.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_method.setObjectName("comboBox_method")
        self.horizontalLayout.addWidget(self.comboBox_method)
        self.comboBox_method_value = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_method_value.setMinimumSize(QtCore.QSize(90, 0))
        self.comboBox_method_value.setObjectName("comboBox_method_value")
        self.horizontalLayout.addWidget(self.comboBox_method_value)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_Report = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Report.setObjectName("pushButton_Report")
        self.horizontalLayout_2.addWidget(self.pushButton_Report)
        self.checkBox_full = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_full.setChecked(False)
        self.checkBox_full.setObjectName("checkBox_full")
        self.horizontalLayout_2.addWidget(self.checkBox_full)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.comboBox_plt_comb = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_plt_comb.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox_plt_comb.setObjectName("comboBox_plt_comb")
        self.horizontalLayout_3.addWidget(self.comboBox_plt_comb)
        self.pushButton_plt_show = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plt_show.setObjectName("pushButton_plt_show")
        self.horizontalLayout_3.addWidget(self.pushButton_plt_show)
        self.checkBox_pltAnnot = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_pltAnnot.setChecked(False)
        self.checkBox_pltAnnot.setObjectName("checkBox_pltAnnot")
        self.horizontalLayout_3.addWidget(self.checkBox_pltAnnot)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.pushButton_dxf = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dxf.setObjectName("pushButton_dxf")
        self.horizontalLayout_4.addWidget(self.pushButton_dxf)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_print = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_print.setObjectName("pushButton_print")
        self.horizontalLayout_5.addWidget(self.pushButton_print)
        self.pushButton_info = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_info.setObjectName("pushButton_info")
        self.horizontalLayout_5.addWidget(self.pushButton_info)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.textBrowser_output = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("ISOCTEUR")
        font.setPointSize(7)
        self.textBrowser_output.setFont(font)
        self.textBrowser_output.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_output.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_output.setObjectName("textBrowser_output")
        self.verticalLayout_4.addWidget(self.textBrowser_output)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1426, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "gismo"))
        self.pushButton_load.setText(_translate("MainWindow", ">add excel data<"))
        self.checkBox_line_name.setText(_translate("MainWindow", "load line name"))
        self.pushButton_clear_data.setText(_translate("MainWindow", "clear data"))
        self.label.setText(_translate("MainWindow", "Point list:"))
        self.plainTextEdit_serch.setPlainText(_translate("MainWindow", "AG1\n"
"AG5"))
        self.pushButton_clear_list.setText(_translate("MainWindow", "clear list"))
        self.pushButton_Sort.setText(_translate("MainWindow", "sort list"))
        self.pushButton_check.setText(_translate("MainWindow", "check list"))
        self.pushButton_getMembers.setText(_translate("MainWindow", "add all available"))
        self.pushButton_find_by_type.setText(_translate("MainWindow", "add by criteria"))
        self.label_3.setText(_translate("MainWindow", "Select method:"))
        self.pushButton_Report.setText(_translate("MainWindow", "GET REPORT"))
        self.checkBox_full.setText(_translate("MainWindow", "long report"))
        self.label_2.setText(_translate("MainWindow", "3D Plot:"))
        self.pushButton_plt_show.setText(_translate("MainWindow", "show"))
        self.checkBox_pltAnnot.setText(_translate("MainWindow", "plot annotation"))
        self.label_4.setText(_translate("MainWindow", "Dxf output:"))
        self.pushButton_dxf.setText(_translate("MainWindow", "export"))
        self.pushButton_print.setText(_translate("MainWindow", "Print report"))
        self.pushButton_info.setText(_translate("MainWindow", "App info"))
        self.textBrowser_output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'ISOCTEUR\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">a---as</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">0-----</span></p></body></html>"))

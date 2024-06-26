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
        MainWindow.resize(1651, 766)
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
        self.checkBox_purge = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_purge.setChecked(True)
        self.checkBox_purge.setObjectName("checkBox_purge")
        self.verticalLayout.addWidget(self.checkBox_purge)
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
        self.plainTextEdit_serch.setMaximumSize(QtCore.QSize(175, 16777215))
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
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.pushButton_get_from_dxf = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_get_from_dxf.setEnabled(True)
        self.pushButton_get_from_dxf.setObjectName("pushButton_get_from_dxf")
        self.verticalLayout.addWidget(self.pushButton_get_from_dxf)
        self.horizontalLayout_8.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
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
        self.pushButton_save_point = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save_point.setObjectName("pushButton_save_point")
        self.horizontalLayout_2.addWidget(self.pushButton_save_point)
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
        self.checkBox_DxfPointsOnly = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_DxfPointsOnly.setObjectName("checkBox_DxfPointsOnly")
        self.horizontalLayout_4.addWidget(self.checkBox_DxfPointsOnly)
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
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_staadGet = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_staadGet.setMinimumSize(QtCore.QSize(148, 0))
        self.pushButton_staadGet.setObjectName("pushButton_staadGet")
        self.horizontalLayout_9.addWidget(self.pushButton_staadGet)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.comboBox_staadTemplate = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_staadTemplate.setObjectName("comboBox_staadTemplate")
        self.horizontalLayout_9.addWidget(self.comboBox_staadTemplate)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.comboBox_staadLC = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_staadLC.setObjectName("comboBox_staadLC")
        self.horizontalLayout_9.addWidget(self.comboBox_staadLC)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.comboBox_staadUCS = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_staadUCS.setObjectName("comboBox_staadUCS")
        self.horizontalLayout_9.addWidget(self.comboBox_staadUCS)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.comboBox_staadUnit = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_staadUnit.setObjectName("comboBox_staadUnit")
        self.horizontalLayout_9.addWidget(self.comboBox_staadUnit)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.comboBox_staadPsasWE = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_staadPsasWE.setObjectName("comboBox_staadPsasWE")
        self.horizontalLayout_9.addWidget(self.comboBox_staadPsasWE)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_Compare = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Compare.setMinimumSize(QtCore.QSize(148, 0))
        self.pushButton_Compare.setObjectName("pushButton_Compare")
        self.horizontalLayout_10.addWidget(self.pushButton_Compare)
        self.checkBox_compare_long = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_compare_long.setChecked(True)
        self.checkBox_compare_long.setAutoRepeat(False)
        self.checkBox_compare_long.setObjectName("checkBox_compare_long")
        self.horizontalLayout_10.addWidget(self.checkBox_compare_long)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_10.addWidget(self.label_13)
        self.comboBox_tolerance_from = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_tolerance_from.setObjectName("comboBox_tolerance_from")
        self.horizontalLayout_10.addWidget(self.comboBox_tolerance_from)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_10.addWidget(self.label_14)
        self.comboBox_tolerance_to = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_tolerance_to.setObjectName("comboBox_tolerance_to")
        self.horizontalLayout_10.addWidget(self.comboBox_tolerance_to)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_10.addWidget(self.label_15)
        self.lineEdit_skip_value_lateral = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_skip_value_lateral.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_skip_value_lateral.sizePolicy().hasHeightForWidth())
        self.lineEdit_skip_value_lateral.setSizePolicy(sizePolicy)
        self.lineEdit_skip_value_lateral.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_skip_value_lateral.setObjectName("lineEdit_skip_value_lateral")
        self.horizontalLayout_10.addWidget(self.lineEdit_skip_value_lateral)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_10.addWidget(self.label_16)
        self.lineEdit_skip_value_vertical = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_skip_value_vertical.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_skip_value_vertical.sizePolicy().hasHeightForWidth())
        self.lineEdit_skip_value_vertical.setSizePolicy(sizePolicy)
        self.lineEdit_skip_value_vertical.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_skip_value_vertical.setObjectName("lineEdit_skip_value_vertical")
        self.horizontalLayout_10.addWidget(self.lineEdit_skip_value_vertical)
        self.checkBox_compare_sign_check = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_compare_sign_check.setChecked(True)
        self.checkBox_compare_sign_check.setObjectName("checkBox_compare_sign_check")
        self.horizontalLayout_10.addWidget(self.checkBox_compare_sign_check)
        self.checkBox_compare_support_type_check = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_compare_support_type_check.setChecked(True)
        self.checkBox_compare_support_type_check.setObjectName("checkBox_compare_support_type_check")
        self.horizontalLayout_10.addWidget(self.checkBox_compare_support_type_check)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.checkBox_compare_coord_check = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_compare_coord_check.setChecked(False)
        self.checkBox_compare_coord_check.setObjectName("checkBox_compare_coord_check")
        self.horizontalLayout_11.addWidget(self.checkBox_compare_coord_check)
        self.lineEdit_coord_delta = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_coord_delta.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_coord_delta.sizePolicy().hasHeightForWidth())
        self.lineEdit_coord_delta.setSizePolicy(sizePolicy)
        self.lineEdit_coord_delta.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_coord_delta.setObjectName("lineEdit_coord_delta")
        self.horizontalLayout_11.addWidget(self.lineEdit_coord_delta)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_4.addWidget(self.line_4)
        self.textBrowser_output = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("ISOCTEUR")
        font.setPointSize(11)
        self.textBrowser_output.setFont(font)
        self.textBrowser_output.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_output.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_output.setObjectName("textBrowser_output")
        self.verticalLayout_4.addWidget(self.textBrowser_output)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1651, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "gismo"))
        self.pushButton_load.setText(_translate("MainWindow", ">add excel data<"))
        self.checkBox_line_name.setText(_translate("MainWindow", "load line name"))
        self.checkBox_purge.setText(_translate("MainWindow", "purge"))
        self.pushButton_clear_data.setText(_translate("MainWindow", "clear data"))
        self.label.setText(_translate("MainWindow", "Point list:"))
        self.plainTextEdit_serch.setPlainText(_translate("MainWindow", "AG1\n"
"AG5"))
        self.pushButton_clear_list.setText(_translate("MainWindow", "clear list"))
        self.pushButton_Sort.setText(_translate("MainWindow", "sort list"))
        self.pushButton_check.setText(_translate("MainWindow", "check list"))
        self.pushButton_getMembers.setText(_translate("MainWindow", "add all available"))
        self.pushButton_find_by_type.setText(_translate("MainWindow", "add by criteria:"))
        self.pushButton_get_from_dxf.setText(_translate("MainWindow", "get from dxf"))
        self.label_6.setText(_translate("MainWindow", "PSAS data analysis options:"))
        self.label_3.setText(_translate("MainWindow", "Select method:"))
        self.pushButton_Report.setText(_translate("MainWindow", "GENERATE PSAS REPORT"))
        self.checkBox_full.setText(_translate("MainWindow", "long report"))
        self.pushButton_save_point.setText(_translate("MainWindow", "save it as new point"))
        self.label_2.setText(_translate("MainWindow", "3D Plot:"))
        self.pushButton_plt_show.setText(_translate("MainWindow", "show"))
        self.checkBox_pltAnnot.setText(_translate("MainWindow", "plot annotation"))
        self.label_4.setText(_translate("MainWindow", "Dxf output:"))
        self.pushButton_dxf.setText(_translate("MainWindow", "export"))
        self.checkBox_DxfPointsOnly.setText(_translate("MainWindow", "Points only"))
        self.pushButton_print.setText(_translate("MainWindow", "Print report"))
        self.pushButton_info.setText(_translate("MainWindow", "App info"))
        self.label_5.setText(_translate("MainWindow", "STAAD input generate options:"))
        self.pushButton_staadGet.setText(_translate("MainWindow", "GENERATE INPUT"))
        self.label_10.setText(_translate("MainWindow", "Staad template used:"))
        self.label_8.setText(_translate("MainWindow", "Load Case to generate:"))
        self.label_7.setText(_translate("MainWindow", "Axias system STAAD(psas):"))
        self.label_9.setText(_translate("MainWindow", "Staad force unit:"))
        self.label_11.setText(_translate("MainWindow", "In PSAS W-E is:"))
        self.label_12.setText(_translate("MainWindow", "PSAS compare options:"))
        self.pushButton_Compare.setText(_translate("MainWindow", "COMPARE"))
        self.checkBox_compare_long.setText(_translate("MainWindow", "long report"))
        self.label_13.setText(_translate("MainWindow", "Tolerance, from [%] :"))
        self.label_14.setText(_translate("MainWindow", "to:"))
        self.label_15.setText(_translate("MainWindow", "Skip force levels - lateral [lbs]:"))
        self.label_16.setText(_translate("MainWindow", "and vertical [lbs]:"))
        self.checkBox_compare_sign_check.setText(_translate("MainWindow", "Gravity/Snow sign check"))
        self.checkBox_compare_support_type_check.setText(_translate("MainWindow", "Support type check"))
        self.checkBox_compare_coord_check.setText(_translate("MainWindow", "Coordinate check with tolerance [inches]:"))
        self.textBrowser_output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'ISOCTEUR\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">a---as</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">0-----</span></p></body></html>"))

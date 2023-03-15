'''
--------------------------------------------------------------------------
Copyright (C) 2022 Lukasz Laba <lukaszlaba@gmail.com>

This file is part of soco.

Soco is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

Soco is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Soco; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
--------------------------------------------------------------------------

'''

import os
import sys
#import win32com.client

import openpyxl #pandas need this!!
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtPrintSupport import QPrintDialog
from PyQt5.QtWidgets import QMessageBox
#from tabulate import tabulate
import matplotlib.pyplot as plt

from mainwindow_ui import Ui_MainWindow
from support_respoint1 import support_respoint
from preset_content import preset_dict

import pandas

support_dict = {}

unit_force = '[]'
unit_moment = '[]'
unit_coord = '[]'


version = 'sinope 0.0.1'

class MAINWINDOW(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #--
        self.ui.pushButton_Report.clicked.connect(show_report)
        # #--
        self.ui.pushButton_pltForces.clicked.connect(plot_forces)
        self.ui.pushButton_pltMoments.clicked.connect(plot_moments)
        #
        # #--
        self.ui.pushButton_Sort.clicked.connect(sort_pointlist)
        self.ui.pushButton_getMembers.clicked.connect(load_memberlist_from_results)
        self.ui.pushButton_find_by_type.clicked.connect(find_by_types)
        self.ui.pushButton_check.clicked.connect(check_pointlist)
        # #--
        self.ui.pushButton_load.clicked.connect(loaddata)
        # #--
        self.ui.pushButton_info.clicked.connect(info)
        self.ui.pushButton_print.clicked.connect(print_report)

opendir = os.path.dirname(__file__)#dir path for save and open
filename = None

support_dict = {}
excel_data_df = None


def loaddata():
    #---asking for filename
    global opendir
    global filename
    #filepath = QtWidgets.QFileDialog.getOpenFileName(caption = 'Open excel file', directory = opendir, filter = ".xlsx' (*.xlsx)")[0]
    filepath = 'C:\FAB-SSS-10_LoadReportForStructural.xlsx'
    #filepath = '/home/lul/Downloads/FAB-SSS-10_LoadReportForStructural.xlsx'
    filepath = str(filepath)
    if not filepath == '':
        opendir = os.path.dirname(filepath)
        filename = os.path.basename(filepath)
    #'C:\FAB-SSS-10_LoadReportForStructural.xlsx'
    #---geting data from selected file
    global excel_data_df
    global support_dict
    excel_data_df = pandas.read_excel(filepath, sheet_name='SUPPORTS')
    list_of_points = excel_data_df['Point'].drop_duplicates().tolist()
    excel_data_df = excel_data_df.rename(columns={  'SumOfBuildingFX': 'FX',
                                                    'SumOfBuildingFY': 'FY',
                                                    'SumOfBuildingFZ': 'FZ',
                                                    'SumOfBuildingMX': 'MX',
                                                    'SumOfBuildingMY': 'MY',
                                                    'SumOfBuildingMZ': 'MZ',
                                                    'CoordX': 'X',
                                                    'CoordY': 'Y',
                                                    'CoordZ': 'Z',
                                                    'Combination': 'Comb'
                                                    })
    for point in list_of_points:
        df1 = excel_data_df[excel_data_df['Point'] == point]
        support_dict[point] = support_respoint(df1)
    #---pushing supports types to combobox
    point_types = excel_data_df['Type'].drop_duplicates().tolist()
    myapp.ui.comboBox_Type.addItems(point_types)
    #---pushing combination mames to combobox
    point_types = excel_data_df['Comb'].drop_duplicates().tolist()
    myapp.ui.comboBox_pltComb.addItems(point_types)
    #---adding filename to app window title
    set_title(filename)
    #--geting units TODO
    global unit_force
    global unit_moment
    global unit_coord
    unit_force = '[lbs]'
    unit_moment = '[ft-lbs]'
    unit_coord = '[inch]'
    #--display status infor
    myapp.ui.textBrowser_output.setText('>>>> %s support point data loaded from %s <<<<'%(len(support_dict.keys()), filename))

#OK
def find_by_types():
    selected_type = myapp.ui.comboBox_Type.currentText()
    searchlist = []
    for point in support_dict:
        if support_dict[point].Type == selected_type:
            searchlist.append(point)
    set_pointlist(searchlist)
    sort_pointlist()

#OK
def get_pointlist():
    text = myapp.ui.plainTextEdit_serch.toPlainText()
    memberlist = list(text.split("\n"))
    memberlist = list(dict.fromkeys(memberlist)) # delete duplicates
    while '' in memberlist:
        memberlist.remove('')
    memberlist = ["".join(i.rstrip().lstrip()) for i in memberlist] # delete spaces at start and end
    return memberlist

#OK
def set_pointlist(mlist):
    out_text = ''
    for i in mlist:
        out_text += i + '\n'
    myapp.ui.plainTextEdit_serch.clear()
    myapp.ui.plainTextEdit_serch.insertPlainText(out_text)

#OK
def sort_pointlist():
    mlist = get_pointlist()
    mlist.sort()
    set_pointlist(mlist)
#OK
def check_pointlist():
    report = ''
    if is_pointlist_empty():
        report += '!!! Search list is empty -add some items !!!'
        myapp.ui.textBrowser_output.setText(report)
        return None

    if data_for_pointlist_exist():
        report += 'All data found' + '\n'
    else:
        report += '!!! PROBLEM !!!! some data not found - please correct the list\n'
    report += '---------------------------------------------------------------------' + '\n'

    for i in get_pointlist():
        if i in support_dict.keys():
            point = support_dict[i]
            report += str(i) + ' - OK - ' + str(point) + '\n'
        else:
            report += str(i) + ' - !!!!!!NO DATA FOUND!!!!!!!<<<<<<<<<<<<<<<<<<<<<<\n'
    myapp.ui.textBrowser_output.setText(report)

#OK
def is_pointlist_empty():
    if get_pointlist():
        return False
    else:
        return True
#OK
def data_for_pointlist_exist():
    if list(set(get_pointlist())-set(support_dict.keys())):
        return False
    else:
        return True

#OK
def load_memberlist_from_results():
    mlist = list(support_dict.keys())
    mlist = [i.replace('i','') for i in mlist]
    mlist = [i.replace('j','') for i in mlist]
    mlist = list(dict.fromkeys(mlist))
    set_pointlist(mlist)

#-----------------------------------------------------------

def base_reaction_report(filterlist=['AG01', 'AG05']):
    report = ''
    for i in filterlist:
        point = support_dict[i]
        report += str(point) + '\n'
        report += point.Bese_reactions.round().to_string(index=False) + '\n\n'
    return report

def merged_summ_reaction_report(filterlist=['AG01', 'AG05']):
    report = ''
    outpoint  = support_respoint()
    for i in filterlist:
        outpoint += support_dict[i]
    report += str(outpoint) + '\n'
    report += outpoint.Bese_reactions.round().to_string(index=False) + '\n\n'
    return report

def merged_replacement_reaction_report(filterlist=['AG01', 'AG05']):
    report = ''
    outpoint  = support_respoint()
    for i in filterlist:
        outpoint *= support_dict[i]
    report += str(outpoint) + '\n'
    report += outpoint.Bese_reactions.round().to_string(index=False) + '\n\n'
    return report

def join_min_max (p1, p2): #<<<<------------HERE
    #....
    return p1.Bese_reactions.round().to_string(index=False)

def show_report():
    if is_pointlist_empty():
        check_pointlist()
        return None
    if not data_for_pointlist_exist():
        check_pointlist()
        return None
    #------
    mlist = get_pointlist()
    report = ''
    sourcefile = filename
    report += 'Data source - ' + sourcefile + '\n'
    report += 'Results for  - ' + str(mlist)
    report += '\n\n'
    report += 'FX FY FZ MX MY MZ are PASS format reaction forces\n'
    report += 'Force unit - %s, Moment unit - %s'%(unit_force, unit_moment)
    report += '\n\n'

    if myapp.ui.checkBox_full.isChecked() or myapp.ui.comboBox_method.currentText() == 'keep separeted':
        report += 'Pass format one by one from selected list table:\n'
        report += base_reaction_report(mlist) + '\n'
    # checking what type of summary selected
    if myapp.ui.comboBox_method.currentText() == 'summ in to one':
        report += 'The merged result for selcted\n'
        report += merged_summ_reaction_report(mlist) + '\n'
        report += '\n'
    if myapp.ui.comboBox_method.currentText() == 'one replacement':
        report += 'The merged result for selcted\n'
        report += merged_replacement_reaction_report(mlist) + '\n'
        report += '\n'    # report += 'Extreme cases list:\n'
    # report += get_extreme_force_table(mlist) + '\n'
    myapp.ui.textBrowser_output.setText(report)

#-----------------------------------------------------------

def plot_forces():
    #You need to use Axes3D from mplot3d in mpl_toolkits, then set the subplot projection to 3d:
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import numpy as np
    soa = np.array([[0, 0, 0, 1, -2, 2], [0, 0, 0, 1, 1, 0],
                    [0, 0, 0, 2, 1, -4], [0, 0, 0, 0.5, 0.7, 0]])
    X, Y, Z, U, V, W = zip(*soa)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(X, Y, Z, U, V, W)
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-5, 5])
    plt.show()

def plot_moments():
    plot_forces()

def print_report():
    if print_dialog.exec_() == QtWidgets.QDialog.Accepted:
        myapp.ui.textBrowser_output.document().print_(print_dialog.printer())

def set_title(info=''):
    if info:
        myapp.setWindowTitle(version + ' - ' + info)
    else:
        myapp.setWindowTitle(version)


def info():
    about = '''
Sinope - J-MEPCon stress pipe reaction analysis app
Alpha stage software for testing only

-------------Licence-------------
Soco is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Soco is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Soco; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA.

Copyright (C) 2023 Lukasz Laba (e-mail : lukaszlaba@gmail.com)
Project website: https://github.com/lukaszlaba/soco
Check for lataest version: https://github.com/lukaszlaba/soco/releases
'''
    myapp.ui.textBrowser_output.setText(about)

if __name__ == '__main__':


    app = QtWidgets.QApplication(sys.argv)
    myapp = MAINWINDOW()
    # print_dialog = QPrintDialog()
    # set_title()
    # myapp.ui.textBrowser_output.setText('Welcome in soco - Staad member force extract tool! Load data and fill input list to get report.')
    # myapp.ui.plainTextEdit_serch.clear()
    # myapp.setWindowIcon(QtGui.QIcon('app.ico'))
    # # myapp.ui.comboBox_preset.addItems(preset_dict.keys())
    myapp.ui.comboBox_method.addItems(['keep separeted'])
    myapp.ui.comboBox_method.addItems(['summ in to one'])
    myapp.ui.comboBox_method.addItems(['one replacement'])
    # # myapp.ui.comboBox_preset.setCurrentIndex(3)
    myapp.show()

    loaddata()
    s1 = support_dict[list(support_dict.keys())[0]]
    s2 = support_dict[list(support_dict.keys())[4]]
    s3 = support_dict[list(support_dict.keys())[12]]
    s4 = support_dict[list(support_dict.keys())[13]]
    s1+s2+s3+s4
    sys.exit(app.exec_())


#command used to frozening with pyinstaller
#pyinstaller --onefile --noconsole --icon=app.ico ..\soco.py

#cd C:\Users\Lenovo\python_wip\myenv\env_sinope\Scripts
#pyuic5 C:\Users\Lenovo\Dropbox\PYAPPS_STRUCT\SOURCE_SINOPE\source\mainwindow.ui > C:\Users\Lenovo\Dropbox\PYAPPS_STRUCT\SOURCE_SINOPE\source\mainwindow_ui.py
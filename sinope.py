'''
--------------------------------------------------------------------------
Copyright (C) 2023 Lukasz Laba <lukaszlaba@gmail.com>

This file is part of Sinope.

Sinope is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

Sinope is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Sinope; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
--------------------------------------------------------------------------

'''

import os
import sys

import openpyxl #pandas need this!!
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtPrintSupport import QPrintDialog
from PyQt5.QtWidgets import QMessageBox
import matplotlib.pyplot as plt
from dxfwrite import DXFEngine as dxf

from mainwindow_ui import Ui_MainWindow
from support_respoint import support_respoint

import pandas

support_dict = {}

unit_force = '[]'
unit_moment = '[]'
unit_coord = '[]'

opendir = os.path.dirname(__file__)#dir path for save and open
filename = None

support_dict = {}
excel_data_df = None


version = 'sinope 0.0.2'

class MAINWINDOW(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #--
        self.ui.pushButton_Report.clicked.connect(show_report)
        # #--
        self.ui.pushButton_plt_show.clicked.connect(plot3D)
        self.ui.pushButton_dxf.clicked.connect(save_as_dxf)
        #
        # #--
        self.ui.pushButton_Sort.clicked.connect(sort_pointlist)
        self.ui.pushButton_getMembers.clicked.connect(load_memberlist_from_results)
        self.ui.pushButton_find_by_type.clicked.connect(find_by_types)
        self.ui.pushButton_check.clicked.connect(check_pointlist)
        # #--
        self.ui.pushButton_load.clicked.connect(loaddata)
        #--
        self.ui.pushButton_info.clicked.connect(info)
        self.ui.pushButton_print.clicked.connect(print_report)
        #--
        self.ui.comboBox_method.currentIndexChanged.connect(ui_update)

def ui_update():
    if myapp.ui.comboBox_method.currentIndex() == 0:
        myapp.ui.comboBox_method_value.setDisabled(True)
    else:
        myapp.ui.comboBox_method_value.setDisabled(False)
    #---
    if myapp.ui.comboBox_method.currentIndex() == 2:
        myapp.ui.comboBox_method_value.clear()
        myapp.ui.comboBox_method_value.addItems(['env+'])
        myapp.ui.comboBox_method_value.addItems(['env-'])
        myapp.ui.comboBox_method_value.addItems(['env+/-'])
        myapp.ui.comboBox_method_value.addItems(['max_abs'])
    else:
        myapp.ui.comboBox_method_value.clear()
        myapp.ui.comboBox_method_value.addItems(['env+'])
        myapp.ui.comboBox_method_value.addItems(['env-'])
        myapp.ui.comboBox_method_value.addItems(['env+/-'])
        myapp.ui.comboBox_method_value.addItems(['max_abs'])
        myapp.ui.comboBox_method_value.addItems(['direct_summ'])

def loaddata():
    #---asking for filename
    global opendir
    global filename
    filepath = QtWidgets.QFileDialog.getOpenFileName(caption = 'Open excel file', directory = opendir, filter = ".xlsx' (*.xlsx)")[0]
    #filepath = 'C:/testdata.xlsx'
    #filepath = '/home/lul/Downloads/test.xlsx'
    filepath = str(filepath)
    if not filepath == '':
        opendir = os.path.dirname(filepath)
        filename = os.path.basename(filepath)
    #'C:\FAB-SSS-10_LoadReportForStructural.xlsx'
    #---geting data from selected file
    global excel_data_df
    global support_dict
    excel_data_df = pandas.read_excel(filepath, sheet_name='SUPPORTS')
    #---adding line prefix
    file_name = os.path.basename(filepath)
    file_name = file_name.split('.')[0]
    line_name = file_name.split('_')[0]
    print(line_name)
    excel_data_df['Point'] = line_name + '_' +excel_data_df['Point']
    #----
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
    excel_data_df['Type'] = excel_data_df['Type'].fillna('undefined')
    #----
    for point in list_of_points:
        df1 = excel_data_df[excel_data_df['Point'] == point]
        support_dict[point] = support_respoint(df1)
    #---pushing supports types to combobox
    point_types = excel_data_df['Type'].drop_duplicates().tolist()
    myapp.ui.comboBox_Type.clear()
    myapp.ui.comboBox_Type.addItems(point_types)
    #---pushing combination mames to combobox
    point_types = excel_data_df['Comb'].drop_duplicates().tolist()
    myapp.ui.comboBox_plt_comb.clear()
    myapp.ui.comboBox_plt_comb.addItems(point_types)
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
        report += point.Bese_reactions.round(2).to_string(index=False) + '\n\n'
    return report

def merged_summ_reaction_report(filterlist=['AG01', 'AG05']):
    if myapp.ui.comboBox_method_value.currentText() == 'env-': support_respoint.switch_merge_method_to_min()
    if myapp.ui.comboBox_method_value.currentText() == 'env+': support_respoint.switch_merge_method_to_max()
    if myapp.ui.comboBox_method_value.currentText() == 'max_abs': support_respoint.switch_merge_method_to_abs()
    if myapp.ui.comboBox_method_value.currentText() == 'direct_summ': support_respoint.switch_merge_method_to_direct()
    #---------------
    if myapp.ui.comboBox_method_value.currentText() == 'env+/-':
        #min option
        support_respoint.switch_merge_method_to_min()
        outpoint_min  = support_respoint()
        for i in filterlist:
            outpoint_min += support_dict[i]
        #max option
        support_respoint.switch_merge_method_to_max()
        outpoint_max  = support_respoint()
        for i in filterlist:
            outpoint_max += support_dict[i]
        report = 'MIN-MAX' + '\n'
        report += join_min_max(outpoint_min, outpoint_max) + '\n\n'
    else:
        report = ''
        outpoint  = support_respoint()
        for i in filterlist:
            outpoint += support_dict[i]
        report += str(outpoint) + '\n'
        report += outpoint.Bese_reactions.round(2).to_string(index=False) + '\n\n'
    return report

def merged_replacement_reaction_report(filterlist=['AG01', 'AG05']):
    if myapp.ui.comboBox_method_value.currentText() == 'env-': support_respoint.switch_merge_method_to_min()
    if myapp.ui.comboBox_method_value.currentText() == 'env+': support_respoint.switch_merge_method_to_max()
    if myapp.ui.comboBox_method_value.currentText() == 'max_abs': support_respoint.switch_merge_method_to_abs()
    if myapp.ui.comboBox_method_value.currentText() == 'direct_summ': support_respoint.switch_merge_method_to_direct()
    #---------------
    if myapp.ui.comboBox_method_value.currentText() == 'env+/-':
        #min option
        support_respoint.switch_merge_method_to_min()
        outpoint_min  = support_respoint()
        for i in filterlist:
            outpoint_min *= support_dict[i]
        #max option
        support_respoint.switch_merge_method_to_max()
        outpoint_max  = support_respoint()
        for i in filterlist:
            outpoint_max *= support_dict[i]
        report = 'MIN-MAX' + '\n'
        report += join_min_max(outpoint_min, outpoint_max) + '\n\n'
    else:
        report = ''
        outpoint  = support_respoint()
        for i in filterlist:
            outpoint *= support_dict[i]
        report += str(outpoint) + '\n'
        report += outpoint.Bese_reactions.round().to_string(index=False) + '\n\n'
    return report

def join_min_max (p_min, p_max):
    min_df = p_min.df.copy()
    min_df.reset_index(inplace=True, drop=True)
    max_df = p_max.df.copy()
    max_df.reset_index(inplace=True, drop=True)
    out_df = p_min.df.copy()
    out_df.reset_index(inplace=True, drop=True)
    for index, row in out_df.iterrows():
        if min_df.at[index, 'FX'] != max_df.at[index, 'FX']:
            out_df.at[index, 'FX'] = '[' + str(min_df.at[index, 'FX'].round()) + '..' + str(max_df.at[index, 'FX'].round()) + ']'
        else:
            out_df.at[index, 'FX'] = str(min_df.at[index, 'FX'].round())

        if min_df.at[index, 'FY'] != max_df.at[index, 'FY']:
            out_df.at[index, 'FY'] = '[' + str(min_df.at[index, 'FY'].round()) + '..' + str(max_df.at[index, 'FY'].round()) + ']'
        else:
            out_df.at[index, 'FY'] = str(min_df.at[index, 'FY'].round())

        if min_df.at[index, 'FZ'] != max_df.at[index, 'FZ']:
            out_df.at[index, 'FZ'] = '[' + str(min_df.at[index, 'FZ'].round()) + '..' + str(max_df.at[index, 'FZ'].round()) + ']'
        else:
            out_df.at[index, 'FZ'] = str(min_df.at[index, 'FZ'].round())
        #---
        if 'FX at' in out_df:
            out_df.at[index, 'FX at'] = '[' + min_df.at[index, 'FX at'] + '..' + max_df.at[index, 'FX at'] + ']'
            out_df.at[index, 'FX at'] = out_df.at[index, 'FX at'].replace('[-..-]', '-')
        if 'FX at' in out_df:
            out_df.at[index, 'FY at'] = '[' + min_df.at[index, 'FY at'] + '..' + max_df.at[index, 'FY at'] + ']'
            out_df.at[index, 'FY at'] = out_df.at[index, 'FY at'].replace('[-..-]', '-')
        if 'FX at' in out_df:
            out_df.at[index, 'FZ at'] = '[' + min_df.at[index, 'FZ at'] + '..' + max_df.at[index, 'FZ at'] + ']'
            out_df.at[index, 'FZ at'] = out_df.at[index, 'FZ at'].replace('[-..-]', '-')
    #....
    out_p = support_respoint(out_df)
    return out_p.Bese_reactions.round().to_string(index=False)

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
    #report += 'FX FY FZ MX MY MZ are PASS format reaction forces\n'
    report += 'FX FY FZ are PASS format reaction forces\n'
    report += 'Force unit - %s '%(unit_force)
    report += '\n\n'
    #------------------
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
    myapp.ui.textBrowser_output.setText(report)

def plot3D():
    comb = myapp.ui.comboBox_plt_comb.currentText()
    force_type = myapp.ui.comboBox_plt_mf.currentText()
    #-----
    X0=[]
    X1=[]
    Y0=[]
    Y1=[]
    Z0=[]
    Z1=[]
    label = []
    max_value = 0
    for s_name in get_pointlist():
        s = support_dict[s_name]
        if force_type == 'force': vector = s.get_force_vector(comb)
        if force_type == 'moment': vector = s.get_force_vector(comb)
        if vector:
            print(vector)
            X0.append(0)
            X1.append(vector[0])
            Y0.append(0)
            Y1.append(vector[1])
            Z0.append(0)
            Z1.append(vector[2])
            label.append(s_name)
            max_value = max(max_value, abs(max(vector)), abs(min(vector)))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(X0, Y0, Z0, X1, Y1, Z1)
    max_value = 1.1*max_value
    ax.set_xlim([-max_value, max_value])
    ax.set_ylim([-max_value, max_value])
    ax.set_zlim([-max_value, max_value])
    if force_type == 'force':
        ax.set_xlabel("Fx " + unit_force)
        ax.set_ylabel("Fy " + unit_force)
        ax.set_zlabel("Fz " + unit_force)
    if force_type == 'moment':
        ax.set_xlabel("Mx " + unit_moment)
        ax.set_ylabel("My " + unit_moment)
        ax.set_zlabel("Mz " + unit_moment)
    ax.set_title(comb + '-' + force_type)
    if myapp.ui.checkBox_pltAnnot.isChecked():
        for i in range(len(X1)):
            ax.text(X1[i], Y1[i], Z1[i], label[i])
    plt.show()

def save_as_dxf():
    if not filename:
        myapp.ui.textBrowser_output.setText('Load excel data first!')
        return 0
    try:
        dxf_filename = filename.split('.')[0]
        dxf_filename = dxf_filename + '.dxf'
        filenamepath = os.path.join(opendir, dxf_filename)
        drawing = dxf.drawing(filenamepath)
        layer_name = 'sinope'
        drawing.add_layer(layer_name, color=2)

        # text = dxf.text('Text', (2, 2, 0), height=5.0, rotation=0)
        # text['layer'] = 'Xxxx'
        # text['color'] = 5
        # drawing.add(text)

        # line = dxf.line((0, 0, 0), (10, 10, 10))
        # line['layer'] = 'Xxxx'
        # line['color'] = 3
        # drawing.add(line)

        for key in support_dict.keys():
            s = support_dict[key]
            text = dxf.mtext(s.Point + s.Bese_reactions.to_string(), s.CoordinateXYZ, height=0.01, rotation=0)
            text['layer'] = layer_name
            drawing.add(text)
        drawing.save()
        myapp.ui.textBrowser_output.setText('Dxf saved at ' + filenamepath)
    except:
        myapp.ui.textBrowser_output.setText('Dxf not saved!! Some problems occurred.')


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
Sinope - J-ConMP stress pipe reaction analysis app
Alpha stage software.

-------------Licence-------------
Sinope is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Sinope is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Sinope; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA.

Copyright (C) 2023 Lukasz Laba (e-mail : lukaszlaba@gmail.com)
Project website: https://github.com/lukaszlaba/sinope
Check for lataest version: https://github.com/lukaszlaba/sinope/releases
'''
    myapp.ui.textBrowser_output.setText(about)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MAINWINDOW()
    print_dialog = QPrintDialog()
    set_title()
    myapp.ui.textBrowser_output.setText('Welcome in sinope - J-ConMP stress pipe reaction analysis app. Load data and fill input list to get report.')
    myapp.ui.plainTextEdit_serch.clear()
    myapp.setWindowIcon(QtGui.QIcon('app.ico'))
    myapp.ui.comboBox_method.addItems(['keep separeted'])
    myapp.ui.comboBox_method.addItems(['summ in to one'])
    myapp.ui.comboBox_method.addItems(['one replacement'])
    ui_update()
    myapp.ui.comboBox_method.setCurrentIndex(2)
    myapp.ui.comboBox_plt_mf.setEnabled(False)
    myapp.show()
    #loaddata()
    # s1 = support_dict[list(support_dict.keys())[0]]
    # s2 = support_dict[list(support_dict.keys())[4]]
    # s3 = support_dict[list(support_dict.keys())[12]]
    # s4 = support_dict[list(support_dict.keys())[13]]
    # s1+s2+s3+s4
    sys.exit(app.exec_())


#command used to frozening with pyinstaller
#pyinstaller --onefile --noconsole --icon=app.ico C:\Users\Lenovo\Dropbox\PYAPPS_STRUCT\SOURCE_SINOPE\source\sinope.py

#cd C:\Users\Lenovo\python_wip\myenv\env_sinope\Scripts
#pyuic5 C:\Users\Lenovo\Dropbox\PYAPPS_STRUCT\SOURCE_SINOPE\source\mainwindow.ui > C:\Users\Lenovo\Dropbox\PYAPPS_STRUCT\SOURCE_SINOPE\source\mainwindow_ui.py
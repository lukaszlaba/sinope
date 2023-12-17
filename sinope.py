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

import openpyxl #pandas need this!
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtPrintSupport import QPrintDialog
from PyQt5.QtWidgets import QInputDialog, QMessageBox
from PyQt5.QtWidgets import QMessageBox
import matplotlib.pyplot as plt
from dxfwrite import DXFEngine as dxf

from mainwindow_ui import Ui_MainWindow
from support_respoint import support_respoint

import staadTemplate_PYT
import staadTemplate_JDC

import pandas

support_dict = {}

unit_force = '[]'
unit_moment = '[]'
unit_coord = '[]'

opendir = os.path.dirname(__file__)#dir path for save and open
filename = None

support_dict = {}

#---
available_staad_templates = ['PYT', 'JDC']
load_case_list = []
ucs_transform_possible = []
get_staad_command = None
#---
version = 'sinope 0.2.3_wip'

class MAINWINDOW(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #--
        self.ui.pushButton_Report.clicked.connect(show_report)
        self.ui.pushButton_save_point.clicked.connect(save_point)
        #--
        self.ui.pushButton_plt_show.clicked.connect(plot3D)
        self.ui.pushButton_dxf.clicked.connect(save_as_dxf)
        #
        #--
        self.ui.pushButton_Sort.clicked.connect(sort_pointlist)
        self.ui.pushButton_getMembers.clicked.connect(load_memberlist_from_results)
        self.ui.pushButton_find_by_type.clicked.connect(find_by_types)
        self.ui.pushButton_check.clicked.connect(check_pointlist)
        self.ui.pushButton_clear_list.clicked.connect(clear_list)
        #--
        self.ui.pushButton_load.clicked.connect(loaddata)
        self.ui.pushButton_clear_data.clicked.connect(clear_data)
        #--
        self.ui.pushButton_info.clicked.connect(info)
        self.ui.pushButton_print.clicked.connect(print_report)
        #--
        self.ui.comboBox_method.currentIndexChanged.connect(ui_update)
        self.ui.comboBox_staadTemplate.currentIndexChanged.connect(ui_update)
        self.ui.pushButton_staadGet.clicked.connect(show_staad_input)

def ui_update():
    if myapp.ui.comboBox_method.currentIndex() == 0:
        myapp.ui.comboBox_method_value.setDisabled(True)
        myapp.ui.checkBox_full.setDisabled(True)
        myapp.ui.pushButton_staadGet.setEnabled(True) #for now as no other option availabale
    else:
        myapp.ui.comboBox_method_value.setDisabled(False)
        myapp.ui.checkBox_full.setDisabled(False)
        myapp.ui.pushButton_staadGet.setDisabled(True) #for now as no other option availabale
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
    #---
    set_template()

def set_template():
    global load_case_list
    global ucs_transform_possible
    global get_staad_command
    if myapp.ui.comboBox_staadTemplate.currentText() == 'PYT':
        load_case_list = staadTemplate_PYT.load_case_list
        ucs_transform_possible = staadTemplate_PYT.ucs_transform_possible
        get_staad_command = staadTemplate_PYT.get_staad_command
    if myapp.ui.comboBox_staadTemplate.currentText() == 'JDC':
        load_case_list = staadTemplate_JDC.load_case_list
        ucs_transform_possible = staadTemplate_JDC.ucs_transform_possible
        get_staad_command = staadTemplate_JDC.get_staad_command
    myapp.ui.comboBox_staadLC.clear()
    myapp.ui.comboBox_staadLC.addItems(load_case_list + ['All'])
    myapp.ui.comboBox_staadUCS.clear()
    myapp.ui.comboBox_staadUCS.addItems(ucs_transform_possible)

def loaddata():
    #---asking for filename
    global opendir
    global filename
    #---
    filepath = QtWidgets.QFileDialog.getOpenFileName(caption = 'Open excel file', directory = opendir, filter = ".xlsx' (*.xlsx)")[0]
    #filepath = 'C:/testdata.xlsx'
    #filepath = '/home/lul/Downloads/test.xlsx'
    filepath = str(filepath)
    if not filepath == '':
        opendir = os.path.dirname(filepath)
        filename = os.path.basename(filepath)
    #'C:\FAB-SSS-10_LoadReportForStructural.xlsx'
    #---
    myapp.ui.textBrowser_output.setText('')
    load_report = 'Loading started.. \n'
    myapp.ui.textBrowser_output.setText(load_report)
    #---geting data from selected file
    global support_dict
    excel_data_df = pandas.read_excel(filepath, sheet_name='SUPPORTS')
    #---adding line prefix
    if myapp.ui.checkBox_line_name.isChecked():
        file_name = os.path.basename(filepath)
        file_name = file_name.split('.')[0]
        if len(file_name.split('_'))>1:
            line_name = file_name.split('_')[0]
            excel_data_df['Point'] = line_name + '_' +excel_data_df['Point']
            load_report += 'pipe line name %s found in excel file name \n'%line_name
            myapp.ui.textBrowser_output.setText(load_report)
        else:
            load_report += 'no pipe line name found in excel file name \n'
            myapp.ui.textBrowser_output.setText(load_report)
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
        #---
        if point in support_dict.keys():
            load_report += point + ' already exist, data overwritten (!!!) \n'
            myapp.ui.textBrowser_output.setText(load_report)
        #---
        support_dict[point] = support_respoint(df1)
    #---pushing supports type list to combobox
    type_list = []
    for key in support_dict.keys():
        s = support_dict[key]
        type_list.append(s.Type)
    type_list = list(set(type_list))
    type_list.sort()
    if len(type_list)>1: type_list.append('any')
    myapp.ui.comboBox_Type.clear()
    myapp.ui.comboBox_Type.addItems(type_list)
    #---pushing line list to combobox
    line_list = []
    for key in support_dict.keys():
        s = support_dict[key]
        line = s.Line
        line_list.append(line)
    line_list = list(set(line_list))
    line_list.sort()
    if len(line_list)>1: line_list.append('any')
    myapp.ui.comboBox_Line.clear()
    myapp.ui.comboBox_Line.addItems(line_list)
    #---pushing combination names to combobox
    comb_list = []
    for key in support_dict.keys():
        s = support_dict[key]
        comb_list += s.CombList
    comb_list = list(set(comb_list))
    comb_list.sort()
    myapp.ui.comboBox_plt_comb.clear()
    myapp.ui.comboBox_plt_comb.addItems(comb_list)
    #--geting units
    global unit_force
    global unit_moment
    global unit_coord
    #-------looking for force unit
    try:
        excel_data_df = pandas.read_excel(filepath, sheet_name='SUMMARY')
        loc = [x[1:] for x in ((v, i, j) for i, row_tup in enumerate(excel_data_df.itertuples(index=False)) for j, v in enumerate(row_tup)) if "Forces (Fx, Fy, Fz):" in str(x[0])]
        index = loc[0][0]
        col = loc[0][1] + 1
        unit_force = '[' + excel_data_df[excel_data_df.columns[col]][index] + ']'
        load_report +=  unit_force + 'force unit found \n'
        myapp.ui.textBrowser_output.setText(load_report)
    except:
        unit_force = '[lbs]'
        load_report +=  'force unit not found, default ' + unit_force + ' used (!!!!) \n'
        myapp.ui.textBrowser_output.setText(load_report)
    #-------looking for moment unit (moment not used for now)
    unit_moment = '[ft-lbs]'
    #-------looking for coordination unit
    try:
        excel_data_df = pandas.read_excel(filepath, sheet_name='SUMMARY')
        #https://stackoverflow.com/questions/53856763/get-row-and-column-in-pandas-for-a-cell-with-a-certain-value
        loc = [x[1:] for x in ((v, i, j) for i, row_tup in enumerate(excel_data_df.itertuples(index=False)) for j, v in enumerate(row_tup)) if "Coordinates:" in str(x[0])]
        index = loc[0][0]
        col = loc[0][1] + 1 # column on the right to where the force unit tag found
        unit_coord = '[' + excel_data_df[excel_data_df.columns[col]][index] + ']'
        load_report +=  unit_coord + 'coordinate unit found \n'
        myapp.ui.textBrowser_output.setText(load_report)
    except:
        unit_coord = '[in]'
        load_report +=  'coordinate unit not found, default ' + unit_force + ' used (!!!!) \n'
        myapp.ui.textBrowser_output.setText(load_report)
    #--display load report
    load_report += '%s support point data added from %s'%(len(list_of_points), filename)
    myapp.ui.textBrowser_output.setText(load_report)
    set_title()

def clear_data():
    global support_dict
    support_dict = {}
    myapp.ui.comboBox_Type.clear()
    myapp.ui.comboBox_Line.clear()
    myapp.ui.comboBox_plt_comb.clear()
    myapp.ui.plainTextEdit_serch.clear()
    myapp.ui.textBrowser_output.setText('')
    set_title()

#OK
def find_by_types():
    selected_type = myapp.ui.comboBox_Type.currentText()
    selected_line = myapp.ui.comboBox_Line.currentText()
    searchlist = []
    for point in support_dict:
        if support_dict[point].Type == selected_type or selected_type == 'any':
                if support_dict[point].Line == selected_line or selected_line == 'any':
                    searchlist.append(point)
    set_pointlist(searchlist)
    sort_pointlist()

#OK
def get_pointlist(splited = False):
    text = myapp.ui.plainTextEdit_serch.toPlainText()
    memberlist = list(text.split("\n"))
    memberlist = list(dict.fromkeys(memberlist)) # delete duplicates
    while '' in memberlist:
        memberlist.remove('')
    memberlist = ["".join(i.rstrip().lstrip()) for i in memberlist] # delete spaces at start and end
    if splited:
        memberlist  = [i.split('@')[0] for i in memberlist]
    return memberlist

#OK
def get_staadpointlist():
    memberlist = get_pointlist(splited = False)
    while '' in memberlist:
        memberlist.remove('')
    memberlist = ["".join(i.rstrip().lstrip()) for i in memberlist] # delete spaces at start and end
    memberlist  = [i.split('@')[1] if '@' in i else '' for i in memberlist]
    return memberlist

#OK
def clear_list():
    myapp.ui.plainTextEdit_serch.clear()

#OK
def set_pointlist(mlist):
    curent_list = get_pointlist()
    mlist = curent_list + mlist
    out_text = ''
    for i in mlist:
        out_text += i + '\n'
    myapp.ui.plainTextEdit_serch.clear()
    myapp.ui.plainTextEdit_serch.insertPlainText(out_text)

#OK
def sort_pointlist():
    mlist = get_pointlist()
    mlist.sort()
    myapp.ui.plainTextEdit_serch.clear()
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

    for i in get_pointlist(splited = True):
        if i in support_dict.keys():
            point = support_dict[i]
            report += str(i) + ' - OK - ' + str(point) + '\n'
        else:
            print(i)
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
    if list(set(get_pointlist(splited = True))-set(support_dict.keys())):
        return False
    else:
        return True

#OK
def load_memberlist_from_results():
    mlist = list(support_dict.keys())
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
    env_option = myapp.ui.comboBox_method_value.currentText()
    if env_option == 'env-': support_respoint.switch_merge_method_to_min()
    if env_option == 'env+': support_respoint.switch_merge_method_to_max()
    if env_option == 'max_abs': support_respoint.switch_merge_method_to_abs()
    if env_option == 'direct_summ': support_respoint.switch_merge_method_to_direct()
    #---
    report = 'Method: summ in to one, %s \n\n'%env_option
    #---
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
        report += join_min_max(outpoint_min, outpoint_max) + '\n'
    else:
        outpoint  = support_respoint()
        for i in filterlist:
            outpoint += support_dict[i]
        report += outpoint.Bese_reactions.round(2).to_string(index=False) + '\n'
    return report

def merged_replacement_reaction_report(filterlist=['AG01', 'AG05']):
    env_option = myapp.ui.comboBox_method_value.currentText()
    if env_option == 'env-': support_respoint.switch_merge_method_to_min()
    if env_option == 'env+': support_respoint.switch_merge_method_to_max()
    if env_option == 'max_abs': support_respoint.switch_merge_method_to_abs()
    if env_option == 'direct_summ': support_respoint.switch_merge_method_to_direct()
    #---
    report = 'Method: one replacement, %s \n\n'%env_option
    #---
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
        report += join_min_max(outpoint_min, outpoint_max) + '\n'
    else:
        outpoint  = support_respoint()
        for i in filterlist:
            outpoint *= support_dict[i]
        report += outpoint.Bese_reactions.round().to_string(index=False) + '\n'
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

def list_to_compact_string(mlist = ['A01', 'A23', 'AA06', 'AA07', 'AA08', 'AA09', 'AA10']):
    out_text = str(mlist)
    out_text = out_text.replace("'", '')
    out_text = out_text.replace("[", '')
    out_text = out_text.replace("]", '')
    return out_text

def save_point():
    global support_dict
    #-
    input_name_dialog = QInputDialog.getText(None, 'Saveing new point','New point name')
    if input_name_dialog[1]:
        point_name = input_name_dialog[0]
    else: return
    #-
    env_option = myapp.ui.comboBox_method_value.currentText()
    if env_option == 'env-': support_respoint.switch_merge_method_to_min()
    if env_option == 'env+': support_respoint.switch_merge_method_to_max()
    if env_option == 'max_abs': support_respoint.switch_merge_method_to_abs()
    if env_option == 'direct_summ': support_respoint.switch_merge_method_to_direct()
    #-
    mlist = get_pointlist(splited = True)
    #-
    if myapp.ui.comboBox_method.currentText() == 'summ in to one':
        outpoint  = support_respoint()
        for i in mlist:
            outpoint += support_dict[i]
    if myapp.ui.comboBox_method.currentText() == 'one replacement':
        outpoint  = support_respoint()
        for i in mlist:
            outpoint *= support_dict[i]
    #-
    outpoint.df['Point'] = point_name
    support_dict[outpoint.Point] = outpoint
    QMessageBox.information(None, 'Info', 'New point saved')
#save_point()

def show_report():
    if is_pointlist_empty():
        check_pointlist()
        return None
    if not data_for_pointlist_exist():
        check_pointlist()
        return None
    #------
    mlist = get_pointlist(splited = True)
    report = ''
    report += 'Results for pipe supports  - ' + list_to_compact_string(mlist)
    report += '\n\n'
    #report += 'FX FY FZ MX MY MZ are PASS format reaction forces\n'
    report += 'FX FY FZ are PASS format reaction forces\n'
    report += 'Force unit - %s \n'%(unit_force)
    report += 'Coordinate unit - %s \n '%(unit_coord)
    report += '\n'
    #------------------
    if myapp.ui.checkBox_full.isChecked() or myapp.ui.comboBox_method.currentText() == 'keep separeted':
        report += '----------------------------------------------\n\n'
        report += 'PSAS format one by one for selected list of supports\n\n'
        report += base_reaction_report(mlist)
    # checking what type of summary selected
    if myapp.ui.comboBox_method.currentText() == 'summ in to one':
        report += '----------------------------------------------\n\n'
        report += "Merged result for selcted\n"
        report += merged_summ_reaction_report(mlist) + '\n'
    if myapp.ui.comboBox_method.currentText() == 'one replacement':
        report += '----------------------------------------------\n\n'
        report += 'Merged result for selcted\n'
        report += merged_replacement_reaction_report(mlist) + '\n'
    report += '----------------------------------------------\n\n'
    myapp.ui.textBrowser_output.setText(report)


def show_staad_input():
    if is_pointlist_empty():
        check_pointlist()
        return None
    if not data_for_pointlist_exist():
        check_pointlist()
        return None
    #------
    psas_point_list = get_pointlist(splited = True)
    staad_point_list = get_staadpointlist()
    LC_list = []
    if myapp.ui.comboBox_staadLC.currentText() == 'All':
        LC_list = load_case_list
    else:
        LC_list = [myapp.ui.comboBox_staadLC.currentText()]
    #------
    report = ''
    #------
    ucsTransform = myapp.ui.comboBox_staadUCS.currentText()
    psasForceUnit = unit_force
    staadForceUnit = '[%s]'%myapp.ui.comboBox_staadUnit.currentText()
    psas_W_direction = myapp.ui.comboBox_staadPsasWE.currentText()
    for LC in LC_list :
        report += '\n'
        report += '---------------------------------------\n'
        report += '\n'
        report += '*Staad input for Load Case ' + LC + ' (force unit %s)'%staadForceUnit + '\n'
        report += 'JOINT LOAD\n'
        for psas_point, staad_point in zip(psas_point_list, staad_point_list):
            respoint = support_dict[psas_point]
            staadPointNumber = staad_point
            if not staadPointNumber: staadPointNumber = '!NoNode!'
            report += get_staad_command(LC, respoint, staadPointNumber, ucsTransform, psasForceUnit, staadForceUnit, psas_W_direction)
            report += '\n'
    myapp.ui.textBrowser_output.setText(report)

def plot3D():
    comb = myapp.ui.comboBox_plt_comb.currentText()
    #-----
    X0=[]
    X1=[]
    Y0=[]
    Y1=[]
    Z0=[]
    Z1=[]
    label = []
    max_value = 0
    for s_name in get_pointlist(splited = True):
        s = support_dict[s_name]
        vector = s.get_force_vector(comb)
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
    ax.set_xlabel("Fx " + unit_force)
    ax.set_ylabel("Fy " + unit_force)
    ax.set_zlabel("Fz " + unit_force)
    ax.set_title('Combination - ' + comb)
    if myapp.ui.checkBox_pltAnnot.isChecked():
        for i in range(len(X1)):
            ax.text(X1[i], Y1[i], Z1[i], label[i])
    plt.show()

def save_as_dxf():
    if not filename:
        myapp.ui.textBrowser_output.setText('Load excel data first!')
        return 0
    try:
        dxf_filename = 'sinope_report'
        dxf_filename = dxf_filename + '.dxf'
        filenamepath = os.path.join(opendir, dxf_filename)
        drawing = dxf.drawing(filenamepath)
        layer_name = 'sinope'
        drawing.add_layer(layer_name, color=2)
        for key in support_dict.keys():
            s = support_dict[key]
            if myapp.ui.checkBox_DxfPointsOnly.isChecked():
                text = dxf.text(s.Point, s.CoordinateXYZ, height=0.1, rotation=0)
            else:
                text = dxf.mtext(s.Point + '\n' + unit_force + '\n' + s.Bese_reactions.round(2).to_string(index=False), s.CoordinateXYZ, height=0.1, rotation=0)
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
    if not info:
        if support_dict:
            info = 'data loaded'
        else:
            info = 'no data loaded'
    if info:
        myapp.setWindowTitle(version + ' - ' + info)
    else:
        myapp.setWindowTitle(version)

def info():
    about = '''
Sinope - J-ConMP stress pipe reaction analysis app
Beta stage software.

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
    #----------------------------------------------------
    myapp.ui.comboBox_method.addItems(['keep separeted'])
    myapp.ui.comboBox_method.addItems(['summ in to one'])
    myapp.ui.comboBox_method.addItems(['one replacement'])
    #----------------------------------------------------
    myapp.ui.comboBox_staadTemplate.addItems(available_staad_templates)
    myapp.ui.comboBox_staadUnit.addItems(['kip', 'lbs', 'kN'])
    myapp.ui.comboBox_staadPsasWE.addItems(['x', 'y'])
    set_template()
    myapp.ui.comboBox_staadTemplate.setDisabled(True) #for now as only one template available
    #-----------------------------------------------------
    ui_update()
    myapp.ui.comboBox_method.setCurrentIndex(0)
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
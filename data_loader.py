from PyQt5 import QtWidgets
import support_respoint
import openpyxl


class data_loader():


    def __init__(self, id=None):
        self.opendir = None
        self.filename = None

    def get_data_from_file(self, filepath):
        pass



import numpy as np
import pandas as pd
# List of Tuples
matrix = [(10, 56, 17),
          (np.NaN, 23, 11),
          (49, 36, 55),
          (75, np.NaN, 34),
          (89, 21, 44)
          ]
# Create a DataFrame
abc = pd.DataFrame(matrix, index=list('abcde'), columns=list('xyz'))
 
# output
abc

#test if main
if __name__ == '__main__':
    loader = data_loader()
    filepatch = 'C:\FAB-SSS-10_LoadReportForStructural.xlsx'
    wookbook = openpyxl.load_workbook(filepatch)
    worksheet = wookbook.active

    data = []

    for row in worksheet.values:
        if row[1]:
            row = list(row)[:14]
            for i in range(len(row)) :
                if row[i] == None:
                    row[i] = 0.0
            data.append(row)





'''
def load_sap_data():
    global opendir
    global filename
    #----asking for filename
    filename = QtWidgets.QFileDialog.getOpenFileName(   caption = 'Open ssmdata file',
                                                    directory = opendir,
                                                    filter = "xls' (*.xls)")[0]
    print(filename)

    filename = str(filename)
    if not filename == '': opendir = os.path.dirname(filename)

    global res_dict
    global NUMBER
    print(filename)
    book = xlrd.open_workbook(filename)
    sh = book.sheet_by_index(0)
    NUMBER = sh.col_values(0)

    while NUMBER[-1] == '':
        NUMBER.pop(-1)

    P = sh.col_values(5)[3:len(NUMBER)]
    V2 = sh.col_values(6)[3:len(NUMBER)]
    V3 = sh.col_values(7)[3:len(NUMBER)]
    T = sh.col_values(8)[3:len(NUMBER)]
    M2 = sh.col_values(9)[3:len(NUMBER)]
    M3 = sh.col_values(10)[3:len(NUMBER)]
    station = sh.col_values(14)[3:len(NUMBER)]
    size = sh.col_values(15)[3:len(NUMBER)]
    NUMBER = NUMBER[3:]
    for i in range(len(NUMBER)):
        try:
            NUMBER[i] = str(int(NUMBER[i]))
        except:
            pass

    #loading data

    respointid = [str(i) + str(j) for i,j in zip(NUMBER, station) if j in ['i', 'j']]

    respointid = list(dict.fromkeys(respointid))

    res_dict = {}

    #init main dist
    for i in respointid:
        res_dict[i] = RESPOINT(i)

    #load data to main dist
    print(len(NUMBER))
    print(len(station))
    for i in range(len(NUMBER)):
        this_id = str(NUMBER[i]) + str(station[i])
        if this_id in res_dict.keys():
            this_respoint = res_dict[this_id]
            this_respoint.frame_number = NUMBER[i]
            this_respoint.station = station[i]
            this_respoint.size = size[i]
            this_respoint.P_list.append(P[i])
            this_respoint.V2_list.append(V2[i])
            this_respoint.V3_list.append(V3[i])
            this_respoint.T_list.append(T[i])
            this_respoint.M2_list.append(M2[i])
            this_respoint.M3_list.append(M3[i])

    myapp.ui.textBrowser_output.setText('>>>> %s res point data loaded from %s <<<<'%(len(res_dict.keys()), os.path.basename(filename)))

    set_title(info = ' - ' + os.path.basename(filename))
'''
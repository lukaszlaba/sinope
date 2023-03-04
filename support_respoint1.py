'''
This file is part of sinope.
'''

import numpy as np
from utils import find_max, find_min, find_maxabs

class support_respoint():

    def __init__(self, data=None):
        self.df = data
        
    @property
    def type(self):
        return self.df['Type'][0]

    @property
    def tag(self):
        return self.df['Tag'][0]

    @property
    def coordinateXYZ(self):
        return [self.df['X'][0],  self.df['Y'][0], self.df['Z'][0]]

    @property
    def bese_reactions(self):
        to_get_list = ['Comb']
        if str(self.df['FX'][0]) != str(float("nan")) : to_get_list.append('FX')
        if str(self.df['FY'][0]) != str(float("nan")) : to_get_list.append('FY')
        if str(self.df['FZ'][0]) != str(float("nan")) : to_get_list.append('FZ')
        if str(self.df['MX'][0]) != str(float("nan")) : to_get_list.append('MX')
        if str(self.df['MY'][0]) != str(float("nan")) : to_get_list.append('MY')
        if str(self.df['MZ'][0]) != str(float("nan")) : to_get_list.append('MZ')
        return self.df.loc[:,to_get_list]

'''
LOAD R1 LOADTYPE Gravity  TITLE SELF-WEIGHT Y-
LOAD R2 LOADTYPE Dead  TITLE ADDITIONAL FRAMING WEIGHT
LOAD R3 LOADTYPE Dead  TITLE DL_SERVICES
LOAD R11 LOADTYPE None  TITLE PSAS P&T X+
*X-dir = East-West direction for this rack
LOAD R12 LOADTYPE None  TITLE PSAS P&T Z+
*Z-dir = North-South direction for this rack
LOAD R13 LOADTYPE None  TITLE PSAS P&T Y-
LOAD R21 LOADTYPE Seismic-H  TITLE EQ SEISMIC_MASS_X
LOAD R22 LOADTYPE Seismic-H  TITLE EQ SEISMIC_MASS_Z
LOAD R23 LOADTYPE Seismic-H  TITLE EQ PSAS X+
LOAD R24 LOADTYPE Seismic-H  TITLE EQ PSAS Z+
LOAD R25 LOADTYPE Seismic-V  TITLE EQ PSAS Y-
LOAD R26 LOADTYPE Seismic-H  TITLE EQ PSAS S.A.M.X+
LOAD R27 LOADTYPE Seismic-H  TITLE EQ PSAS S.A.M.Z+
LOAD R28 LOADTYPE Seismic-V  TITLE EQ PSAS S.A.M.Y-
LOAD R31 LOADTYPE Wind  TITLE WIND_PSAS_X+
LOAD R32 LOADTYPE Wind  TITLE WIND_PSAS_Z+
LOAD R33 LOADTYPE Wind  TITLE WIND_PSAS_Y-
LOAD R34 LOADTYPE Wind  TITLE WIND_STR_X+
LOAD R35 LOADTYPE Wind  TITLE WIND_STR_Z+
LOAD R36 LOADTYPE Wind  TITLE WIND_STR_Y-
'''

#test if main
if __name__ == '__main__': 
    m = support_respoint()


    

 
 
 
 
 
 
 
    
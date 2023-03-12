'''
This file is part of sinope.
'''

import numpy as np
import pandas as pd
from utils import find_max, find_min, find_maxabs

class support_respoint():

    def __init__(self, data=pd.DataFrame({'A' : []})):
        self.df = data
        # self.df['FX at'] = np.nan
        # self.df['FY at'] = np.nan
        # self.df['FZ at'] = np.nan
        # self.df['MX at'] = np.nan
        # self.df['MY at'] = np.nan
        # self.df['MZ at'] = np.nan
        
    def __add__(self, other):
        if self.df.empty:
            return support_respoint(other.df.copy())
        #----
        print('AAADDING')
        this = self.df.copy()
        this.reset_index(inplace=True, drop=True)
        #print(this)
        other = other.df.copy()
        other.reset_index(inplace=True, drop=True)
        #print(other)
        out = self.df.copy()
        out.reset_index(inplace=True, drop=True)
        #print(out)
        for index, row in out.iterrows():
            #print (index)
            out.at[index, 'Point'] = this.at[index, 'Point'] + ' and ' + other.at[index, 'Point']
            #----
            if out.at[index, 'Comb'] == 'E(E/W)':
                out.at[index, 'FX'] = this.at[index, 'FX'] + other.at[index, 'FX']
                out.at[index, 'FY'] = this.at[index, 'FY'] + other.at[index, 'FY']
            else:
                out.at[index, 'FX'] = abs(this.at[index, 'FX']) + abs(other.at[index, 'FX'])
                out.at[index, 'FY'] = abs(this.at[index, 'FY']) + abs(other.at[index, 'FY'])
        #(.....!!!.....)
        return support_respoint(out)

    def __mul__(self, other):
        if self.df.empty:
            self.df = other.df.copy()
        this = self.df.copy()
        this.reset_index(inplace=True, drop=True)
        #print(this)
        other = other.df.copy()
        other.reset_index(inplace=True, drop=True)
        #print(other)
        out = self.df.copy()
        out.reset_index(inplace=True, drop=True)
        if not "FX at" in out:
            out['FX at'] = np.nan
            out['FX at'] = np.nan
            out['FY at'] = np.nan
            out['FZ at'] = np.nan
            out['MX at'] = np.nan
            out['MY at'] = np.nan
            out['MZ at'] = np.nan
        #--
        for index, row in out.iterrows():
            out.at[index, 'Point'] = this.at[index, 'Point'] + ' or ' + other.at[index, 'Point']
            #-----
            if abs(this.at[index, 'FX']) > abs(other.at[index, 'FX']):
                out.at[index, 'FX'] = this.at[index, 'FX']
            else:
                out.at[index, 'FX'] = other.at[index, 'FX']
                out.at[index, 'FX at'] = other.at[index, 'Point']
            #-----
            if abs(this.at[index, 'FY']) > abs(other.at[index, 'FY']):
                out.at[index, 'FY'] = this.at[index, 'FY']
            else:
                out.at[index, 'FY'] = other.at[index, 'FY']
                out.at[index, 'FY at'] = other.at[index, 'Point']
            #-----
            if abs(this.at[index, 'FZ']) > abs(other.at[index, 'FZ']):
                out.at[index, 'FZ'] = this.at[index, 'FZ']
            else:
                out.at[index, 'FZ'] = other.at[index, 'FZ']
                out.at[index, 'FZ at'] = other.at[index, 'Point']
        #(......MI missed....)
        return support_respoint(out)

    @property
    def Point(self):
        return self.df['Point'].iloc[0]
    
    @property
    def Type(self):
        return self.df['Type'].iloc[0]

    @property
    def Tag(self):
        return self.df['Tag'].iloc[0]

    @property
    def CoordinateXYZ(self):
        return [self.df['X'].iloc[0],  self.df['Y'].iloc[0], self.df['Z'].iloc[0]]

    @property
    def Bese_reactions(self):
        to_get_list = ['Comb']
        
        if str(self.df['FX'].iloc[0]) != str(float("nan")) : 
            to_get_list.append('FX')
            if 'FX at' in self.df: to_get_list.append('FX at')

        if str(self.df['FY'].iloc[0]) != str(float("nan")) : 
            to_get_list.append('FY')
            if 'FY at' in self.df: to_get_list.append('FY at')

        if str(self.df['FZ'].iloc[0]) != str(float("nan")) : 
            to_get_list.append('FZ')
            if 'FZ at' in self.df: to_get_list.append('FZ at')
        
        if str(self.df['MX'].iloc[0]) != str(float("nan")) : 
            to_get_list.append('MX')
            if 'MX at' in self.df: to_get_list.append('MX at')
        
        if str(self.df['MY'].iloc[0]) != str(float("nan")) : 
            to_get_list.append('MY')
            if 'MY at' in self.df: to_get_list.append('MY at')
        
        if str(self.df['MZ'].iloc[0]) != str(float("nan")) : 
            to_get_list.append('MZ')
            if 'MZ at' in self.df: to_get_list.append('MZ at')
        
        return self.df.loc[:,to_get_list]

    def __str__(self):
        return self.Point + ',' + self.Type
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


    

 
 
 
 
 
 
 
    
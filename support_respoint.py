'''
This file is part of sinope.
'''

import numpy as np
import pandas as pd


sign_no_respect_combo_list = ['E(N/S)', 'E(E/W)', 'W(N/S)', 'W(E/W)']

class support_respoint():

    __MERGE_METHOD = 'max' # or min or abs
    
    def switch_merge_method_to_max():
        support_respoint.__MERGE_METHOD = 'max'

    def switch_merge_method_to_min():
        support_respoint.__MERGE_METHOD = 'min'

    def switch_merge_method_to_abs():
        support_respoint.__MERGE_METHOD = 'abs'

    def switch_merge_method_to_direct():
        support_respoint.__MERGE_METHOD = 'direct'
        
    #-------
    
    def __init__(self, data=pd.DataFrame({'A' : []})):
        self.df = data

    def __add__(self, other):
        if self.df.empty:
            return support_respoint(other.df.copy())
        #----
        this = self.df.copy()
        this.reset_index(inplace=True, drop=True)
        other = other.df.copy()
        other.reset_index(inplace=True, drop=True)
        out = self.df.copy()
        out.reset_index(inplace=True, drop=True)
        #----------------------------------------------------
        #format to make posible adding this and other in case one have no M
        #----------------------------------------------------
        if self.merge_method_is_max():
            print('max')
            for index, row in out.iterrows():
                out.at[index, 'Point'] = this.at[index, 'Point'] + ' and ' + other.at[index, 'Point']
                #----
                if out.at[index, 'Comb'] in  sign_no_respect_combo_list:
                    print(out.at[index, 'Comb'])
                    out.at[index, 'FX'] = abs(this.at[index, 'FX']) + abs(other.at[index, 'FX'])
                    out.at[index, 'FY'] = abs(this.at[index, 'FY']) + abs(other.at[index, 'FY'])
                    out.at[index, 'FZ'] = abs(this.at[index, 'FZ']) + abs(other.at[index, 'FZ'])
                else:
                    out.at[index, 'FX'] = max(0, this.at[index, 'FX'], this.at[index, 'FX'] + other.at[index, 'FX'])
                    out.at[index, 'FY'] = max(0, this.at[index, 'FY'], this.at[index, 'FY'] + other.at[index, 'FY'])
                    out.at[index, 'FZ'] = max(0, this.at[index, 'FZ'], this.at[index, 'FZ'] + other.at[index, 'FZ'])
        #----------------------------------------------------
        if self.merge_method_is_min():
            print('min')
            for index, row in out.iterrows():
                out.at[index, 'Point'] = this.at[index, 'Point'] + ' and ' + other.at[index, 'Point']
                #----
                if out.at[index, 'Comb'] in  sign_no_respect_combo_list:
                    out.at[index, 'FX'] = - abs(this.at[index, 'FX']) - abs(other.at[index, 'FX'])
                    out.at[index, 'FY'] = - abs(this.at[index, 'FY']) - abs(other.at[index, 'FY'])
                    out.at[index, 'FZ'] = - abs(this.at[index, 'FZ']) - abs(other.at[index, 'FZ'])
                else:
                    out.at[index, 'FX'] = min(0, this.at[index, 'FX'], this.at[index, 'FX'] + other.at[index, 'FX'])
                    out.at[index, 'FY'] = min(0, this.at[index, 'FY'], this.at[index, 'FY'] + other.at[index, 'FY'])
                    out.at[index, 'FZ'] = min(0, this.at[index, 'FZ'], this.at[index, 'FZ'] + other.at[index, 'FZ'])
        #----------------------------------------------------            
        if self.merge_method_is_abs():
            print('abs')
            for index, row in out.iterrows():
                out.at[index, 'Point'] = this.at[index, 'Point'] + ' and ' + other.at[index, 'Point']
                #----
                if out.at[index, 'Comb'] in  sign_no_respect_combo_list:
                    out.at[index, 'FX'] = abs(this.at[index, 'FX']) + abs(other.at[index, 'FX'])
                    out.at[index, 'FY'] = abs(this.at[index, 'FY']) + abs(other.at[index, 'FY'])
                    out.at[index, 'FZ'] = abs(this.at[index, 'FZ']) + abs(other.at[index, 'FZ'])
                else:   
                               
                    if abs(this.at[index, 'FX']) > abs(this.at[index, 'FX'] + other.at[index, 'FX']):
                        out.at[index, 'FX'] = this.at[index, 'FX']
                    else:
                        out.at[index, 'FX'] = this.at[index, 'FX'] + other.at[index, 'FX']

                    if abs(this.at[index, 'FY']) > abs(this.at[index, 'FY'] + other.at[index, 'FY']):
                        out.at[index, 'FY'] = this.at[index, 'FY']
                    else:
                        out.at[index, 'FY'] = this.at[index, 'FY'] + other.at[index, 'FY']

                    if abs(this.at[index, 'FZ']) > abs(this.at[index, 'FZ'] + other.at[index, 'FZ']):
                        out.at[index, 'FZ'] = this.at[index, 'FZ']
                    else:
                        out.at[index, 'FZ'] = this.at[index, 'FZ'] + other.at[index, 'FZ']                                            
        #----------------------------------------------------
        if self.merge_method_is_direct():
            print('direct')
            for index, row in out.iterrows():
                out.at[index, 'Point'] = this.at[index, 'Point'] + ' and ' + other.at[index, 'Point']
                #----
                if out.at[index, 'Comb'] in  sign_no_respect_combo_list:
                    out.at[index, 'FX'] = abs(this.at[index, 'FX']) + abs(other.at[index, 'FX'])
                    out.at[index, 'FY'] = abs(this.at[index, 'FY']) + abs(other.at[index, 'FY'])
                    out.at[index, 'FZ'] = abs(this.at[index, 'FZ']) + abs(other.at[index, 'FZ'])
                else:
                    out.at[index, 'FX'] = this.at[index, 'FX'] + other.at[index, 'FX']
                    out.at[index, 'FY'] = this.at[index, 'FY'] + other.at[index, 'FY']
                    out.at[index, 'FZ'] = this.at[index, 'FZ'] + other.at[index, 'FZ']
        #!!!!!!!!!!!!!!!!!!!!!!!!MI missed
        return support_respoint(out)

    def __mul__(self, other):
        if self.df.empty:
            self.df = other.df.copy()
        this = self.df.copy()
        this.reset_index(inplace=True, drop=True)
        other = other.df.copy()
        other.reset_index(inplace=True, drop=True)
        out = self.df.copy()
        out.reset_index(inplace=True, drop=True)
        # if not "FX at" in out:
        #     out['FX at'] = np.nan
        #     out['FX at'] = np.nan
        #     out['FY at'] = np.nan
        #     out['FZ at'] = np.nan
        #     out['MX at'] = np.nan
        #     out['MY at'] = np.nan
        #     out['MZ at'] = np.nan
        #----------------------------------------------------
        #format to make posible adding this and other in case one have no M
        #----------------------------------------------------
        if self.merge_method_is_max():
            for index, row in out.iterrows():
                out.at[index, 'Point'] = this.at[index, 'Point'] + ' or ' + other.at[index, 'Point']
                
                if out.at[index, 'Comb'] in  sign_no_respect_combo_list:
                    if abs(this.at[index, 'FX']) > abs(other.at[index, 'FX']):
                        out.at[index, 'FX'] = abs(this.at[index, 'FX'])
                    else:
                        out.at[index, 'FX'] = abs(other.at[index, 'FX'])
                        out.at[index, 'FX at'] = other.at[index, 'Point']
                    if out.at[index, 'FX'] == 0: out.at[index, 'FX at'] = '-'
                    #-----
                    if abs(this.at[index, 'FY']) > abs(other.at[index, 'FY']):
                        out.at[index, 'FY'] = abs(this.at[index, 'FY'])
                    else:
                        out.at[index, 'FY'] = abs(other.at[index, 'FY'])
                        out.at[index, 'FY at'] = other.at[index, 'Point']
                    if out.at[index, 'FY'] == 0: out.at[index, 'FY at'] = '-'
                    #-----
                    if abs(this.at[index, 'FZ']) > abs(other.at[index, 'FZ']):
                        out.at[index, 'FZ'] = abs(this.at[index, 'FZ'])
                    else:
                        out.at[index, 'FZ'] = abs(other.at[index, 'FZ'])
                        out.at[index, 'FZ at'] = other.at[index, 'Point']
                    if out.at[index, 'FZ'] == 0: out.at[index, 'FZ at'] = '-'
                else:
                    if this.at[index, 'FX'] > other.at[index, 'FX']:
                        out.at[index, 'FX'] = max(0, this.at[index, 'FX'])
                    else:
                        out.at[index, 'FX'] = max(0, other.at[index, 'FX'])
                        out.at[index, 'FX at'] = other.at[index, 'Point']
                    if out.at[index, 'FX'] == 0: out.at[index, 'FX at'] = '-'
                    #-----
                    if this.at[index, 'FY'] > other.at[index, 'FY']:
                        out.at[index, 'FY'] = max(0, this.at[index, 'FY'])
                    else:
                        out.at[index, 'FY'] = max(0, other.at[index, 'FY'])
                        out.at[index, 'FY at'] = other.at[index, 'Point']
                    if out.at[index, 'FY'] == 0: out.at[index, 'FY at'] = '-'
                    #-----
                    if this.at[index, 'FZ'] > other.at[index, 'FZ']:
                        out.at[index, 'FZ'] = max(0, this.at[index, 'FZ'])
                    else:
                        out.at[index, 'FZ'] = max(0, other.at[index, 'FZ'])
                        out.at[index, 'FZ at'] = other.at[index, 'Point']
                    if out.at[index, 'FZ'] == 0: out.at[index, 'FZ at'] = '-'                    
        #----------------------------------------------------
        if self.merge_method_is_min():
            for index, row in out.iterrows():
                out.at[index, 'Point'] = this.at[index, 'Point'] + ' or ' + other.at[index, 'Point']
                
                if out.at[index, 'Comb'] in  sign_no_respect_combo_list:
                    if abs(this.at[index, 'FX']) > abs(other.at[index, 'FX']):
                        out.at[index, 'FX'] = -abs(this.at[index, 'FX'])
                    else:
                        out.at[index, 'FX'] = -abs(other.at[index, 'FX'])
                        out.at[index, 'FX at'] = other.at[index, 'Point']
                    if out.at[index, 'FX'] == 0: out.at[index, 'FX at'] = '-'
                    #-----
                    if abs(this.at[index, 'FY']) > abs(other.at[index, 'FY']):
                        out.at[index, 'FY'] = -abs(this.at[index, 'FY'])
                    else:
                        out.at[index, 'FY'] = -abs(other.at[index, 'FY'])
                        out.at[index, 'FY at'] = other.at[index, 'Point']
                    if out.at[index, 'FY'] == 0: out.at[index, 'FY at'] = '-'
                    #-----
                    if abs(this.at[index, 'FZ']) > abs(other.at[index, 'FZ']):
                        out.at[index, 'FZ'] = -abs(this.at[index, 'FZ'])
                    else:
                        out.at[index, 'FZ'] = -abs(other.at[index, 'FZ'])
                        out.at[index, 'FZ at'] = other.at[index, 'Point']
                    if out.at[index, 'FZ'] == 0: out.at[index, 'FZ at'] = '-'
                else:
                    if this.at[index, 'FX'] < other.at[index, 'FX']:
                        out.at[index, 'FX'] = min(0, this.at[index, 'FX'])
                    else:
                        out.at[index, 'FX'] = min(0, other.at[index, 'FX'])
                        out.at[index, 'FX at'] = other.at[index, 'Point']
                    if out.at[index, 'FX'] == 0: out.at[index, 'FX at'] = '-'
                    #-----
                    if this.at[index, 'FY'] < other.at[index, 'FY']:
                        out.at[index, 'FY'] = min(0, this.at[index, 'FY'])
                    else:
                        out.at[index, 'FY'] = min(0, other.at[index, 'FY'])
                        out.at[index, 'FY at'] = other.at[index, 'Point']
                    if out.at[index, 'FY'] == 0: out.at[index, 'FY at'] = '-'
                    #-----
                    if this.at[index, 'FZ'] < other.at[index, 'FZ']:
                        out.at[index, 'FZ'] = min(0, this.at[index, 'FZ'])
                    else:
                        out.at[index, 'FZ'] = min(0, other.at[index, 'FZ'])
                        out.at[index, 'FZ at'] = other.at[index, 'Point']
                    if out.at[index, 'FZ'] == 0: out.at[index, 'FZ at'] = '-'
        #----------------------------------------------------
        if self.merge_method_is_abs():
            for index, row in out.iterrows():
                out.at[index, 'Point'] = this.at[index, 'Point'] + ' or ' + other.at[index, 'Point']
                #-----
                if abs(this.at[index, 'FX']) > abs(other.at[index, 'FX']):
                    out.at[index, 'FX'] = this.at[index, 'FX']
                else:
                    out.at[index, 'FX'] = other.at[index, 'FX']
                    out.at[index, 'FX at'] = other.at[index, 'Point']
                if out.at[index, 'FX'] == 0: out.at[index, 'FX at'] = '-'
                #-----
                if abs(this.at[index, 'FY']) > abs(other.at[index, 'FY']):
                    out.at[index, 'FY'] = this.at[index, 'FY']
                else:
                    out.at[index, 'FY'] = other.at[index, 'FY']
                    out.at[index, 'FY at'] = other.at[index, 'Point']
                if out.at[index, 'FY'] == 0: out.at[index, 'FY at'] = '-'
                #-----
                if abs(this.at[index, 'FZ']) > abs(other.at[index, 'FZ']):
                    out.at[index, 'FZ'] = this.at[index, 'FZ']
                else:
                    out.at[index, 'FZ'] = other.at[index, 'FZ']
                    out.at[index, 'FZ at'] = other.at[index, 'Point']
                if out.at[index, 'FZ'] == 0: out.at[index, 'FZ at'] = '-'
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!MI missed
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
        return (self.df['X'].iloc[0],  self.df['Y'].iloc[0], self.df['Z'].iloc[0])

    @property
    def Bese_reactions(self):
        to_get_list = ['Comb']
        #----
        if str(self.df['FX'].iloc[0]) != str(float("nan")) : 
            to_get_list.append('FX')

        if str(self.df['FY'].iloc[0]) != str(float("nan")) : 
            to_get_list.append('FY')

        if str(self.df['FZ'].iloc[0]) != str(float("nan")) : 
            to_get_list.append('FZ')
        
        if str(self.df['MX'].iloc[0]) != str(float("nan")) : 
            to_get_list.append('MX')
        
        if str(self.df['MY'].iloc[0]) != str(float("nan")) : 
            to_get_list.append('MY')
        
        if str(self.df['MZ'].iloc[0]) != str(float("nan")) : 
            to_get_list.append('MZ')
            
        #-------
        if 'FX' in to_get_list:
            if 'FX at' in self.df: to_get_list.append('FX at')

        if 'FY' in to_get_list:
            if 'FY at' in self.df: to_get_list.append('FY at')

        if 'FZ' in to_get_list:
            if 'FZ at' in self.df: to_get_list.append('FZ at')
        
        if 'MX' in to_get_list:
            if 'MX at' in self.df: to_get_list.append('MX at')
        
        if 'MY' in to_get_list:
            if 'MY at' in self.df: to_get_list.append('MY at')
        
        if 'MZ' in to_get_list:
            if 'MZ at' in self.df: to_get_list.append('MZ at')
        #----
        return self.df.loc[:,to_get_list]
    
    def get_force_value(self, Comb_name='E(UP)', Force_name='FX'):
        value = float(self.df.loc[self.df['Comb'] == Comb_name][Force_name])
        
        if str(value) != str(float("nan")):
            return value
        else:
            return None

    def get_force_vector(self, Comb_name='E(UP)'):
        FX = self.get_force_value(Comb_name, 'FX')
        FY = self.get_force_value(Comb_name, 'FY')
        FZ = self.get_force_value(Comb_name, 'FZ')
        if FX or FY or FZ:
            return [FX, FY, FZ]
        else:
            return None

    def get_moment_vector(self, Comb_name='E(UP)'):
        MX = self.get_force_value(Comb_name, 'MX')
        MY = self.get_force_value(Comb_name, 'MY')
        MZ = self.get_force_value(Comb_name, 'MZ')
        if MX or MY or MZ:
            return [MX, MY, MZ]
        else:
            return None

        
    def merge_method_is_max(self):
        if support_respoint.__MERGE_METHOD == 'max':
            return True
        else:
            return False

    def merge_method_is_min(self):
        if support_respoint.__MERGE_METHOD == 'min':
            return True
        else:
            return False

    def merge_method_is_abs(self):
        if support_respoint.__MERGE_METHOD == 'abs':
            return True
        else:
            return False

    def merge_method_is_direct(self):
        if support_respoint.__MERGE_METHOD == 'direct':
            return True
        else:
            return False

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


    

 
 
 
 
 
 
 
    
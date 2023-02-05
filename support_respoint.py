'''
This file is part of sinope.
'''

import numpy as np
from utils import find_max, find_min, find_maxabs

class support_respoint():

    def __init__(self, id=None):
        self.point = None
        self.type = None
        self.tag = None
        #--
        self.CordX = None
        self.CordY = None
        self.CordZ = None
        #--
        self.data_E_DOWN = np.array([0, 0, 0, 0, 0, 0])
        self.data_E_E_W = np.array([0, 0, 0, 0, 0, 0])
        self.data_E_N_S = np.array([0, 0, 0, 0, 0, 0])
        self.data_E_UP = np.array([0, 0, 0, 0, 0, 0])
        
        self.data_Gravity = np.array([0, 0, 0, 0, 0, 0])
        
        self.data_Pressure1 = np.array([0, 0, 0, 0, 0, 0])
        self.data_Pressure2 = np.array([0, 0, 0, 0, 0, 0])
        self.data_Pressure3 = np.array([0, 0, 0, 0, 0, 0])
        
        self.data_SAM1 = np.array([0, 0, 0, 0, 0, 0])
        self.data_SAM2 = np.array([0, 0, 0, 0, 0, 0])
        
        self.data_Therma1 = np.array([0, 0, 0, 0, 0, 0])
        self.data_Therma2 = np.array([0, 0, 0, 0, 0, 0])
        self.data_Therma3 = np.array([0, 0, 0, 0, 0, 0])
        
        self.data_W_E_W = np.array([0, 0, 0, 0, 0, 0])
        self.data_W_N_S = np.array([0, 0, 0, 0, 0, 0])
        #--
        
    @property
    def force_Gravity(self):
        return self.data_Gravity
    
    
    
    
        # out gravity, EQ E_W, EQ E_W, Pressure, SAM, Thermal,  W E_W, W E_W
        
        # s1 + s2, s1 * s2
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





'''    
    def calc_additional_forces(self):
        self.calc_Mtot()
        self.calc_Vtot()
        self.calc_bolt_maxtension()
        self.calc_bolt_maxcompression()
        self.calc_bolt_maxshear()
        self.calc_Fynorm()
        self.calc_Fznorm()
        
    #---
    def calc_Mtot(self):
        for record in self.res:
            My = record[self.colMy]
            Mz = record[self.colMz]
            record.append(round((My**2 + Mz**2)**0.5, 3))

    def calc_Vtot(self):
        for record in self.res:
            Fy = record[self.colFy]
            Fz = record[self.colFz]
            record.append(round((Fy**2 + Fz**2)**0.5, 3))

    def calc_bolt_maxtension(self):
        for record in self.res:
            My = abs(record[self.colMy])
            Mz = abs(record[self.colMz])
            Fx = record[self.colFx]
            #--
            if 'ft' in self.unit_moment: a = 1
            if 'in' in self.unit_moment: a = 12
            if 'm' in self.unit_moment: a = 0.305
            if 'mm' in self.unit_moment: a = 305
            #--   
            fp = Fx / 4
            fm = -My / a / 2 - Mz / a / 2
            f = fp + fm
            f = min(f,0)
            record.append(round(f, 3))

    def calc_bolt_maxcompression(self):
        for record in self.res:
            My = abs(record[self.colMy])
            Mz = abs(record[self.colMz])
            Fx = record[self.colFx]
            #--
            if 'ft' in self.unit_moment: a = 1
            if 'in' in self.unit_moment: a = 12
            if 'm' in self.unit_moment: a = 0.305
            if 'mm' in self.unit_moment: a = 305
            #--
            fp = Fx / 4
            fm = My / a / 2 + Mz / a / 2
            f = fp + fm
            f = max(f,0)
            record.append(round(f, 3))

    def calc_bolt_maxshear(self):
        for record in self.res:
            Fy = abs(record[self.colFy])
            Fz = abs(record[self.colFz])
            Mx = abs(record[self.colMx])
            fvy = Fy / 4
            fvz = Fz / 4
            #--
            if 'ft' in self.unit_moment: a = 1
            if 'in' in self.unit_moment: a = 12
            if 'm' in self.unit_moment: a = 0.305
            if 'mm' in self.unit_moment: a = 305
            #--
            fm = Mx / 2 / (a**2 + a**2)**0.5
            fmy = fm/2**0.5
            fmz = fm/2**0.5
            #--
            fy = fvy + fmy
            fz = fvz + fmz
            f =(fy**2 + fz**2)**0.5
            record.append(round(f, 3))

    def calc_Fynorm(self):
        for record in self.res:
            Fy = record[self.colFy]
            if 'i' in self.number:
                Fynom = Fy
            if 'j' in self.number:
                Fynom = -Fy
            record.append(Fynom)
            
    def calc_Fznorm(self):
        for record in self.res:
            Fz = record[self.colFz]
            if 'i' in self.number:
                Fznom = Fz
            if 'j' in self.number:
                Fznom = -Fz
            record.append(Fznom)
    #---
    @property
    def Fxmaxabs(self):
        return find_maxabs(self.res, self.colFx)
    @property
    def Fxmax(self):
        return find_max(self.res, self.colFx)
    @property
    def Fxmin(self):
        return find_min(self.res, self.colFx)


    @property
    def Fymaxabs(self):
        return find_maxabs(self.res, self.colFy)
        
    @property
    def Fzmaxabs(self):
        return find_maxabs(self.res, self.colFz)

    @property
    def Mxmaxabs(self):
        return find_maxabs(self.res, self.colMx)

    @property
    def Mymaxabs(self):
        return find_maxabs(self.res, self.colMy)
    @property
    def Mymax(self):
        return find_max(self.res, self.colMy)
    @property
    def Mymin(self):
        return find_min(self.res, self.colMy)

    @property
    def Mzmaxabs(self):
        return find_maxabs(self.res, self.colMz)
    @property
    def Mzmax(self):
        return find_max(self.res, self.colMz)
    @property
    def Mzmin(self):
        return find_min(self.res, self.colMz)

    @property
    def Mzmaxabs(self):
        return find_maxabs(self.res, self.colMz)
        
    @property
    def Mtotmax(self):
        return find_maxabs(self.res, self.colMtot)

    @property
    def Vtotmax(self):
        return find_maxabs(self.res, self.colVtot)

    @property
    def Bolttensionmax(self):
        return find_maxabs(self.res, self.colboltmaxtension)
        
    @property
    def Boltcompressionmax(self):
        return find_maxabs(self.res, self.colmaxboltcompression)

    @property
    def Boltshearmax(self):
        return find_maxabs(self.res, self.colmaxboltshear)     
        
    @property
    def Fynormmax(self):
        return find_max(self.res, self.colFynorm)
    @property
    def Fynormmin(self):
        return find_min(self.res, self.colFynorm)

    @property
    def Fznormmax(self):
        return find_max(self.res, self.colFznorm)
    @property
    def Fznormmin(self):
        return find_min(self.res, self.colFznorm)

    #---
    @property
    def Fxlist(self):
        return [i[self.colFx] for i in self.res]
    @property
    def Fylist(self):
        return [i[self.colFy] for i in self.res]
    @property
    def Fzlist(self):
        return [i[self.colFz] for i in self.res]
    @property
    def Mxlist(self):
        return [i[self.colMx] for i in self.res]
    @property
    def Mylist(self):
        return [i[self.colMy] for i in self.res]
    @property
    def Mzlist(self):
        return [i[self.colMz] for i in self.res]
        
    @property
    def Mtotlist(self):
        return [i[self.colMtot] for i in self.res]
    @property
    def Vtotlist(self):
        return [i[self.colVtot] for i in self.res]
        
    @property
    def MaxBoltmaxtensionlist(self):
        return [i[self.colboltmaxtension] for i in self.res]
    @property
    def Maxboltcompressionlist(self):
        return [i[self.colmaxboltcompression] for i in self.res] 
    @property
    def Maxboltshearlist(self):
        return [i[self.colmaxboltshear] for i in self.res]  
    
    @property
    def Fynormlist(self):
        return [i[self.colFynorm] for i in self.res]
    @property
    def Fznormlist(self):
        return [i[self.colFznorm] for i in self.res]

    @property
    def LClist(self):
        return [i[self.colLC] for i in self.res]
    @property
    def numberlist(self):
        return [self.number]*len(self.res)
'''

#test if main
if __name__ == '__main__': 
    m = support_respoint()


    

 
 
 
 
 
 
 
    
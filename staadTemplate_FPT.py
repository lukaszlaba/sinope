'''
This file is part of Sinope.
'''
import numpy as np

description = '''
Full PSAS Transfer - Bocian Project

Staad reference loads list:

PSAS GRAVITY            -  FX FY FZ from PSAS Gravity, signs respected
PSAS SEISMIC IN X DIR   -  FX FY FZ from PSAS E(E/W) or E(N/S), signs respected
PSAS SEISMIC IN Z DIR   -  FX FY FZ from PSAS E(E/W) or E(N/S), signs respected
PSAS SEISMIC IN Y DIR   -  FX FY FZ from PSAS E(DOWN), signs respected, Note - PSAS E(DOWN) and E(UP) are the same so E(DOWN)
                           taken, signs respected
PSAS SEISMIC IN X-DIR SAM1   -  FX FY FZ from PSAS S.A.M. 1, signs respected
PSAS SEISMIC IN Z-DIR SAM2   -  FX FY FZ from PSAS S.A.M. 2, signs respected
PSAS PRESSURE 1   -  FX FY FZ from PSAS Pressure 1, signs respected
PSAS PRESSURE 2   -  FX FY FZ from PSAS Pressure 2, signs respected
PSAS PRESSURE 3   -  FX FY FZ from PSAS Pressure 3, signs respected
PSAS THERMAL 1   -  FX FY FZ from PSAS Thermal 1, signs respected
PSAS THERMAL 2   -  FX FY FZ from PSAS Thermal 2, signs respected
PSAS THERMAL 3   -  FX FY FZ from PSAS Thermal 3, signs respected
PSAS SNOW   -  FX FY FZ from PSAS Snow, signs respected
PSAS WIND IN X DIR   -  FX FY FZ from PSAS W(E/W) or W(N/S), signs respected
PSAS WIND IN Z DIR   -  FX FY FZ from PSAS W(E/W) or W(N/S), signs respected
'''

load_case_list = [  'PSAS GRAVITY',
                    'PSAS SEISMIC IN X DIR',
                    'PSAS SEISMIC IN Z DIR',
                    'PSAS SEISMIC IN Y DIR',
                    'PSAS SEISMIC IN X-DIR SAM1',
                    'PSAS SEISMIC IN Z-DIR SAM2',
                    'PSAS PRESSURE 1',
                    'PSAS PRESSURE 2',
                    'PSAS PRESSURE 3',
                    'PSAS THERMAL 1',
                    'PSAS THERMAL 2',
                    'PSAS THERMAL 3',
                    'PSAS SNOW',
                    'PSAS WIND IN X DIR',
                    'PSAS WIND IN Z DIR'
                ]

ucs_transform_possible = ['X(x)/Y(z)/Z(-y)', 'X(y)/Y(z)/Z(x)']
units = {'[kip]':1, '[lbs]':0.001, '[kN]': 0.22480894, '[N]': 0.00022480894}

def force_transform(psas_force = np.array([1, 1, 0]), ucsTransform = 'X(x)/Y(z)/Z(-y)'):
    if ucsTransform == 'X(x)/Y(z)/Z(-y)': tm = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
    if ucsTransform == 'X(y)/Y(z)/Z(x)': tm = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    psas_force = np.array([[psas_force[0]], [psas_force[1]], [psas_force[2]]])
    staad_force = np.dot(tm, psas_force)
    staad_force = np.rot90(staad_force)[0]
    return staad_force

def staad_poin_force_command_record(staadPointNumber, staad_force, reduceZero=False):
    command = ''
    if reduceZero:
        command += '%s'%staadPointNumber
        if staad_force[0]: command += ' FX %s'%staad_force[0]
        if staad_force[1]: command += ' FY %s'%staad_force[1]
        if staad_force[2]: command += ' FZ %s'%staad_force[2]

        if np.all(staad_force == 0): command = '*...all forces zero, no command generated'
    else:
        command += '%s FX %s FY %s FZ %s'%(staadPointNumber, staad_force[0], staad_force[1], staad_force[2])
    return command

def get_staad_command(LC, respoint, staadPointNumber, ucsTransform, psasForceUnit, staadForceUnit, psas_W_direction):
    forceFactor = units[psasForceUnit] / units[staadForceUnit]
    std_input = ''
    psas_point = respoint.Point
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS GRAVITY':
        psas_force = respoint.get_force_vector('Gravity')
        if not psas_force: return '*!!!!!!No gravity data in psas at point %s!!!!!!'%str(psas_point)
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        std_input += '*input for ' + str(psas_point) + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS SEISMIC IN X DIR':
        if 'X(x)' in ucsTransform.replace('-', ''):
            psas_axis = 'x'
        else:
            psas_axis = 'y'
        if psas_W_direction == psas_axis:
            seismic_dir = 'E(E/W)'
            psas_force = respoint.get_force_vector('E(E/W)')
        else:
            seismic_dir = 'E(N/S)'
            psas_force = respoint.get_force_vector('E(N/S)')
        if not psas_force: return '*!!!!!!No Seismic data in psas at point %s!!!!!!'%str(psas_point)
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        #staad_force = abs(staad_force)
        std_input += '*input for ' + str(psas_point) + ' using PSAS ' + seismic_dir + ' seismic'   + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS SEISMIC IN Z DIR':
        if 'Z(y)' in ucsTransform.replace('-', ''):
            psas_axis = 'y'
        else:
            psas_axis = 'x'
        if psas_W_direction == psas_axis:
            seismic_dir = 'E(E/W)'
            psas_force = respoint.get_force_vector('E(E/W)')
        else:
            seismic_dir = 'E(N/S)'
            psas_force = respoint.get_force_vector('E(N/S)')
        if not psas_force: return '*!!!!!!No Seismic data in psas at point %s!!!!!!'%str(psas_point)
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        #staad_force = abs(staad_force)
        std_input += '*input for ' + str(psas_point) + ' using PSAS ' + seismic_dir + ' seismic'   + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS SEISMIC IN Y DIR':
        psas_force = respoint.get_force_vector('E(DOWN)')
        if not psas_force: return '*!!!!!!No Seismic E(DOWN) data in psas at point %s!!!!!!'%str(psas_point)
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        std_input += '*input for ' + str(psas_point) + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS SEISMIC IN X-DIR SAM1':
        psas_force = respoint.get_force_vector('SAM1')
        if not psas_force: return '*!!!!!!No Seismic data in psas at point %s!!!!!!'%str(psas_point)
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        #staad_force = abs(staad_force)
        std_input += '*input for ' + str(psas_point) + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS SEISMIC IN Z-DIR SAM2':
        psas_force = respoint.get_force_vector('SAM2')
        if not psas_force: return '*!!!!!!No Seismic data in psas at point %s!!!!!!'%str(psas_point)
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        #staad_force = abs(staad_force)
        std_input += '*input for ' + str(psas_point) + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS PRESSURE 1':
        psas_force = respoint.get_force_vector('Pressure1')
        if not psas_force: return '*!!!!!!No Pressure1 data in psas at point %s!!!!!!'%str(psas_point)
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        std_input += '*input for ' + str(psas_point) + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS PRESSURE 2':
        psas_force = respoint.get_force_vector('Pressure2')
        if not psas_force: return '*!!!!!!No Pressure1 data in psas at point %s!!!!!!'%str(psas_point)
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        std_input += '*input for ' + str(psas_point) + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS PRESSURE 3':
        psas_force = respoint.get_force_vector('Pressure3')
        if not psas_force: return '*!!!!!!No Pressure1 data in psas at point %s!!!!!!'%str(psas_point)
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        std_input += '*input for ' + str(psas_point) + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS THERMAL 1':
        psas_force = respoint.get_force_vector('Thermal1')
        if not psas_force: return '*!!!!!!No Pressure1 data in psas at point %s!!!!!!'%str(psas_point)
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        std_input += '*input for ' + str(psas_point) + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS THERMAL 2':
        psas_force = respoint.get_force_vector('Thermal2')
        if not psas_force: return '*!!!!!!No Pressure1 data in psas at point %s!!!!!!'%str(psas_point)
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        std_input += '*input for ' + str(psas_point) + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS THERMAL 3':
        psas_force = respoint.get_force_vector('Thermal3')
        if not psas_force: return '*!!!!!!No Pressure1 data in psas at point %s!!!!!!'%str(psas_point)
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        std_input += '*input for ' + str(psas_point) + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS SNOW':
        psas_force = respoint.get_force_vector('Snow')
        if not psas_force: return '*!!!!!!No Snow data in psas at point %s!!!!!!'%str(psas_point)
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        std_input += '*input for ' + str(psas_point) + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS WIND IN X DIR':
        if 'X(x)' in ucsTransform.replace('-', ''):
            psas_axis = 'x'
        else:
            psas_axis = 'y'
        if psas_W_direction == psas_axis:
            wind_dir = 'W(E/W)'
            psas_force = respoint.get_force_vector('W(E/W)')
        else:
            wind_dir = 'W(N/S)'
            psas_force = respoint.get_force_vector('W(N/S)')
        if not psas_force: return '*!!!!!!No wind data in psas at point %s!!!!!!'%str(psas_point)
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        std_input += '*input for ' + str(psas_point) + ' using PSAS ' + wind_dir + ' wind'   + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS WIND IN Z DIR':
        if 'Z(y)' in ucsTransform.replace('-', ''):
            psas_axis = 'y'
        else:
            psas_axis = 'x'
        if psas_W_direction == psas_axis:
            wind_dir = 'W(E/W)'
            psas_force = respoint.get_force_vector('W(E/W)')
        else:
            wind_dir = 'W(N/S)'
            psas_force = respoint.get_force_vector('W(N/S)')
        if not psas_force: return '*!!!!!!No wind data in psas at point %s!!!!!!'%str(psas_point)
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        std_input += '*input for ' + str(psas_point) + ' using PSAS ' + wind_dir + ' wind'   + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    return std_input
#show_staad_input()


















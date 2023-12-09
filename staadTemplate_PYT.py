'''
This file is part of Sinope.
'''
import numpy as np

load_case_list = [  'PSAS GRAVITY',#
                    'PSAS SEISMIC IN X DIR',#
                    'PSAS SEISMIC IN Z DIR',#
                    'PSAS SEISMIC IN Y DIR',#
                    'PSAS SEISMIC IN X-DIR SAM1',
                    'PSAS SEISMIC IN Z-DIR SAM2',
                    'PSAS SUSTAINED THERMAL PRESSURE IN X DIR',#
                    'PSAS SUSTAINED THERMAL PRESSURE IN Z DIR',#
                    'PSAS SUSTAINED THERMAL PRESSURE IN Y DIR',#
                    'PSAS SNOW', #
                    'PSAS WIND IN X DIR', #
                    'PSAS WIND IN Z DIR' #
                ]

ucs_transform_possible = ['X(x)/Y(z)/Z(-y)', 'X(y)/Y(z)/Z(x)']
units = {'[kip]':1, '[lbs]':0.001, '[kN]': 0.225}

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
        staad_force = abs(staad_force)
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
        staad_force = abs(staad_force)
        std_input += '*input for ' + str(psas_point) + ' using PSAS ' + seismic_dir + ' seismic'   + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS SEISMIC IN Y DIR': #check the method
        psas_force_up = respoint.get_force_vector('E(UP)')
        if not psas_force_up: return '*!!!!!!No Seismic E(UP) data in psas at point %s!!!!!!'%str(psas_point)
        psas_force_down = respoint.get_force_vector('E(DOWN)')
        if not psas_force_down: return '*!!!!!!No Seismic E(DOWN) data in psas at point %s!!!!!!'%str(psas_point)
        psas_force_up = abs(np.array(psas_force_up))
        psas_force_down = abs(np.array(psas_force_down))
        psas_force = np.maximum(psas_force_up, psas_force_down)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        staad_force = abs(staad_force)
        std_input += '*input for ' + str(psas_point) + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS SEISMIC IN X-DIR SAM1':
        psas_force = respoint.get_force_vector('SAM1')
        if not psas_force: return '*!!!!!!No Seismic data in psas at point %s!!!!!!'%str(psas_point)
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        staad_force = abs(staad_force)
        std_input += '*input for ' + str(psas_point) + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS SEISMIC IN Z-DIR SAM2':
        psas_force = respoint.get_force_vector('SAM2')
        if not psas_force: return '*!!!!!!No Seismic data in psas at point %s!!!!!!'%str(psas_point)
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        staad_force = abs(staad_force)
        std_input += '*input for ' + str(psas_point) + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #--------------------------------------------------------------------------------------------------
    if LC in ['PSAS SUSTAINED THERMAL PRESSURE IN X DIR', 'PSAS SUSTAINED THERMAL PRESSURE IN Y DIR', 'PSAS SUSTAINED THERMAL PRESSURE IN Z DIR'] :
        psas_Thermal1 = respoint.get_force_vector('Thermal1')
        if not psas_Thermal1: return '*!!!!!!No Thermal1 data in psas at point %s!!!!!!'%str(psas_point)
        psas_Thermal2 = respoint.get_force_vector('Thermal2')
        if not psas_Thermal2: return '*!!!!!!No Thermal2 data in psas at point %s!!!!!!'%str(psas_point)
        psas_Thermal3 = respoint.get_force_vector('Thermal3')
        if not psas_Thermal3: return '*!!!!!!No Thermal3 data in psas at point %s!!!!!!'%str(psas_point)
        psas_Pressure1 = respoint.get_force_vector('Pressure1')
        if not psas_Pressure1: return '*!!!!!!No Pressure1 data in psas at point %s!!!!!!'%str(psas_point)
        psas_Pressure2 = respoint.get_force_vector('Pressure2')
        if not psas_Pressure2: return '*!!!!!!No Pressure2 data in psas at point %s!!!!!!'%str(psas_point)
        psas_Pressure3 = respoint.get_force_vector('Pressure3')
        if not psas_Pressure3: return '*!!!!!!No Pressure3 data in psas at point %s!!!!!!'%str(psas_point)
        psas_Thermal1 = np.array(psas_Thermal1)
        psas_Thermal2 = np.array(psas_Thermal2)
        psas_Thermal3 = np.array(psas_Thermal3)
        psas_Pressure1 = np.array(psas_Pressure1)
        psas_Pressure2 = np.array(psas_Pressure2)
        psas_Pressure3 = np.array(psas_Pressure3)
        out1 =  [   max(abs(psas_Thermal1[0]), abs(psas_Pressure1[0]), abs(psas_Thermal1[0]+psas_Pressure1[0])),
                    max(abs(psas_Thermal1[1]), abs(psas_Pressure1[1]), abs(psas_Thermal1[1]+psas_Pressure1[1])),
                    max(abs(psas_Thermal1[2]), abs(psas_Pressure1[2]), abs(psas_Thermal1[2]+psas_Pressure1[2])),
                ]
        out2 =  [   max(abs(psas_Thermal2[0]), abs(psas_Pressure2[0]), abs(psas_Thermal2[0]+psas_Pressure2[0])),
                    max(abs(psas_Thermal2[1]), abs(psas_Pressure2[1]), abs(psas_Thermal2[1]+psas_Pressure2[1])),
                    max(abs(psas_Thermal2[2]), abs(psas_Pressure2[2]), abs(psas_Thermal2[2]+psas_Pressure2[2])),
                ]
        out3 =  [   max(abs(psas_Thermal3[0]), abs(psas_Pressure3[0]), abs(psas_Thermal3[0]+psas_Pressure3[0])),
                    max(abs(psas_Thermal3[1]), abs(psas_Pressure3[1]), abs(psas_Thermal3[1]+psas_Pressure3[1])),
                    max(abs(psas_Thermal3[2]), abs(psas_Pressure3[2]), abs(psas_Thermal3[2]+psas_Pressure3[2])),
                ]
        out1=np.array(out1)
        out2=np.array(out2)
        out3=np.array(out3)
        psas_force = np.maximum(out1, out2, out3)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        if LC == 'PSAS SUSTAINED THERMAL PRESSURE IN X DIR':
            staad_force[1] = 0
            staad_force[2] = 0
        if LC == 'PSAS SUSTAINED THERMAL PRESSURE IN Y DIR':
            staad_force[0] = 0
            staad_force[2] = 0
        if LC == 'PSAS SUSTAINED THERMAL PRESSURE IN Z DIR':
            staad_force[0] = 0
            staad_force[1] = 0
        std_input += '*input for ' + str(psas_point) + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force, reduceZero=True)
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
        staad_force = abs(staad_force)
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
        staad_force = abs(staad_force)
        std_input += '*input for ' + str(psas_point) + ' using PSAS ' + wind_dir + ' wind'   + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    return std_input
#show_staad_input()
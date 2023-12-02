'''
This file is part of Sinope.
'''
import numpy as np

load_case_list = [  'PSAS GRAVITY',# OK

                    'PSAS SEISMIC IN X DIR',# OK
                    'PSAS SEISMIC IN Z DIR',# OK
                    'PSAS SEISMIC IN Y DIR',# OK

                    'PSAS SEISMIC IN X-DIR SAM1',#
                    'PSAS SEISMIC IN Z-DIR SAM2',#

                    'PSAS SUSTAINED THERMAL PRESSURE IN X DIR',# OK
                    'PSAS SUSTAINED THERMAL PRESSURE IN Z DIR',# OK
                    'PSAS SUSTAINED THERMAL PRESSURE IN Y DIR',# OK

                    'PSAS SNOW', # OK

                    'PSAS WIND IN X DIR', # OK
                    'PSAS WIND IN Z DIR' # OK
                ]



ucs_transform_possible = ['X(x)/Y(z)/Z(y)', 'X(y)/Y(z)/Z(x)']
units = {'[kip]':1, '[lbs]':0.001, '[kN]': 0.225}

def force_transform(psas_force = np.array([1, 1, 0]), ucsTransform = 'X(x)/Y(z)/Z(y)'):
    if ucsTransform == 'X(x)/Y(z)/Z(y)': tm = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    if ucsTransform == 'X(y)/Y(z)/Z(x)': tm = np.array([[0, 1, 0], [1, 0, 0], [0, 1, 1]])
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

def get_staad_commend(LC, respoint, staadPointNumber, ucsTransform, psasForceUnit, staadForceUnit, psas_W_direction):
    forceFactor = units[psasForceUnit] / units[staadForceUnit]
    std_input = ''
    psas_point = respoint.Point
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS GRAVITY':
        psas_force = respoint.get_force_vector('Gravity')
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        std_input += '*input for ' + str(psas_point) + ' at staad node ' + str(staadPointNumber) + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS SEISMIC IN X DIR':
        if 'X(x)' in ucsTransform:
            psas_axis = 'x'
        else:
            psas_axis = 'y'
        if psas_W_direction == psas_axis:
            seismic_dir = 'E(E/W)'
            psas_force = respoint.get_force_vector('E(E/W)')
        else:
            seismic_dir = 'E(N/S)'
            psas_force = respoint.get_force_vector('E(N/S)')
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        staad_force = abs(staad_force)
        std_input += '*input for ' + str(psas_point) + ' at staad node ' + str(staadPointNumber) + ' using ' + seismic_dir + ' seismic'   + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS SEISMIC IN Z DIR':
        if 'Z(y)' in ucsTransform:
            psas_axis = 'y'
        else:
            psas_axis = 'x'
        if psas_W_direction == psas_axis:
            seismic_dir = 'E(E/W)'
            psas_force = respoint.get_force_vector('E(E/W)')
        else:
            seismic_dir = 'E(N/S)'
            psas_force = respoint.get_force_vector('E(N/S)')
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        staad_force = abs(staad_force)
        std_input += '*input for ' + str(psas_point) + ' at staad node ' + str(staadPointNumber) + ' using ' + seismic_dir + ' seismic'   + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS SEISMIC IN Y DIR':
        psas_force = respoint.get_force_vector('E(UP)')
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        staad_force = abs(staad_force)
        std_input += '*input for ' + str(psas_point) + ' at staad node ' + str(staadPointNumber) + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #--------------------------------------------------------------------------------------------------
    if LC in ['PSAS SUSTAINED THERMAL PRESSURE IN X DIR', 'PSAS SUSTAINED THERMAL PRESSURE IN Y DIR', 'PSAS SUSTAINED THERMAL PRESSURE IN Z DIR'] :
        psas_Thermal1 = np.array(respoint.get_force_vector('Thermal1'))
        psas_Thermal2 = np.array(respoint.get_force_vector('Thermal2'))
        psas_Thermal3 = np.array(respoint.get_force_vector('Thermal3'))
        psas_Pressure1 = np.array(respoint.get_force_vector('Pressure1'))
        psas_Pressure2 = np.array(respoint.get_force_vector('Pressure2'))
        psas_Pressure3 = np.array(respoint.get_force_vector('Pressure3'))
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
        psas_force = max(out1, out2, out3)
        psas_force = np.array(psas_force)
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
        std_input += '*input for ' + str(psas_point) + ' at staad node ' + str(staadPointNumber) + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force, reduceZero=False)
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS SNOW':
        psas_force = respoint.get_force_vector('Snow')
        if not psas_force:
            return '*!!!!!!No Snow data in psas at point %s!!!!!!'%str(psas_point)
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        std_input += '*input for ' + str(psas_point) + ' at staad node ' + str(staadPointNumber) + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS WIND IN X DIR':
        if 'X(x)' in ucsTransform:
            psas_axis = 'x'
        else:
            psas_axis = 'y'
        if psas_W_direction == psas_axis:
            wind_dir = 'W(E/W)'
            psas_force = respoint.get_force_vector('W(E/W)')
        else:
            wind_dir = 'W(N/S)'
            psas_force = respoint.get_force_vector('W(N/S)')
        if not psas_force:
            return '*!!!!!!No wind data in psas at point %s!!!!!!'%str(psas_point)
        psas_force = np.array(psas_force)
        print(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        staad_force = abs(staad_force)
        std_input += '*input for ' + str(psas_point) + ' at staad node ' + str(staadPointNumber) + ' using ' + wind_dir + ' wind'   + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS WIND IN Z DIR':
        if 'Z(y)' in ucsTransform:
            psas_axis = 'y'
        else:
            psas_axis = 'x'
        if psas_W_direction == psas_axis:
            wind_dir = 'W(E/W)'
            psas_force = respoint.get_force_vector('W(E/W)')
        else:
            wind_dir = 'W(N/S)'
            psas_force = respoint.get_force_vector('W(N/S)')
        if not psas_force:
            return '*!!!!!!No wind data in psas at point %s!!!!!!'%str(psas_point)
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        staad_force = abs(staad_force)
        std_input += '*input for ' + str(psas_point) + ' at staad node ' + str(staadPointNumber) + ' using ' + wind_dir + ' wind'   + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)


    return std_input

#show_staad_input()


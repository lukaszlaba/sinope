'''
This file is part of Sinope.
'''
import numpy as np

load_case_list = [  'PSAS_GRAVITY',
                    'PSAS SEISMIC IN X DIR',
                    'PSAS SEISMIC IN X DIR',
                    'PSAS SEISMIC IN Y DIR',
                    'PSAS SEISMIC IN X-DIR SAM1',
                    'PSAS SEISMIC IN X-DIR SAM2',
                    'PSAS SUSTAINED THERMAL PRESSURE IN X DIR',
                    'PSAS SUSTAINED THERMAL PRESSURE IN Z DIR',
                    'PSAS SUSTAINED THERMAL PRESSURE IN Y DIR',
                    'PSAS SNOW',
                    'PSAS WIND IN X DIR',
                    'PSAS WIND IN Z DIR',
                    'PSAS SNOW'
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

def staad_poin_force_command_record(staadPointNumber, staad_force):
    command = ''
    command += '%s FX %s FY %s FZ %s'%(staadPointNumber, staad_force[0], staad_force[1], staad_force[2])
    return command

def get_staad_commend(LC, respoint, staadPointNumber, ucsTransform, psasForceUnit, staadForceUnit, psas_W_direction):
    forceFactor = units[psasForceUnit] / units[staadForceUnit]
    std_input = ''
    psas_point = respoint.Point
    #--------------------------------------------------------------------------------------------------
    if LC == 'PSAS_GRAVITY':
        psas_force = respoint.get_force_vector('Gravity')
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
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
                    max(abs(psas_Thermal1[1]), abs(psas_Pressure1[1]), abs(psas_Thermal1[0]+psas_Pressure1[1])),
                    max(abs(psas_Thermal1[2]), abs(psas_Pressure1[2]), abs(psas_Thermal1[2]+psas_Pressure1[2])),
                ]
        out2 =  [   max(abs(psas_Thermal2[0]), abs(psas_Pressure2[0]), abs(psas_Thermal2[0]+psas_Pressure2[0])),
                    max(abs(psas_Thermal2[1]), abs(psas_Pressure2[1]), abs(psas_Thermal2[0]+psas_Pressure2[1])),
                    max(abs(psas_Thermal2[2]), abs(psas_Pressure2[2]), abs(psas_Thermal2[2]+psas_Pressure2[2])),
                ]
        out3 =  [   max(abs(psas_Thermal3[0]), abs(psas_Pressure3[0]), abs(psas_Thermal3[0]+psas_Pressure3[0])),
                    max(abs(psas_Thermal3[1]), abs(psas_Pressure3[1]), abs(psas_Thermal3[0]+psas_Pressure3[1])),
                    max(abs(psas_Thermal3[2]), abs(psas_Pressure3[2]), abs(psas_Thermal3[2]+psas_Pressure3[2])),
                ]
        psas_force = max(out1, out2, out3)
        psas_force = np.array(psas_force)
        staad_force = force_transform(psas_force, ucsTransform) * forceFactor
        staad_force = np.round(staad_force, decimals=3)
        std_input += '*input for ' + str(psas_point) + ' at staad node ' + str(staadPointNumber) + '\n'
        std_input += staad_poin_force_command_record(staadPointNumber, staad_force)
    #print(LC, respoint, staadPointNumber, ucsTransform, psasForceUnit, staadForceUnit, psas_W_direction)
    return std_input

#show_staad_input()

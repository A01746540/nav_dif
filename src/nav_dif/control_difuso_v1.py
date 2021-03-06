# -*- coding: utf-8 -*-
"""Control Difuso v1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NXPcRFgNzeJM7ADdUNO1slc0JVpWLzSF

<h3>Lógica Difusa - Control Difuso QUANTUM</h3>
"""

# Librerías requeridas
import numpy as np
from fuzzy import *

# CALIBRACION DE VARIABLES
maxP = 200
CI = [0, 0, maxP/4-40, maxP/4*2]
CC = [maxP/4+40, maxP/4*2, maxP/4*3-40]
CD = [maxP/4*2, maxP/4*3+40, maxP/4*4, maxP/4*4]

maxL = 6
CCE = [0, 0, maxL/4-0.5, maxL/4*2]
CME = [maxL/4-0.5, maxL/4*2, maxL/4*3+0.5]
CLE = [maxL/4*2, maxL/4*3+0.5, maxL/4*4, maxL/4*4]


maxCV = 1 - 0.2
CL =  [0+0.2, 0+0.2, maxCV/4+0.2, maxCV/4*2+0.2]
CM = [maxCV/4+0.2, maxCV/4*2+0.2, maxCV/4*3+0.2]
CR = [maxCV/4*2+0.2, maxCV/4*3+0.2, maxCV/4*4+0.2, maxCV/4*4+0.2]

maxV = 2
CRI = [0-1, 0-1, maxV/7-1, maxV/7*2-1]
CMI = [maxV/7-1, maxV/7*2-1, maxV/7*3-1]
CLI = [maxV/7*2-1, maxV/7*3-1, maxV/7*4-1]
CLD = [maxV/7*3-1, maxV/7*4-1, maxV/7*5-1]
CMD = [maxV/7*4-1, maxV/7*5-1, maxV/7*6-1]
CRD = [maxV/7*5-1, maxV/7*6-1, maxV/7*7-1, maxV/7*7-1]

# Universo de discurso para la posicion del objeto
p = np.linspace(0, maxP, maxP*100)
# Funciones de pertenencia para la posicion
I = trapmf(p, CI)
C = trimf(p, CC)
D = trapmf(p, CD)

# Universo de discurso para la distancia del objeto
l = np.linspace(0, maxL, maxL*100)
# Funciones de pertenencia para la distancia
CE = trapmf(l, CCE)
ME = trimf(l, CME)
LE = trapmf(l, CLE)

# Universo de discurso para la velocidad lineal
cv = np.linspace(0.2, 1, 100)
# Funciones de pertenencia para la velocidad lineal
L = trapmf(cv, CL)
M = trimf(cv, CM)
R = trapmf(cv, CR)

# Universo de discurso para la velocidad angular
v = np.linspace(-1, 1, maxV*100)
# Funciones de pertenencia para la velocidad angular
RI = trapmf(v,CRI)
MI = trimf(v, CMI)
LI = trimf(v, CLI)
LD = trimf(v, CLD)
MD = trimf(v, CMD)
RD = trapmf(v, CRD)

def controlDifuso(p0, l0):
     #Fuzzificar: encontrar la pertenencia de p0 a cada conjunto difuso de entrada
    val_I = trapmf(p0, CI)
    val_C = trimf(p0, CC)
    val_D = trapmf(p0, CD)

    #Fuzzificar: encontrar la pertenencia de l0 a cada conjunto difuso de entrada
    val_CE = trapmf(l0, CCE)
    val_ME = trimf(l0, CME)
    val_LE = trapmf(l0, CLE)

    # Se calculan las funciones cortadas
    Lp = cut(max(min(val_I, val_CE), min(val_C, val_CE), min(val_D, val_CE)), L)
    Mp = cut(max(min(val_I, val_ME), min(val_C, val_ME), min(val_D, val_ME)), M)
    Rp = cut(max(min(val_I, val_LE), min(val_C, val_LE), min(val_D, val_LE)), R)
    CVp = union([Lp, Mp, Rp])

    VRDp = cut(max(min(val_I, val_CE), min(val_C, val_CE)), RD)
    VMDp = cut(max(min(val_I, val_ME), min(val_C, val_ME)), MD)
    VLDp = cut(max(min(val_I, val_LE), min(val_C, val_LE)), LD)
    VRIp = cut(min(val_D, val_CE), RI)
    VMIp = cut(min(val_D, val_ME), MI)
    VLIp = cut(min(val_D, val_LE), LI)
    Vp = union([VRDp, VMDp, VLDp, VRIp, VMIp, VLIp])

    # Aplicamos defuzzificación
    centroidVLineal = defuzz(cv, CVp, 'centroid')
    centroidVAngular = defuzz(v, Vp, 'centroid')

    return round(centroidVLineal,4), round(centroidVAngular,4)

while True:
    print('Ingrese posicion')
    p0= int(input())
    print('Ingrese distancia')
    l0= int(input())

    centroidVLineal, centroidVAngular = controlDifuso(p0, l0)
    
    print('velocidad lineal =', centroidVLineal)
    print('velocidad angular =', centroidVAngular)
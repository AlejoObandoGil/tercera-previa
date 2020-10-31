# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 17:02:28 2020

@author: Usuario
"""

#paquetes requeridos
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt 


#definimos los rangos de velocidad de 0 a 80 
x = np.arange(30,80,0.1)

#definimos las funciones miembro triangular 
lento = fuzz.trimf(x,[30,30,50])
medio = fuzz.trimf (x, [30,50,70])
medio_rapido = fuzz.trimf(x,[50,60,80])
rapido = fuzz.trimf(x, [60,80,80])


#se grafica la funcion de membresía
plt.figure()
plt.plot(x, rapido, 'b', linewidth=1.5, label='rapido')
plt.plot(x, medio_rapido, 'k', linewidth=1.5, label='medio_rapido')
plt.plot(x, medio, 'm', linewidth=1.5, label='medio')
plt.plot(x, lento, 'r', linewidth=1.5, label='lento')
plt.title('Penalti difuso')
plt.ylabel('Membresía')
plt.xlabel('Velocidad (k/h')
plt.legend(loc='center right', bbxo_to_anchor=(1.25,0.5), ncol=1, fancybox=True, shadow=True)
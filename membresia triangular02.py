# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 16:15:14 2020

@author: Usuario
"""

#Funcion de membresía Triangular 
import numpy as np
import skfuzzy as sk 
import matplotlib.pyplot as plt 

#se define un array x para el manejo del factor de calidad en un restaurante 
x = np.arange(0,11,1)

#se define un array para la funcion miembro del tipo regular 
calidad = sk.trimf(x,[0, 0, 5])

#se grafica la funcion de membresía
plt.figure()
plt.plot(x, calidad, 'b', linewidth=1.5, label='servicio')
plt.title('calidad del servicio del restaurante')
plt.ylabel('Membresía')
plt.xlabel('nivel de servicio')
plt.legend(loc='center right', bbxo_to_anchor=(1.25,0.5), ncol=1, fancybox=True, shadow=True)
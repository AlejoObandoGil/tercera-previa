# CONTROL DIFUSO API

# Elimina las advertencias
import warnings
warnings.filterwarnings('ignore')

# Importar librerias 
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control  as ctrl
%matplotlib inline

# Se crean los objetos antecedentes y consecuentes a partir de las variables del universo y las funciones de membresia
calidad = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad')
servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'servicio')
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

# La poblacion de la funcion de membresia automatica e posible con .automf (3, 5 o 7)
calidad.automf(3)
servicio.automf(3)

# Las funciones de membresia personalizados se pueden contruir interactivamente conlas API Pythonic
propina['bajo'] = fuzz.trimf(propina.universe, [0, 0, 13])
propina['medio'] = fuzz.trimf(propina.universe, [0, 13, 25])
propina['alto'] = fuzz.trimf(propina.universe, [13, 25, 25])

#visualizacion con .view()
calidad['average'].view()
servicio.view()
propina.view()

#creacion de las reglas
regla1 = ctrl.Rule(calidad['poor'] | servicio['poor'], propina['bajo'])
regla2 = ctrl.Rule(servicio['average'], propina['medio'])
regla3 = ctrl.Rule(servicio['good'] | calidad['good'], propina['alto'])

#visualizacion de la regla 1
regla1.view()

#generacion del simulador
control_propina = ctrl.ControlSystem([regla1, regla2, regla3])
asignacion_propina = ctrl.ControlSystemSimulation(control_propina)

#pasar entradas al ControlSytem usando etiquetas 'Antecedent' con pythonic API 
#Nota: si quiere pasar muchas entradas a la vez, usar .inputs (dict_of_data)

asignacion_propina.input['calidad'] = 6.5
asignacion_propina.input ['servicio'] = 9.8

#se obtiene el valor 
asignacion_propina.compute()

#se muestra la informacion 
print("valor de la propina: ")
print (asignacion_propina.output['propina'])

# se muestra la curva de asignacion de propina
propina.view(sim=asignacion_propina)
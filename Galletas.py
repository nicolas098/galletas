import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Definición variables difusas
nivel_cromatico = ctrl.Antecedent(np.arange(0, 11, 1), 'nivel_cromatico')
temperatura = ctrl.Consequent(np.arange(0, 31, 1), 'temperatura')

# Definición funciones de pertenencia nivel cromático
nivel_cromatico['cruda'] = fuzz.trimf(nivel_cromatico.universe, [0, 0, 4])
nivel_cromatico['semicruda'] = fuzz.trimf(nivel_cromatico.universe, [2, 5, 8])
nivel_cromatico['dorada'] = fuzz.trimf(nivel_cromatico.universe, [6, 10, 10])

# Definición funciones de pertenencia temperatura
temperatura['baja'] = fuzz.trimf(temperatura.universe, [0, 0, 10])
temperatura['moderada'] = fuzz.trimf(temperatura.universe, [5, 15, 25])
temperatura['alta'] = fuzz.trimf(temperatura.universe, [20, 30, 30])

# Definición de las reglas difusas
regla1 = ctrl.Rule(nivel_cromatico['cruda'], temperatura['alta'])
regla2 = ctrl.Rule(nivel_cromatico['semicruda'], temperatura['moderada'])
regla3 = ctrl.Rule(nivel_cromatico['dorada'], temperatura['baja'])

# Creación del sistema de control difuso
controlador_temperatura = ctrl.ControlSystem([regla1, regla2, regla3])
simulador = ctrl.ControlSystemSimulation(controlador_temperatura)

# Caso 1: Nivel cromático = 2 (Cruda)
simulador.input['nivel_cromatico'] = 2
simulador.compute()
temperatura_1 = simulador.output['temperatura']

# Caso 2: Nivel cromático = 6 (Semicruda)
simulador.input['nivel_cromatico'] = 6
simulador.compute()
temperatura_2 = simulador.output['temperatura']

# Caso 3: Nivel cromático = 9 (Dorada)
simulador.input['nivel_cromatico'] = 9
simulador.compute()
temperatura_3 = simulador.output['temperatura']

# Graficar las funciones de pertenencia
nivel_cromatico.view()  # Gráfico de nivel cromático
temperatura.view()  # Gráfico de temperatura

#gráfico de los resultados de los tres casos
niveles_cromaticos = [2, 6, 9]
temperaturas = [temperatura_1, temperatura_2, temperatura_3]

plt.figure(figsize=(10, 6))
plt.plot(niveles_cromaticos, temperaturas, marker='o', linestyle='-', color='b')
plt.title('Temperatura del Horno según Nivel Cromático')
plt.xlabel('Nivel Cromático')
plt.ylabel('Temperatura del Horno (°C)')
plt.grid(True)
plt.show()


#Ejercicio 5 - Horno galletas
#Programar un controlador difuso que permita calcular la temperatura con la cual se deben hornear unas galletas. La temperatura del horno debe estar entre 0 y 30 grados. 
#Para determinar la temperatura del horno se captura mediante una camara el nivel cromático de las galletas, dependiendo del nivel de programa la temperatura. Para la temperatura se tienen 3 etiquetas linguisticas, así: alta, moderada y baja.
#El nivel cromático se mide entre 0 y 10, y tiene 2 etiquetas linguisticas, cruda, semicruda y dorada.También se han definido las siguientes reglas:

#R1: Si las galletas están crudas entonces la temperatura del horno es alta
#R2: Si las galletas están semicrudas entonces la temperatura del horno es moderada.
#R3: Si las galletas están doradas entonces temperatura baja

#Encontrar la temperatura para 3 casos de prueba definidos por usted.





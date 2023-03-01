import numpy as np
import matplotlib.pyplot as plt
from Difuza import *
from scipy import constants
# Definimos los parámetros de la simulación ---------------
t_actual = 0   # tiempo inicial en segundos
t_final = 1   # tiempo final en segundos 
dt = 0.01     # intervalo de tiempo entre muestras, en segundos
CONSTANTE_M = 2 # Masa del carro
CONSTANTE_m = 1 # Masa de la pertiga
CONSTANTE_l = 1 # Longitud dela pertiga
# Definimos los valores iniciales -------------------------
pos0=(15*np.pi)/180
vel0=0
acel0=0

#grafica la funcion
def grafica(x,y,delta_t,ordenadas,titulo):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel='time (s)', ylabel=ordenadas, title=titulo+' Delta t = ' + str(delta_t) + " s")
    ax.grid()  
    plt.show()
# Calcula la aceleracion en el siguiente instante de tiempo dado el angulo y la velocidad angular actual, y la fuerza ejercida
def calcula_aceleracion(theta, v, f):
    numerador = constants.g * np.sin(theta) + np.cos(theta) * ((-f - CONSTANTE_m * CONSTANTE_l * np.power(v, 2) * np.sin(theta)) / (CONSTANTE_M + CONSTANTE_m))
    denominador = CONSTANTE_l * (4/3 - (CONSTANTE_m * np.power(np.cos(theta), 2) / (CONSTANTE_M + CONSTANTE_m)))
    return numerador / denominador
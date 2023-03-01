import numpy as np

#
# Función trapmf(x, [a, b, c, d]): función de pertenencia trapezoidal.
# Argumentos:
#   x: int, float, numpy.ndarray
#      Contiene los valores de x en el universo de discurso
#      para los cuales se evalúa su valor de pertenencia.
#   [a, b, c, d]: list, numpy.ndarray
#      contiene los parámetros de la función de pertenencia
#      debe cumplirse a <= b <= c <= d
# Retorna:
#   valor de pertencia de x según función de membresía triangular.
#   trapmf(x, param): float, si x es int, float.
#   trapmf(x, param): numpy.ndarray: si x es numpy.ndarray
#   -1 si no es posible calcular el valor
#
def trapmf(x, param):
    # param = [a, b, c, d]
    # a <= b <= c <=d
    a = float(param[0])
    b = float(param[1])
    c = float(param[2])
    d = float(param[3])
    if (a <= b) and (b <= c) and (c <= d):
        if (type(x) is int) or (type(x) is float) or (type(x) is np.float64):    
            if x < a:
                m = 0.0
            elif (a <= x) and (x < b):
                m = (x - a)/(b - a)   
            elif (b <= x) and (x <= c):
                m = 1.0  
            elif (c < x) and (x <= d):
                m = (d - x)/(d - c)  
            else:
                m = 0.0
            return m
        else: 
            m = np.zeros(x.size)
            for i in range(x.size):
                if x[i] < a:
                    m[i] = 0.0
                elif (a <= x[i]) and (x[i] < b):
                    m[i] = (x[i] - a)/(b - a)   
                elif (b <= x[i]) and (x[i] <= c):
                    m[i] = 1.0
                elif (c < x[i]) and (x[i] <= d):
                    m[i] = (d - x[i])/(d - c)  
                else:
                    m[i] = 0.0
            return m
    else:
        return -1

#
# Función trimf(x, param): función de pertenencia triangular.
# Argumentos:
#   x: int, float, numpy.ndarray
#      Contiene los valores de x en el universo de discurso
#      para los cuales se evalúa su valor de pertenencia.
#   param = [a, b, c]: list, numpy.ndarray
#      contiene los parámetros de la función de pertenencia
#      debe cumplirse a <= b <= c
# Retorna:
#   valor de pertencia de x según función de membresía triangular.
#   trimf(x, param): float, si x es int, float.
#   trimf(x, param): numpy.ndarray: si x es numpy.ndarray
#   -1 si no es posible calcular el valor
#
def trimf(x, param):
    # param = [a, b, c]
    # a <= b <= c
    a = float(param[0])
    b = float(param[1])
    c = float(param[2])
    if (a <= b) and (b <= c):
        if (type(x) is int) or (type(x) is float) or (type(x) is np.float64):     
            if x <= a:
                m = 0.0
            elif (a <= x) and (x <= b):
                m = (x - a)/(b - a)   
            elif (b <= x) and (x <= c):
                m = (c - x)/(c - b)  
            else:
                m = 0.0 
            return m
        else: 
            m = np.zeros(x.size)
            for i in range(x.size):
                if x[i] <= a:
                    m[i] = 0.0
                elif (a <= x[i]) and (x[i] <= b):
                    m[i] = (x[i] - a)/(b - a)   
                elif (b <= x[i]) and (x[i] <= c):
                    m[i] = (c - x[i])/(c - b)  
                else:
                    m[i] = 0.0
        return m
    else:
        return -1
        
# Función singleton(x, x0): función de pertenencia singleton.
# Argumentos:
#   x: int, float, numpy.ndarray
#      Contiene los valores de x en el universo de discurso
#      para los cuales se evalúa su valor de pertenencia.
#   x0: valor de referencia.
# Retorna:
#   singleton(x, x0): float, si x es int, float.
#   singleton(x, x0): numpy.ndarray: si x es numpy.ndarray
#   -1 si no es posible calcular el valor
#
def Singleton(x, x0):
    # Si es un arreglo, evalua para todos sus elementos.
    m = np.zeros(x.size)
    for i in range(x.size):
        if x[i] == x0:
            m[i] = 1.0
        else:
            m[i] = 0.0
    return m   

#x: vector del dominio
#Fp:  vector de funciones de pertenencia
#x0: valor del dominio
def fuzzificar(Fp,x,x0):
    x=np.round(x,decimals=2)
    AA=Singleton(x,x0)
    fuzz=[]
    for i in range(len(Fp)):
        for j in range(len(x)):
            if AA[j] == 1:
                fuzz.append(Fp[i][j])
    fuzz=np.array(fuzz)
    return(fuzz)
# Función defuzz(): Defuzzificación
# Argumentos:
#   y: numpy.ndarray, universo de discurso de salida
#   mf: función resultante del proceso de fuzzificación
#   option: String, método de defuzzificación
# Retorna:
#   Float: valor de salida
def defuzz(y, mf, option):
    if option == 'centroid':
        num = 0
        den = 0
        for i in range(y.size):
            num = num + y[i]*mf[i]
            den = den + mf[i]
        y0 = num/den
        return y0
    
    elif option == 'bisector':
        area = 0
        aux = 0
        for i in range(y.size - 1):
            area = area + (y[i+1] - y[i]) * ((mf[i+1] + mf[i])/2)
        for i in range(y.size):
            aux = aux + (y[i+1] - y[i]) * ((mf[i+1] + mf[i])/2)
            if (aux >= area/2):
                return y[i]

# Función union(): Unión de funciones de membresía por método max, Inferencia Borrosa Mamdani
# Argumentos:
#   data: arreglo de elementos numpy.ndarray, todos de igual dimensión
# Retorna:
#   numpy.ndarray: unión de las funciones
#
def union(data):
    aux = np.zeros(data[0].size)
    for j in range(len(data)):
        for i in range(aux.size):
            aux[i] = max(aux[i], data[j][i])
    return aux
#Funcion cortar funcion de salida
#val: valor minimo entre theta y w 
#Fp: funcion de pertenecia de la salida
def cortarF(val,Fp):
    val=float(val)
    Fr=np.zeros(Fp.size)
    if (type(val) is int) or (type(val) is float):
        for i in range(Fp.size):
            Fr[i]=min(val,Fp[i])
        return(Fr)
    else:
        return -1

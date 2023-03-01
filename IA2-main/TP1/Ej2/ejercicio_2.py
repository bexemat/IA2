import numpy as np         #Para trabajar con vectores de forma mas rapida y con mayor velocidad
import math                #Para realizar operaciones matematicas

class Nodo:
    def __init__(self, padre=None, pos=[0,0]):
        self.padre = padre
        self.pos = pos
        self.g = 0
        self.h = 0
        self.f = 0
    def calculate_h(self,objetivo): #Heuristica entre nodo actual y final
        self.h = math.sqrt((self.pos[0]-objetivo.pos[0])**2+(self.pos[1]-objetivo.pos[1])**2)
    def calculate_g(self,estado_actual): #camino recorrido
        self.g = estado_actual.g + 1
    def calculate_f(self): #Calculo de f
        self.f = self.g + self.h

def buscar_posicion(value, map):  #esta funcion nos devuelve la posicion ingresando la matriz mapa y el numero cuya posicion se quiere encontrar
    if value == 0:  # 0 es numero no valido por lo que no retorna nada
        return (0, 0)
    else:
      result = np.argwhere(map == value)   #argwhere busca en la matriz "map" que posicion ocupa el valor "value" y devuelve la posicion
      return tuple(result[0])   #Las tuples se utilizan para almacenar varios elementos en una sola variable

def a_star(map,a,b): 
    OPEN = []   #lista de nodos por investigar (lista abierta u hojas del arbol)
    CLOSED = [] #lista de nosos ya investigados (lista cerrada)
    inicio = Nodo(None,buscar_posicion(a,map))  #armamos el objeto inicio
    objetivo = Nodo(None,buscar_posicion(b,map))  #armamos el objeto objetivo
    inicio.calculate_h(objetivo)        #calcula la heuristica del inicio
    inicio.calculate_f()
    estado_actual = inicio       #Decimos que el estado actual es el nodo inicio
    OPEN.append(estado_actual)   #agragamos el nodo inicio a la lista abierta

    def get_f(nodo):    #solo se usa para hacer el sorting de nodos.f (en simples paralabras:ordena los nodos de acuerdo al f)
      return nodo.f

    if estado_actual.pos == objetivo.pos:  #si ya estamos en el objetivo
        print("La posicion actual y objetivo son las mismas")
        path = [] #creamos un vector que almacen el camino optimo
        while estado_actual is not None:  #obtenemos el camino  optimo en una lista de padres de cada nodo
            path.append(estado_actual.pos) #añadimos a la lista la poscion actual
            estado_actual = estado_actual.padre #actualizamos la posicion actual por el padre
        return(path[-2:0:-1]) #retorna el camino "invertido" porque parte del final al inicio

    Flag_Salida=True #Para los casos en los productos estan al lado:En la 1° iteracion o salida no buscamos la solucion vecina 
    while estado_actual.pos != objetivo.pos: #mientras no se alcance la posicion objetivo:
        OPEN.sort(key=get_f)    #metodo sort ordena las posiciones de la lista open de acuerdo al nodo.f (ordena la lista de acuerdo a los valores f)
        estado_actual = OPEN[0] #toma como estado actual al primero de la lista "OPEN"
        OPEN.pop(0) #se elimina al primer nodo de la lista "OPEN"
        CLOSED.append(estado_actual)  #y lo ponemos en la lista de ya explorados

        if estado_actual.pos == objetivo.pos:  #si llegamos al objetivo
            path = [] #creamos un vector que almacen el camino optimo
            while estado_actual is not None:  #obtenemos el camino  optimo en una lista de padres de cada nodo
                path.append(estado_actual.pos) #añadimos a la lista la poscion actual
                estado_actual = estado_actual.padre #actualizamos la posicion actual por el padre
            return(path[-2:0:-1]) #retorna el camino "invertido" porque parte del final al inicio

        #Si aun no llegamos al objetivo
        vecinos = []
        for a in [(1,0),(-1,0),(0,1),(0,-1)]: #movimientos validos
            pos = (a[0] + estado_actual.pos[0], a[1] + estado_actual.pos[1]) #Hace el movimiento
            if (0 <= estado_actual.pos[0]+a[0] < len(map)) and (0 <= estado_actual.pos[1]+a[1] < len(map[0])): #tomamos posiciones validas
                if map[pos]==0:
                    vecinos.append(Nodo(estado_actual,pos))   #creamos nodos nuevos para cada posicion y los añadimos a la lista vecinos
                elif (map[pos]==map[objetivo.pos] and Flag_Salida==False):  #si la posicion es el objetivo se agrega
                    vecinos.append(Nodo(estado_actual,pos))
        Flag_Salida=False

        for vecino in vecinos:
            if vecino in CLOSED:    #si ya esta en lista de explorados saltamos esa iteracion
                continue 
            vecino.calculate_g(estado_actual) #Hacemos los calculos de g,h y f de cada uno de los vecinos
            vecino.calculate_h(objetivo)
            vecino.calculate_f()
            if  vecino not in OPEN: 
                vecino.padre = estado_actual                #Asiganamos el padre a cada vecino
                OPEN.append(vecino)                     #añadimos a cada vecino a la lista abierta


print("Ejercicio 2")
map = np.array([[ 0,  0,  0,  0,  0,  0,  0],
                [ 0,  1,  2,  0, 25, 26,  0],
                [ 0,  3,  4,  0, 27, 28,  0],
                [ 0,  5,  6,  0, 29, 30,  0],
                [ 0,  7,  8,  0, 31, 32,  0],
                [ 0,  0,  0,  0,  0,  0,  0],
                [ 0,  9, 10,  0, 33, 34,  0],
                [ 0, 11, 12,  0, 35, 36,  0],
                [ 0, 13, 14,  0, 37, 38,  0],
                [ 0, 15, 16,  0, 39, 40,  0],
                [ 0,  0,  0,  0,  0,  0,  0],
                [ 0, 17, 18,  0, 41, 42,  0],
                [ 0, 19, 20,  0, 43, 44,  0],
                [ 0, 21, 22,  0, 45, 46,  0],
                [ 0, 23, 24,  0, 47, 48,  0],
                [ 0,  0,  0,  0,  0,  0,  0]])
a=1 #inicio 
b=45 #fin
solution = a_star(map,a,b)  #llamamos a la funcion A* indicando el mapa, el inicio y el fin
print("Camino optimo:")
print(solution)
for pos in solution:
    map[pos] = -1 #Camino optimo completar con unos
print(np.matrix(map))
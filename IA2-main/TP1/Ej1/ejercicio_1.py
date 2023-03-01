import numpy as np         #Para trabajar con vectores de forma mas rapida y con mayor velocidad
import math                #Para realizar operaciones matematicas
import random              #permite trabajar con funciones q generan valores aleatorios

class Nodo:
    def __init__(self, padre=None, pos=[0,0,0,0,0,0]):
        self.padre = padre
        self.pos = pos
        self.g = 0
        self.h = 0
        self.f = 0
    def calculate_h(self,objetivo): #Heuristica entre nodo actual y final
        self.h = math.sqrt((self.pos[0]-objetivo.pos[0])**2+(self.pos[1]-objetivo.pos[1])**2+(self.pos[2]-objetivo.pos[2])**2+(self.pos[3]-objetivo.pos[3])**2+(self.pos[4]-objetivo.pos[4])**2+(self.pos[5]-objetivo.pos[5])**2)
    def calculate_g(self,estado_actual,vecino): #camino recorrido
        self.g = estado_actual.g + math.sqrt((self.pos[0]-vecino.pos[0])**2+(self.pos[1]-vecino.pos[1])**2+(self.pos[2]-vecino.pos[2])**2+(self.pos[3]-vecino.pos[3])**2+(self.pos[4]-vecino.pos[4])**2+(self.pos[5]-vecino.pos[5])**2)
    def calculate_f(self): #Calculo de f
        self.f = self.g + self.h

def buscar_posicion(value, map):  #esta funcion nos devuelve la posicion ingresando la matriz mapa y el N° cuya posicion se quiere encontrar
    if value == 0:  # 0 es numero no valido por lo que no retorna nada
        return (0, 0, 0, 0, 0, 0)
    else:
      result = np.argwhere(map == value)   #argwhere busca en la matriz "map" que posicion ocupa el valor "value" y devuelve la posicion
      return tuple(result[0])  #Las tuples se utilizan para almacenar varios elementos en una sola variable

def a_star(map,a,b):  #se busca ir del punto 'a' al 'b' a traves del mapa 'map'
    OPEN = []   #lista de nodos por investigar (lista abierta -> hojas del arbol)
    CLOSED = [] #lista de nodos ya investigados (lista cerrada)
    inicio = Nodo(None,buscar_posicion(a,map))  #armamos el objeto inicio
    objetivo = Nodo(None,buscar_posicion(b,map))  #armamos el objeto objetivo
    inicio.calculate_h(objetivo)        #calcula la heuristica del inicio
    inicio.calculate_f()
    estado_actual = inicio       #Decimos que el estado actual es el nodo inicio
    OPEN.append(estado_actual)   #agragamos el nodo actual

    def get_f(nodo):    #para obtener el f de un nodo
      return nodo.f

    #Proceso iterativo
    while estado_actual.pos != objetivo.pos: #mientras no se alcance la posicion objetivo:
        OPEN.sort(key=get_f)    #metodo sort ordena las posiciones de la lista open de acuerdo a los valores de nodo.f (ordena la lista de acuerdo a los valores f)
        estado_actual = OPEN[0] #toma como estado actual al primero de la lista "OPEN" (explora el nodo con menor f)
        OPEN.pop(0) #se elimina al primer nodo de la lista "OPEN"
        CLOSED.append(estado_actual)  #y lo ponemos en la lista de ya explorados

        #si llegamos al objetivo
        if estado_actual.pos == objetivo.pos:  
            path = []
            while estado_actual is not None:  #obtenemos el camino  optimo en una lista de padres de cada nodo
                path.append(estado_actual.pos) #añadimos a la lista la posicion actual
                estado_actual = estado_actual.padre #actualizamos la posicion actual por el padre
            return(path[::-1]) #retorna el camino "invertido" porque parte del final al inicio

        #Si no llegamos al objetivo
        vecinos = [] 
        for i in (1,0,-1): #movimientos validos en X
            for j in (1,0,-1): #movimientos validos en Y
                for k in (1,0,-1): #movimientos validos en Z
                    for ii in (1,0,-1): #movimientos validos en XX
                        for jj in (1,0,-1): #movimientos validos en YY
                            for kk in (1,0,-1): #movimientos validos en ZZ
                                a=(i,j,k,ii,jj,kk) #Avance en cada iteracion hacia cada vecino
                                #Omitimos el caso donde no hay avance
                                if a==(0,0,0,0,0,0):
                                    break
                                #Para los casos donde hay avance:
                                else:
                                    pos = (a[0] + estado_actual.pos[0], a[1] + estado_actual.pos[1], a[2] + estado_actual.pos[2],a[3] + estado_actual.pos[3],a[4] + estado_actual.pos[4],a[5] + estado_actual.pos[5]) #Hace el movimiento
                                    if (0 <= estado_actual.pos[0]+a[0] < map.shape[0]) and (0 <= estado_actual.pos[1]+a[1] < map.shape[1]) and (0 <= estado_actual.pos[2]+a[2] < map.shape[2]) and (0 <= estado_actual.pos[3]+a[3] < map.shape[3]) and (0 <= estado_actual.pos[4]+a[4] < map.shape[4]) and (0 <= estado_actual.pos[5]+a[5] < map.shape[5]): #tomamos posiciones validas
                                        if map[pos]==0: #Verificamos q el nuevo nodo no sea un obstaculo
                                            vecinos.append(Nodo(estado_actual,pos))   #creamos nodos nuevos con sus respectivos padres para cada posicion y los añadimos a la lista vecinos
                                        elif (map[pos]==map[objetivo.pos]):  #si la posicion es el objetivo se agrega
                                            vecinos.append(Nodo(estado_actual,pos))
        for vecino in vecinos:
            if vecino in CLOSED:    #si ya esta en lista de explorados saltamos esa iteracion
                continue 
            vecino.calculate_g(estado_actual,vecino) #Hacemos los calculos de g,h y f de cada uno de los vecinos
            vecino.calculate_h(objetivo)
            vecino.calculate_f()
            if vecino not in OPEN: 
                vecino.padre = estado_actual                #Asiganamos el padre a cada vecino
                OPEN.append(vecino)                     #añadimos a cada vecino a la lista abierta (hojas del arbol)

def main():
    print("Ejercicio 1")
    NposD=14        #Elegimos el numero de posiciones q se pueden tomar cada articulacion
    map = np.zeros([NposD,NposD,NposD,NposD,NposD,NposD]) #Generamos la matriz de 6D (6gdl)
    NposT=NposD**6       #Numero de posiciones (todas las combinaciones posibles de las pos Articulares)
    print ("Numero de posiciones", NposT)

    inicio=1                 #inicio se identifica como 1 en el mapa
    fin=3                    #fin se identifica como 3 en el mapa
    PosI=[0,0,0,0,0,0]       #Pos inicial
    PosF=[10,5,3,7,13,12]       #Pos final
    map[tuple(PosI)]=inicio    #Pos inicial y final en el mapa
    map[tuple(PosF)]=fin       #tuples: almacenar varios elementos en una sola variable
    print ("Posicion Inicial", PosI)
    print ("Posicion Final", PosF)
    if PosI==PosF:
        return(print("La posicion actual y objetivo son las mismas"))

    obstaculo=2   #los obstaculos se identifican como 4 en el mapa
    PorcObst=80   #80% del mapa son obstaculos
    Nobstaculo=int(NposT*PorcObst/100)        #numero de obstaculos en la matriz mapa
    print ("Numero de obstaculos", Nobstaculo)
    for i in range (Nobstaculo):
        x=random.randint(0, map.shape[0]-1) #generamos las 6 coordenadas aleatorias en donde se colocara un obstaculo
        y=random.randint(0, map.shape[1]-1)
        z=random.randint(0, map.shape[2]-1)
        xx=random.randint(0, map.shape[3]-1)
        yy=random.randint(0, map.shape[4]-1)
        zz=random.randint(0, map.shape[5]-1)
        if map[x,y,z,xx,yy,zz]==0:         #'0' corresponde a posiciones vacias en el mapa
            map[x,y,z,xx,yy,zz]=obstaculo  #creamos un obstaculo en la posicion aleatoria

    solution = a_star(map,inicio,fin)  #llamamos a la funcion A* indicando el mapa, el inicio y el fin
    print("Camino optimo:")
    print(solution)

if __name__ == "__main__":
    main()
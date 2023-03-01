from Ffitness import *
import random

class Individuo:
    def __init__(self,name=None, orden=None):
        self.name=name
        self.orden = orden
        self.fitness = 0
        self.prob= 0

def get_fitness(Individuo):    #solo se usa para hacer el sorting de nodos.f (en simples paralabras:ordena los nodos de acuerdo al f)
      return Individuo.fitness

print("Inicio de programa")

MatrizCosto=np.loadtxt('MatrizCosto.txt',skiprows=0) #carga la matriz de costos generada en a*
CostoBaseCarga=np.loadtxt('costoBase.txt',skiprows=0) #carga el vector generado en a*
ListaPedidos=np.array([[1,22,37,42,53],
                       [63,71,82,94,10],
                       [11,22,39,41,55],
                       [19,23,31,49,57],
                       [45,82,93,64,75]]) #Cargamos la lista de pedidos(5 pedidos de 5 productos)

""" 
    Generamos la poblacion inicial (inicializacion)
"""
IndInicial=np.arange(1,101,dtype=int) #Vector que contiene los 100 productos ordenados de 1 a 100
TamañoPoblacion=4 #4 individuos por poblacion
poblacion=np.zeros((TamañoPoblacion,size(IndInicial)),dtype=int)
for i in range(TamañoPoblacion):
    np.random.shuffle(IndInicial) #Los 100 productos ordenados aleatoriamente
    poblacion[i,:]=IndInicial

MaxIterr=10    #se eligieron 10 generaciones arbitrariamente
iteracion=0

mejor_fitness=10000 #Le asignamos valores grandes para que tomen el primer valor
fitness_act=10000

parar=False
while(parar==False):
    print('---------------------Iteracion '+str(iteracion+1))
    "Inicializacion de individuos"
    Uno=Individuo('Uno', poblacion[0,:])
    Dos=Individuo('Dos', poblacion[1,:])
    Tres=Individuo('Tres', poblacion[2,:])
    Cuatro=Individuo('Cuatro', poblacion[3,:])

    "Fitness"
    #Creamos un vector que almacena los resultados de todos los indivudios(generacion)
    fitness=np.zeros(TamañoPoblacion)
    #Hacemos el itercambio de filas en las matrices de Costo y Costo-base para que coincidan con cada individuo
    print('Calculando Fitness')
    N_Individuo=0
    MatrizCosto_Aux=np.array(MatrizCosto)
    CostoBaseCarga_Aux=np.array(CostoBaseCarga)
    Costos=zeros(size(ListaPedidos, 0))
    while (N_Individuo<TamañoPoblacion):
        N_Producto=0
        N_Pedido=0
        #Fitness almacena los costos minimos de cada fila de la lista de pedidos
        while N_Producto<np.size(IndInicial):
            MatrizCosto_Aux[N_Producto,:]=MatrizCosto[poblacion[N_Individuo][N_Producto]-1,:]
            CostoBaseCarga_Aux[N_Producto]=CostoBaseCarga[poblacion[N_Individuo][N_Producto]-1]
            N_Producto+=1
        while N_Pedido<np.size(ListaPedidos,0):
            #Operamos con la fila k de la lista de pedidos
            SolucionInicial=ListaPedidos[N_Pedido,:]   #solucion inicial de lista de ordenes
            SolucionInicial=elimina_ceros(SolucionInicial) #eliminamos los ceros de la lista
            Costos[N_Pedido]=TempleSimulado(10,0.5,0.99999,SolucionInicial,MatrizCosto_Aux,CostoBaseCarga_Aux)
            N_Pedido+=1
        fitness[N_Individuo]=promedio(Costos) #Fitness del almacen
        N_Individuo+=1
    #En caso de q el temple simulado arroje un peor fitness al mismo mejor individuo de la generacion anterior salvamos el mejor fitness
    if fitness_act<fitness[0]:
        fitness[0]=fitness_act
    #Asignamos el resultado a cada Individuo
    Uno.fitness=fitness[0]
    Dos.fitness=fitness[1]
    Tres.fitness=fitness[2]
    Cuatro.fitness=fitness[3]
    #Los ordenamos segun el fitness
    Orden = []
    Orden.append(Uno) 
    Orden.append(Dos) 
    Orden.append(Tres) 
    Orden.append(Cuatro) 

    "FITNESS INDIVIDUOS:"
    Orden.sort(key=get_fitness)
    
    print("FITNESS INDIVIDUOS:")
    for obj in Orden:
        print('Objeto',obj.name,'con fitness',obj.fitness)

    print('Mejor Individuo de la generacion con fitness '+ str(Orden[0].fitness))
    print(Orden[0].orden)

    "Seleccion del mejor individuo"
    mejor_fitness=Orden[0].fitness
    mejor_orden=Orden[0].orden

    "PARADA"
    iteracion+=1
    if(iteracion==MaxIterr):
        parar=True

    "EVOLUCION"
    if(parar==False):
        "PROBABILIDAD DE SELECCION DE INDIVIDUOS DE ACUERDO AL FITNESS:"
        #Sum=Orden[0].fitness+Orden[1].fitness+Orden[2].fitness+Orden[3].fitness
        #Buscamos que el de menor fitness tenga mas probabilidades
        Orden[0].prob=70
        Orden[1].prob=25
        Orden[2].prob=3
        Orden[3].prob=2
        #for obj in Orden:
        #   print('Objeto',obj.name,'con fitness',obj.fitness,'con probabilidad',obj.prob)
        "CANDIDATOS:"
        #Obtenemos los candidatos
        num=random.randint(0, 100)
        Candidatos=[]
        while (size(Candidatos)<4):
            if   num<Orden[0].prob:
                Candidatos.append(Orden[0])
            elif num<Orden[0].prob+Orden[1].prob:
                Candidatos.append(Orden[1])
            elif num<Orden[0].prob+Orden[1].prob+Orden[2].prob:
                Candidatos.append(Orden[2])
            elif num<Orden[0].prob+Orden[1].prob+Orden[2].prob+Orden[3].prob:
                Candidatos.append(Orden[3])
            num=random.randint(0, 100)
        
        print('Candidatos')
        for obj in Candidatos:
            print(obj.name, obj.fitness)

        "El mejor individuo pasa directamente a la siguiente generacion"
        N_Individuos=0 #Numero de individuos actuales para la sig generacion
        print('Pasando el mejor individuo como individuo 1 de la sig generacion')
        poblacion[0,:]=Orden[0].orden
        N_Individuos+=1
        
        "Cruce de orden (ya q los productos no pueden repetirse)"
        #Obtenemos el par que se va a cruzar
        PAR=[]
        seguir=True
        i=1
        while(seguir==True):
            if Candidatos[0].name!=Candidatos[i].name:
                PAR.append(Candidatos[0])
                PAR.append(Candidatos[i])
                print('PAR a cruzar:',PAR[0].name, PAR[1].name)
                #Hacemos el cruce de orden
                print('Haciendo cruce para individuo '+str(N_Individuos+1))
                poblacion[N_Individuos,:]=cruzar(PAR[0].orden,PAR[1].orden)
                N_Individuos+=1
                print('Haciendo cruce para individuo '+str(N_Individuos+1))
                poblacion[N_Individuos,:]=cruzar(PAR[1].orden,PAR[0].orden)
                N_Individuos+=1
                seguir=False
            i+=1
            if i==size(Candidatos):
                seguir=False    

        "Mutamos (este problema solo admite permutaciones ya que los pruductos solo ocupan una unica posicion)"
        #Si faltan individuos en la nueva generacion mutamos alguno de los candidatos
        while(N_Individuos<4):
            print('Haciendo mutacion para individuo '+str(N_Individuos+1))
            N_permutacion=0
            #Elegimos 10 permutaciones de genes por mutacion (intercambio)
            while(N_permutacion<10):
                poblacion[N_Individuos,:]=cambioPos(Candidatos[N_Individuos-1].orden, size(Candidatos[N_Individuos-1].orden))
                N_permutacion+=1
            N_Individuos+=1
            
print('---------------------Resultado Final')
print('Mejor Individuo con fitness '+ str(mejor_fitness))
print(mejor_orden)

print("fin de programa")
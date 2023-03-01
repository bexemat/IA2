#Se deben realizar 10 tareas T1,T2,...,T10
#Cada tarea tiene una duracion especifica
#Se tienen 3 Maquinas y no pueden hacer mas de una tarea a la vez
#Cada tarea puede realizarse por una maquina en especifico

import random              #permite trabajar con funciones q generan valores aleatorios

class Tarea:
    def __init__(self, Nombre=None, Duracion_Max=None, N_Maquinas=None):
        self.Nombre = 'Tarea '+str(Nombre)
        self.Duracion = random.randint(1,Duracion_Max)
        self.Tipo = random.randint(1,N_Maquinas)
        self.maquina=None
        self.Tiempo=None
        self.Estado='Incompleta'

class Maquina:
    def __init__(self, Nombre=None, Tipo=None):
        self.Nombre = 'Maquina '+str(Nombre)
        self.Numero = Nombre
        self.Tipo=Tipo
        self.Estado = 'Disponible'
        self.Tiempo=''

class Tipo:
    def __init__(self, Nombre=None, Cantidad=None):
        self.Nombre = Nombre
        self.Cantidad= Cantidad

def get_cantidad(Tipo):    #para obtener la cantidad de un mismo tipo
    return Tipo.Cantidad

def Busqueda_CSP(Tareas, Maquinas, N_tipos):
    OPEN= []   #Lista de tareas por realizar
    SOLUCION=[]  #Lista de tareas que se estan realizando
    #La siguiente variable a asignar será aquella que tenga menos valores posibles en su dominio
    #En este caso son las tareas q necesitan del tipo de maquina que hay en menor cantidad
    contador=[]     #Cantidad de maquinas de cada tipo
    for i in range(N_tipos):
        contador.append(Tipo(i+1,0))
        for Maquina in Maquinas:
            if Maquina.Tipo==contador[i].Nombre:
                contador[i].Cantidad+=1
    #ordena los tipos de acuerdo a la cantidad
    contador.sort(key=get_cantidad)    
    
    #Ordenamos las tareas de acuerdo a la disponibilidad de maquinas
    aux=[]
    for tipo in contador:
        for Tarea in Tareas:
            if Tarea.Tipo==tipo.Nombre:
                aux.append(Tarea)

    print('Lista de tareas ordenadas de acuerdo a prioridad')
    OPEN=aux       #Inicialmente todas las tareas estan en la lista por realizar
    for tarea in OPEN:
        print(tarea.Nombre+'  Duracion:'+str(tarea.Duracion)+'  Tipo de tarea:'+str(tarea.Tipo))
    print()

    #Si aun la asignacion no es completa se sigue con el codigo
    tiempo=0
    while(OPEN!=[]): #Si la asignacion es completa -> devolvemos la solucion encontrada
        #Seleccionamos un par maquina disponible y una tarea pendiente
        Asignacion_maquina=False
        Asignacion_tarea=False
        for maquina in Maquinas:
            if Asignacion_maquina==False and maquina.Estado=='Disponible':
                for tarea in OPEN:
                    if Asignacion_tarea==False and tarea.Tipo==maquina.Tipo:
                        maquina.Estado='Ocupada'
                        
                        tarea.Tiempo=tiempo
                        tarea.maquina=maquina.Numero

                        SOLUCION.append(maquina)
                        SOLUCION.append(tarea)
                        OPEN.remove(tarea)

                        Asignacion_maquina=True
                        Asignacion_tarea=True
        
        if OPEN==[]:
            return(SOLUCION)
        
        #Si no se pueden asignar tareas ni maquinas entonces esperamos hasta que se desocupe una maquina
        if Asignacion_maquina==False and Asignacion_tarea==False:
            Min_duracion=1000
            for tarea in SOLUCION:
                if tarea.Estado=='Incompleta' and tarea.Duracion<Min_duracion:
                    Min_duracion=tarea.Duracion
                    i=SOLUCION.index(tarea)
            
            SOLUCION[i].Estado='Completa'
            tiempo=tiempo+SOLUCION[i].Duracion
            Maquinas[SOLUCION[i].maquina-1].Estado='Disponible'

            for tarea in SOLUCION:
                if tarea.Estado=='Incompleta':
                    tarea.Duracion=tarea.Duracion-SOLUCION[i].Duracion

def main():
    print("Ejercicio 5")
    N_Tareas=10       #Elegimos el numero de tareas q se deben realizar
    N_Tipos=3         #Tipos de tareas y maquinas (Una tarea solo puede ser realizada por una maquina del mismo tipo)
    Duracion_max=20   #Duracion maxima que puede tomar una tarea
    N_Maquinas=5      #Numero de maquinas

    print('Lista de tareas')
    Tareas=[]         #Lista q almacena las tareas
    for i in range (1,N_Tareas+1):
        Tareas.append(Tarea(i,Duracion_max,N_Tipos))
        print(Tareas[i-1].Nombre+'  Duracion:'+str(Tareas[i-1].Duracion)+'  Tipo de tarea:'+str(Tareas[i-1].Tipo))
    print()

    print('Lista de maquinas')
    Maquinas=[]         #Lista q almacena las maquinas
    for i in range (1,N_Maquinas+1):  #Generamos las maquinas
        if i<=N_Tipos:                #Generamos al menos una maquina de cada tipo
            Maquinas.append(Maquina(i,i))
            print(Maquinas[i-1].Nombre+'    Tipo de maquina:'+str(Maquinas[i-1].Tipo))
        else:                         #El resto de maquinas pueden ser de cualquier tipo
            j=random.randint(1,N_Tipos)
            Maquinas.append(Maquina(i,j))
            print(Maquinas[i-1].Nombre+'    Tipo de maquina:'+str(Maquinas[i-1].Tipo))
    print()

    solucion=Busqueda_CSP(Tareas,Maquinas,N_Tipos)
    print('Solucion:')
    for nodo in solucion:
        if nodo.Tiempo=='':
            print('La '+nodo.Nombre+' realiza')
        else:
            print('la '+nodo.Nombre+' que comienza en el segundo '+ str(nodo.Tiempo))
            print()
    
if __name__ == "__main__":
    main()
import numpy as np
from numpy import *
import random as rd
from matplotlib import pyplot as plt
import math

#Esta funcion crea un vector q almacena la cantidad de productos q hay por pedido
def cantidadProductosLista(a,cantidadElementosFila):
    j=0
    cant=np.zeros(100)  #formamos un vector que contiene la cantidad de productos por fila de la lista(antes de que comiencen los 0)
    while(j<100):
        i=0
        aux=0
        while(i<cantidadElementosFila):
            if(a[j][i]!=0):
                aux+=1
            i+=1
        cant[j]=aux
        j+=1
    return (cant) #retornamos el vector que contiene la cantidad de productos por fila que no sean 0

#Esta funcion cambia la posicion de 2 productos aleatoriamente
def cambioPos(vector,cant):
    i=0
    ind=np.random.randint(1,cant,size=2)
    while(i<2):    #este while es para evitar que haya salido aleatoriamente el mismo numero por ej(4,4)       
        if(i==1):
            while(ind[i]==ind[i-1]):
                ind[i]=np.random.randint(1,cant,size=1)             
        i+=1
    #intercambia 2 posiciones del vector individuo
    aux=vector[ind[0]]    
    vector[ind[0]]=vector[ind[1]]
    vector[ind[1]]=aux  
    return vector

def cruzar(Padre1,Padre2):    
    Cruce1=0
    Cruce2=0
    while(Cruce1==Cruce2):
        Cruce1=random.randint(0,size(Padre1)-1)
        Cruce2=random.randint(Cruce1,size(Padre1)-1)

    Hijo=zeros(size(Padre1),dtype=int)
    Hijo[Cruce1:Cruce2]=Padre2[Cruce1:Cruce2]
    
    ProdNoRep=[]
    for producto in Padre1:
        Exist = producto in Hijo
        if Exist==False:
            ProdNoRep.append(producto)

    i=Cruce2
    j=0
    while(i<size(Hijo)):
        Hijo[i]=ProdNoRep[j]
        i+=1
        j+=1
        
    i=0
    while(i<Cruce1):
        Hijo[i]=ProdNoRep[j]
        i+=1
        j+=1
    return Hijo


def modificaActual(a,cant):
    k=0
    c=np.zeros((100,28))
    while(k<100):
        c[k]=(cambioPos(a[k],cant[k]))
        k+=1
    return c

def promedio(fitness):
    i=0
    aux=0
    while(i<size(fitness)):
        aux+=fitness[i]
        i+=1
    fitness=aux/size(fitness)
    return fitness

def TempleSimulado(TempInicial,TempFinal,SecEnfr,SolucionInicial, MatrizCosto, CostoBaseCarga):
    Temp=TempInicial
    iter=1
    Sact=CostoActual(SolucionInicial, MatrizCosto, CostoBaseCarga)  
    #Mejor costo y mejor solucion
    Mcosto=Sact
    Msol=SolucionInicial
    
    #print('La distancia inicial es:'+str(Sact)+' con la lista inicial: '+str(SolucionInicial))
    SolucionActual=SolucionInicial  
    
    it_list = []
    prob_list = []
    temp_list=[]
    solucion_list=[]
    while True:
        it_list.append(iter)
        temp_list.append(Temp)
        solucion_list.append(Sact)
            
        #Si se llega a la temp final o se supera el numero de iteraciones
        if(Temp<TempFinal):
            minDist=Mcosto
            #print("distancia minima: "+str(Mcosto)+' con la lista: '+str(Msol))
            #plt.plot(it_list,temp_list) #grafica temperatura
            #plt.show()
            #plt.plot(it_list,solucion_list) #grafica costos de solucion
            #plt.show()
            return minDist

        #Si no se llega a la temp final o se supera el numero de iteraciones
        SolucionCandidato=intercambiarPosicion(SolucionActual)
        Scand=CostoActual(SolucionCandidato, MatrizCosto, CostoBaseCarga)
        if Scand<Mcosto:
            Mcosto=Scand
            Msol=SolucionCandidato
        #print(Scand)
        delta=Scand-Sact
        #Si la solucion es mejor, se acepta
        if(delta<=0):
            SolucionActual=SolucionCandidato
        #Si la solucion no es mejor, acepta pero con una probabilidad de  e^(-cost/temp)
        else:               
            prob = math.exp(-delta / Temp)
            prob_list.append(prob)
            if rd.uniform(0, 1) < prob:
                SolucionActual = SolucionCandidato
        Sact=CostoActual(SolucionActual, MatrizCosto, CostoBaseCarga)
        Temp=Temp*SecEnfr
        iter+=1

#Esta funcion intercambia dos elementos de la lista del recorrido al alzar
def intercambiarPosicion(Sol):
    aux_list = Sol.copy()
    idx = range(len(aux_list))
    i1, i2 = rd.sample(idx, 2)
    aux_list[i1], aux_list[i2] = aux_list[i2], aux_list[i1]
    return aux_list

#Esta funcion calcula el costo del recorrido de la lista
def CostoActual(Sact, MatrizCosto, CostoBaseCarga):
    i=0
    CostoTotal=0
    while(i<size(Sact)):
        if(i==0):
            CostoTotal=CostoTotal+CostoBaseCarga[Sact[i]-1] #Sale de la posicion incial
        elif(i!=0 and i!=size(Sact)-1):                           
            CostoTotal=CostoTotal+MatrizCosto[Sact[i]-1][Sact[i+1]-1] #Va de un producto al otro
        elif(i==size(Sact)-1):
            CostoTotal=CostoTotal+CostoBaseCarga[Sact[i]-1] #vuelve a la posicion inicial
        i=i+1
    return (CostoTotal)

#Esta funcion elimina los ceros de un vector
def elimina_ceros(original): 
        nueva = []
        for dato in original:
            if dato != 0:
                nueva.append(dato)
        return nueva
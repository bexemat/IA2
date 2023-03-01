import numpy as np
import random as rd
from matplotlib import pyplot as plt
import math
from numpy import *
MatrizCosto=np.loadtxt('MatrizCosto.txt',skiprows=0) #carga la matriz de costos generada en a*
CostoBaseCarga=np.loadtxt('costoBase.txt',skiprows=0) #carga el vector generado en a*
ListaPedidos=np.loadtxt('listaPedidos.txt',dtype="int",skiprows=0) #Cargamos la lista de pedidos

#Esta funcion elimina los ceros de un vector
def elimina_ceros(original): 
        nueva = []
        for dato in original:
            if dato != 0:
                nueva.append(dato)
        return nueva

#Esta funcion intercambia dos elementos de la lista del recorrido al alzar
def intercambiarPosicion(Sol):
    aux_list = Sol.copy()
    idx = range(len(aux_list))
    i1, i2 = rd.sample(idx, 2)
    aux_list[i1], aux_list[i2] = aux_list[i2], aux_list[i1]
    return aux_list

#Esta funcion calcula el costo del recorrido de la lista
def CostoActual(Sact):
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

def TempleSimulado(TempInicial,TempFinal,SecEnfr,SolucionInicial):
    Temp=TempInicial
    iter=1
    Sact=CostoActual(SolucionInicial)  
    #Mejor costo y mejor solucion
    Msol=SolucionInicial
    Mcosto=Sact
    
    print('La distancia inicial es '+str(Sact)+' con la lista inicial: '+str(SolucionInicial))
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
            print("distancia minima: "+str(Mcosto)+' con la lista: '+str(Msol))
            #plt.plot(it_list,temp_list) #grafica temperatura
            #plt.show()
            plt.plot(it_list,solucion_list) #grafica costos de solucion
            plt.show()
            return (minDist)

        #Si no se llega a la temp final o se supera el numero de iteraciones
        SolucionCandidato=intercambiarPosicion(SolucionActual)
        Scand=CostoActual(SolucionCandidato)
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
        Sact=CostoActual(SolucionActual)
        Temp=Temp*SecEnfr
        iter+=1

for Nlist in range(size(ListaPedidos[1])):    #Recorremos todas las listas
    print('Lista: '+str(Nlist+1))
    SolucionInicial=ListaPedidos[Nlist,:]   #solucion inicial de lista de ordenes
    SolucionInicial=elimina_ceros(SolucionInicial) #eliminamos los ceros de la lista
    #Buenos resultados: Tinicial=10 Tfinal=0.5 Enfriamiento=0.99999
    Tinicial=10
    Tfinal=0.5
    Enfriamiento=0.99999
    TempleSimulado(Tinicial,Tfinal,Enfriamiento,SolucionInicial)
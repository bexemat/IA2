'''
    Se calculan todos las distancias optimas y se las introduce a una matriz de la siguiente forma
        elemento [0][0]=distancia de ir del producto 1 al producto 1
        elemento [3][40]=distancia de ir del producto 4 al 41
    Tambien se calcula un vector el cual nos otorga la distancia que hay de la posicion 
    deseada a la estacion de carga
        
'''
from Aestrella import *
import pandas as pd
import numpy as np

def CalculoCosto(map):
    print('Calculando costos')
    productos=np.max(map)  #Cantidad de productos
    costoPosBaseCarga=np.array(zeros(productos)) #vector de 72 de ceros
    MatrizCostos=np.zeros((productos, productos)) #matriz de 72 de ceros 
                          
    k=0
    while(k<productos):
        a=-1 #La base se indica con -1
        b=k+1
        print('Costo de base a producto:'+str(b))
        costo=a_star(map,a,b)
        costoPosBaseCarga[k]=costo  #En esta matriz se almacenan las distancias desde la base a cada uno de los 100 productos
        k=k+1     
    np.savetxt('costoBase.txt',costoPosBaseCarga,'%d')
    CB=pd.DataFrame(data=costoPosBaseCarga)
    CB.to_csv('costoBase.csv',sep=' ',header=False,index=False,float_format='%d')

    
    #calcula matriz de 100x100
    j=0
    while(j<(productos)):
        i=0   
        while(i<(productos)):       
            a=j+1 #inicio   
            b=i+1 #fin    
            print('Costo a productos desde pruducto '+str(a)+' a producto '+str(b))
            
            if a>b:  #como la distancia de A a B es igual a la de B a A...
                MatrizCostos[j][i]=MatrizCostos[i][j]
            else:
                costo = a_star(map,a,b)        
                MatrizCostos[j][i]=costo  #En esta matriz se almacenan las distancias entre los distintos productos
            i=i+1            
        j=j+1 
    
    np.savetxt('MatrizCosto.txt',MatrizCostos,fmt='%d')
    MC=pd.DataFrame(data=MatrizCostos)
    MC.to_csv('MatrizCosto.csv',sep=' ',header=False,index=False,float_format='%d')

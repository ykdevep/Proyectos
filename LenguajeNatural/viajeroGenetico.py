import numpy as np
import random as rnd

## Se definen 5 ciudades identificadas con números...
## Se trabajan con las ciudadesde 2 a 5 porque siempre se sale y se regresa a 1...

##      Matriz de distancias...
##     --  1    2   3   4   5
##      1  0    10  15  18  24
##      2  10   0   20  18  13
##      3  15   20  0   21  28
##      4  18   18  21  0   16
##      5  24   13  28  16  0

distanciaEntreCiudades = [[0, 10, 15, 18, 24],
                          [10, 0, 20, 18, 13],
                          [15, 20, 0, 21, 28],
                          [18, 18, 21, 0, 16],
                          [24, 13, 28, 16, 0]]

tamanno = 3

## PoblacionInicial(tamannoPoblacion)  -->> Genera una población (RUTAS) de tamaño especificado

def PoblacionInicial(tamannoPoblacion):
    poblacion = np.zeros((tamannoPoblacion, 4))
    print (poblacion)

    longitud = len(poblacion)

    for fila in range(0,longitud):
        listaValores = [0, 0, 0, 0]
        for columna in range(0,4):
            ciudadCamino = rnd.randint(2, 5)
            marcado = 0
            temporal = listaValores[ciudadCamino - 2]
            while (marcado != 1):
                if (temporal == 0):
                    poblacion[fila, columna] = ciudadCamino
                    listaValores[ciudadCamino - 2] = 1
                    marcado = 1
                else:
                    ciudadCamino = rnd.randint(2, 5)
                    temporal = listaValores[ciudadCamino - 2]
                                 
    return poblacion

def DeterminarDistanciaTotal(tamannoPoblacion, distanciaCiudades, poblacion):
    distanciaTotal = np.zeros((tamannoPoblacion, 1))
    print("Valor original de suma " + str(distanciaTotal))
    for distancia in range(0, tamannoPoblacion):
        segundoValor = int(poblacion[distancia, 0]) 
        distanciaTotal[distancia, 0] += distanciaEntreCiudades[distancia][segundoValor - 1]
        for ciudades in range (1, 4):
            primerValor = int(poblacion[ciudades - 1, 0])
            distanciaTotal[distancia, 0] += distanciaEntreCiudades[primerValor - 1][ciudades + 1]
        distanciaTotal[distancia] += distanciaEntreCiudades[tamannoPoblacion][0]

    return distanciaTotal







var = PoblacionInicial(tamanno)
print (var)
distancia = DeterminarDistanciaTotal(tamanno, distanciaEntreCiudades, var)
print ("   ")
print(distancia)

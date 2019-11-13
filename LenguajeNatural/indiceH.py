##
## -> El índice H es usado para la medición de la calidad profesional de los científicos.
## -> Se determina en función de la cantidad de citas que han recibido los artículos de un científico.
## -> Un científico tiene un índice H si a publicado H trabajos con al menos H citas cada uno.
## -> Existe la librería de Python "scholarmetrics" que implementa un algoritmo para el calcular
##           el índice H.
##
## -> Algoritmo para el cálculo del índice H.
## -> Se lee una lista que contiene la cantidad de citas que tienen los artículos de un científico.
## -> Para la lectura de la lista se emplea la libreria pandas.
##

##
## -> Se cargan las librerias necesarias.
##

import pandas
from scholarmetrics import hindex

##
## -> Se lee un fichero en formato csv que contiene una sola columna con las citas de los artículos.
## -> Se utilizan las siguientes variables:
##                    direccionFichero  {Contiene la ruta del fichero a leer}
##                    citasArticulos    {Contiene la información del fichero}
##                    listadoCitas      {Información de variable "citasArticulos" en formato de lista}
##

direccionFichero = "C:/Users/eacar/Desktop/indiceH.csv"
citasArticulos = pandas.read_csv(direccionFichero)

if citasArticulos.empty: #Validando si los datos fueron cargados...
    print ("    ")
    print ("Fichero se encuentra vacío, por favor verifique que sea el correcto...")
else:
    print ("    ")
    print ("Fichero cargado exitosamente...")

listadoCitas = []
for i in range(len(citasArticulos)):
    listadoCitas.append(citasArticulos.iloc[i,0])

##
## -> Se muestra la información extraida del fichero csv.
##

print("   ")
print ("La cantidad de citas por publicación es la siguiente: ")
for i in range(len(listadoCitas)):
    print (str(listadoCitas[i]))

##
## -> Se procede a realizar el cálculo del índice H.
## -> El algoritmo realiza las siguientes acciones:
##                      1. Si la lista no contiene elementos el valor es cero.
##                      2. Se ordena la lista en orden decreciente.
##                      3. El valor será el valor máximo que satisface listadoCitas[i] >= i + 1.
##

indiceHTemporal = len(listadoCitas)
if (indiceHTemporal == 0):
    indiceH = 0

listadoCitas = sorted(listadoCitas, reverse = True)
i = 0
while (i < indiceHTemporal and listadoCitas[i] >= (i + 1)):
    i += 1

indiceH = i

##
## -> Se determina el valor del índice H a partir de mismos valores de entrada con librería python.
## -> Se comparan ambos resultados.
##

print ("   ")
print ("El índice H del científico es: " + str(indiceH))
print ("El índice H usando la librería de Python scholarmetrics es: " + str(hindex(listadoCitas)))

if (indiceH == hindex(listadoCitas)):
    print ("Los resultados obtenidos son iguales.")
else:
    print ("Error: Los resultados son diferentes.")

##
## -> Probando con una lista de valores generada aleatoriamente.
## -> Se emplearán valores entre 0 y 10 y un total de 10 valores.
##

import random
listaAleatorio = []

for i in range (10):
    listaAleatorio.append(random.randint(0, 10)) 

print("   ")
print ("La cantidad de citas por publicación es la siguiente: ")
for i in range(len(listaAleatorio)):
    print (str(listaAleatorio[i]))


indiceHTemporal = len(listaAleatorio)
if (indiceHTemporal == 0):
    indiceH = 0

listaAleatorio = sorted(listaAleatorio, reverse = True)
i = 0
while (i < indiceHTemporal and listaAleatorio[i] >= (i + 1)):
    i += 1

indiceH = i

##
## -> Se determina el valor del índice H a partir de mismos valores de entrada con librería python.
## -> Se comparan ambos resultados.
##

print ("   ")
print ("El índice H del científico es: " + str(indiceH))
print ("El índice H usando la librería de Python scholarmetrics es: " + str(hindex(listaAleatorio)))

if (indiceH == hindex(listaAleatorio)):
    print ("Los resultados obtenidos son iguales.")
else:
    print ("Error: Los resultados son diferentes.")



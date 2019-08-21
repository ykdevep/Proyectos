

import pandas as panda
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime


direccionFichero = "C:/Users/eacar/Desktop/ubic.json"
json = panda.read_json(direccionFichero)

print ("    ")
print ("Cargando fichero de contaminantes CO, puede tardar un momento, por favor espere...")
if json.empty: #Validando si los datos fueron cargados...
    print ("    ")
    print ("Fichero se encuentra vacío, por favor verifique que sea el correcto...")
else:
    print ("    ")
    print ("Fichero cargado exitosamente...")

######################################################################################################################
##                                                                                                                  ##
##                       Mostrando los primeros 5 valores cargados de cada uno de los ficheros...                   ##
##                        Mostrando los últimos 5 valores cargados de cada uno de los ficheros...                   ##
##                                                                                                                  ##
######################################################################################################################

print ("Imprimiendo los primeros 5 registros del registro de contaminantes CO...")
print (json.head(5))

print ("    ")
print ("Imprimiendo los últimos 5 registros del registro de contaminantes CO...")
print (json.tail(5))

######################################################################################################################
##                                                                                                                  ##
##                          Determinando cantidad de campos vacíos en los datos...                                  ##
##                                                                                                                  ##
######################################################################################################################

print ("    ")
print ("En los datos existen la siguientes cantidad de datos vacíos:")
info = json.apply(lambda x: sum(x.isnull()),axis=0)
print (info)

######################################################################################################################
##                                                                                                                  ##
##                              Rellenando todos los valores vacios con el campo NULL...                            ##
##                 Esto es necesario para poder insertar correctamente los valores en la base de datos...           ##
##                                                                                                                  ##
######################################################################################################################

print ("    ")
print ("Rellenando los campos vacíos con el valor NULL ...")
xls = json.fillna("NULL")

print (" FIN ")


for i in range(0, 1):
    print (json.iloc[i,0])
    control = json.iloc[i,0]
    valor = []
    valor.append(json.iloc[i,0])

print ("  ")
print(valor)
print("")
print ("Imprimiendo control")
print (type(control))
print (len(control))
print (control)

datos =  control.values()

print ("Datos diccionario")
print (datos)

print ("LLaves del diccionario")
llaves = control.keys()
print (llaves)

print ("Datos 1")
print (datos[0])



print (" FIN 2 ")
    
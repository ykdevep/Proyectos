

import pandas as panda
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
import time as pruebaTiempo


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


for i in range(0, 2):
    print (json.iloc[i])
    control = json.iloc[i,0]
    marcaTiempo = control['timestampMs']
    latitud = control['latitudeE7']
    longitud = control['longitudeE7']
    print ("Imprimiendo valores:")
    print ("tiempo:")
    print (marcaTiempo)
    tiempo2 = marcaTiempo[0:10]
    print (type(tiempo2))
    print (tiempo2)
    fecha = pruebaTiempo.ctime(int(tiempo2))
    fecha2 = datetime.fromtimestamp(int(tiempo2))
    print ("Fecha:")
    print (fecha)
    print (fecha2)
    print ("latitud:")
    print (latitud)
    print ("longitud:")
    print (longitud)

   
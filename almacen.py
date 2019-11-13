######################################################################################################################
##                                                                                                                  ##
##    Módulo Python 3.6.5 (32 bits) para leer un fichero xls y guardar la información en una base de datos MySQL    ##
##                                     mediante las librerías pandas y mysql                                        ##
##                                                                                                                  ##
##              Se leen los datos pertenecientes a los valores de longitud y latitud a partir de fichero json       ##
##                                                                                                                  ## 
##                Se muestran los primeros y últimos 5 registros para ver si la información es correcta             ##
##                            Se determina el número total de campos vacíos en los datos                            ##
##                                                                                                                  ##
##                                                 Versión 1.12.5                                                   ##
##                                          Fecha creación: 1/02/2018                                               ##
##                                        Última modificación: 19/04/2019                                           ##
##                                         Enrique Alfonso Carmona García                                           ##
##                                          eacarmona860920@gmail.com                                               ##
##                         La información relativa a la librería pandas puede ser consultada en:                    ##
##                                    http://pandas.pydata.org/pandas-docs/stable/index.html                        ##
##             La información relativa a la librería numpy (necesaria para pandas) puede ser consultada en:         ##
##                                          https://docs.scipy.org/doc/                                             ##
##                           La información relativa a mysql.conector puede ser consultada en:                      ##
##                                   https://dev.mysql.com/doc/connector-python/en/                                 ##
##                                    Se requiere  "pip install mysql-connector-python"                             ##
##                                                                                                                  ##
######################################################################################################################
 
######################################################################################################################
##                                                                                                                  ##
##                                      Cargando las librerías necesarias...                                        ##
##                                                                                                                  ##
###################################################################################################################### 

import pandas as panda
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
from geopy import distance

######################################################################################################################
##                                                                                                                  ##
##                                      Listado de variables utilizadas...                                          ##
##                                                                                                                  ##
## direccionFichero [Contiene la ruta donde se encuentra el fichero xls a leer]...                                  ##
##                                                                                                                  ##
## config [Contiene la información de configuración del servidor de base de datos MySQL]...                         ##
## nombreBd [Contiene el nombre de la base de datos]...                                                             ##
## tabla [Contiene las instrucciones SQL necesarias para crear las tablas en la base de datos]...                   ##
## datos [Contiene toda la información necesaria para insertar un nuevo registro en la base de datos]...            ##
## add [Contiene las instrucciones SQL para insertar un registro nuevo en la base de datos]...                      ##
## cnx [Para manejar la conección al servidor MySQL]...                                                             ##
## cursor [Para indicar las instrucciones al servidor MySQL]...                                                     ##
##                                                                                                                  ##
######################################################################################################################

######################################################################################################################
##                                                                                                                  ##
##                             Estableciendo las variables de configuración necesarias...                           ##
##                          Estableciendo la esctructura de las tablas en la base de datos...                       ##
##                                                                                                                  ##
######################################################################################################################

nombreBDAlmacen = 'almacen'  ## Configuración para la base de dato de localización gegráfica...
config = {
  'user': 'kike',
  'password': 'kike123',
  'host': '127.0.0.1',
  'database': 'almacen',
  'raise_on_warnings': True,
}

config2 = {
  'user': 'kike',
  'password': 'kike123',
  'host': '127.0.0.1',
  'database': 'estacionesmonitoreo',
  'raise_on_warnings': True,
}

tablaAlmacen = {} ## Definición de la tabla de localización...
tablaAlmacen[nombreBDAlmacen] = ( 
    "CREATE TABLE `almacendatos` ("
    "   `IDALDA` INT NOT NULL AUTO_INCREMENT,"
    "   `IDUSUARIO` INT NULL,"
    "   `FECHA` TIMESTAMP NULL,"
    "   `MARCATIEMPO` DOUBLE NULL,"
    "   `SO2` DOUBLE NULL,"
    "   `TORRESO2` TEXT NULL,"
    "   `NO2` DOUBLE NULL,"
    "   `TORRENO2` TEXT NULL,"
    "   `HR` DOUBLE NULL,"
    "   `TORREHR` TEXT NULL,"
    "   `TEMPAMB` DOUBLE NULL,"
    "   `TORRETEMPAMB` TEXT NULL,"
    "   `CO` DOUBLE NULL,"
    "   `TORRECO` TEXT NULL,"
    "   `NO` DOUBLE NULL,"
    "   `TORRENO` TEXT NULL,"
    "   `NOX` DOUBLE NULL,"
    "   `TORRENOX` TEXT NULL,"
    "   `O3` DOUBLE NULL,"
    "   `TORREO3` TEXT NULL,"
    "   `PM10` DOUBLE NULL,"
    "   `TORREPM10` TEXT NULL,"
    "   `PM25` DOUBLE NULL,"
    "   `TORREPM25` TEXT NULL,"
    "   `PA` DOUBLE NULL,"
    "   `TORREPA` TEXT NULL,"
    "   `RUVA` DOUBLE NULL,"
    "   `TORRERUVA` TEXT NULL,"
    "   `RUVB` DOUBLE NULL,"
    "   `TORRERUVB` TEXT NULL,"
    "   `BVP` DOUBLE NULL,"
    "   `EDA` DOUBLE NULL,"
    "   `RITMOCARD` DOUBLE NULL,"
    "   `TEMPCUERPO` DOUBLE NULL,"
    "   PRIMARY KEY (`IDALDA`));"
    "   ENGINE = InnoDB"
)

######################################################################################################################
##                                                                                                                  ##
##                   Creando una clase para convertir los tipos de datos a tipos MySQL...                           ##
##                                                                                                                  ##
######################################################################################################################

class NumpyMySQLConverter(mysql.connector.conversion.MySQLConverter):
    
    """ A mysql.connector Converter que es capaz de manejar los tipos de datos de Numpy """

    def _float32_to_mysql(self, value):
        return float(value)

    def _float64_to_mysql(self, value):
        return float(value)

    def _int32_to_mysql(self, value):
        return int(value)

    def _int64_to_mysql(self, value):
        return int(value) 

    def _timestamp_to_mysql(self, value):
        return datetime.timestamp(value)

######################################################################################################################
##                                                                                                                  ##
##                       Conectando al SGBD MySQL y creando las tablas definidas...                                 ##
##                                                                                                                  ##
######################################################################################################################

try:
    print ("Creando las variables de conexión...")
    cnx = mysql.connector.connect(**config)
    cnx1 = mysql.connector.connect(**config2)
    cnx.set_converter_class(NumpyMySQLConverter)
    cnx1.set_converter_class(NumpyMySQLConverter)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print ("   ")
    print("Su usuario o contraseña no son correctos, por favor verifique...")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print ("   ")
    print("No existe la base de datos, por favor verifique...")
  else:
    print ("   ")
    print(err)
else:
    print ("   ")
    print ("Conexión exitosa...")
    cursor = cnx.cursor()
    cursor1 = cnx1.cursor()

######################################################################################################################
##                                                                                                                  ##
##                           Función para crear la base de datos en el formato correspondiente...                   ##
##                                                                                                                  ##
######################################################################################################################

def create_database(cursor):  ## Función para la base de d...
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(nombreBDAlmacen))
    except mysql.connector.Error as err:
        print ("   ")
        print("Error al crear la base de datos señalada: {}".format(err))
        exit(1)

######################################################################################################################
##                                                                                                                  ##
##                                          Se solicita crear las base de datos...                                  ##
##                                                                                                                  ##
######################################################################################################################

try:  
    cnx.database = nombreBDAlmacen  
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = nombreBDAlmacen
    else:
        print ("   ")
        print(err)
        exit(1) 

######################################################################################################################
##                                                                                                                  ##
##                                  Se solicita crear todas las tablas definidas...                                 ##
##                                                                                                                  ##
######################################################################################################################

for name, ddl in tablaAlmacen.items():
    try:
        print ("   ")
        print("Creando la tabla {}: ".format(name), end='')
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print ("   ")
            print("Ya existe la base de datos...")
        else:
            print ("   ")
            print(err.msg)
    else:
        print ("   ")
        print("Tablas creadas...")









cursor.close()
cnx.close()
cursor1.close()
cnx1.close()





'''
newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
other = (41.45999, -81.957418)
print(distance.distance(newport_ri, cleveland_oh).miles)
print(distance.distance(newport_ri,cleveland_oh))
print(distance.distance(newport_ri, other).miles)
print(distance.distance(newport_ri,other))
valor = distance.distance(newport_ri, cleveland_oh)
valor2 = distance.distance(newport_ri, other)
print(type(valor))
print(valor)
print(valor2)

if (valor > valor2):
    print("Wl mayor es 1 " + str(valor))
else:
    print("EL mayor es 2 " + str(valor2))
'''



distanciaUsuarioATorre = {}

def MedicionDistancia(ubicacionUsuario, ubicacionTorre):
    distanciaUsuarioATorre.append(distance.distance(ubicacionUsuario, ubicacionTorre))



######################################################################################################################
##                                                                                                                  ##
##                                      Cargando las librerías necesarias...                                        ##
##                                                                                                                  ##
###################################################################################################################### 

import pandas as panda
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

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

nombreBDLoc = 'datawarehouse'  ## Configuración para la base de dato de localización gegráfica...
config = {
  'user': 'kike',
  'password': 'kike123',
  'host': '127.0.0.1',
  'database': 'datawarehouse',
  'raise_on_warnings': True,
}

tablaLoc = {} ## Definición de la tabla de localización...
tablaLoc[nombreBDLoc] = ( 
    "CREATE TABLE `tiempo` ("
    "   `IDTIEMPO` INT NOT NULL AUTO_INCREMENT,"
    "   `DIA` DOUBLE NULL,"
    "   `MES` DOUBLE NULL,"
    "   `ANNO` DOUBLE NULL,"
    "   `HORA` DOUBLE NULL,"
    "   `MINUTO` DOUBLE NULL,"
    "   `SEGUNDO` DOUBLE NULL,"
    "   PRIMARY KEY (`IDTIEMPO`));"
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
    cnx.set_converter_class(NumpyMySQLConverter)
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

######################################################################################################################
##                                                                                                                  ##
##                           Función para crear la base de datos en el formato correspondiente...                   ##
##                                                                                                                  ##
######################################################################################################################

def create_database(cursor):  ## Función para la base de d...
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(nombreBDLoc))
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
    cnx.database = nombreBDLoc  
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = nombreBDLoc
    else:
        print ("   ")
        print(err)
        exit(1) 

######################################################################################################################
##                                                                                                                  ##
##                                  Se solicita crear todas las tablas definidas...                                 ##
##                                                                                                                  ##
######################################################################################################################

for name, ddl in tablaLoc.items():
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

######################################################################################################################
##                                                                                                                  ##
##      Las variables corresponden a sus respectivos campos en la base de datos (Ver descripción anterior)...       ##
##         datosEgreso [Contiene la información necesaria para hacer la inserción en la base de datos]...           ##
##                 addEgreso [Consulta SQL que inserta la información en la base de datos]...                       ##
##                                                                                                                  ##
######################################################################################################################

dia = ""
mes = ""
anno = ""
hora = ""
minuto = ""
segundo = ""

datosTiempo = {
    'datoDia' : dia,
    'datoMes' : mes,
    'datoAnno' : anno,
    'datoHora' : hora,
    'datoMinuto' : minuto,
    'datoSegundo' : segundo,
}

addTiempo = ("INSERT INTO tiempo"
                "(DIA, MES, ANNO, HORA, MINUTO, SEGUNDO)"
                "VALUES (%(datoDia)s, %(datoMes)s, %(datoAnno)s, %(datoHora)s, %(datoMinuto)s, %(datoSegundo)s)"
            )

######################################################################################################################
##                                                                                                                  ##
##                             Se leen los valores del json y se asignan a las variables...                         ##
##                 Esto es necesario para poder insertar correctamente los valores en la base de datos...           ##
##                                                                                                                  ##
######################################################################################################################

valorTiempo = int(1527811200)
tiempo = datetime.fromtimestamp(valorTiempo)

for i in range(1, 308160):
    dia = tiempo.day
    mes = tiempo.month
    anno = tiempo.year
    hora = tiempo.hour
    minuto = tiempo.minute
    segundo = tiempo.second
    valorTiempo = valorTiempo + int(60)
    tiempo = datetime.fromtimestamp(valorTiempo)    

    datosTiempo = {
        'datoDia' : dia,
        'datoMes' : mes,
        'datoAnno' : anno,
        'datoHora' : hora,
        'datoMinuto' : minuto,
        'datoSegundo' : segundo,
        }
    
    print ("Insertando registro " + str(i) + " de " + str(308160))
    cursor.execute(addTiempo, datosTiempo)
    cnx.commit()
    print ("Registro " + str(i) +  " insertado, completado el " + str(int(i)*100/int(308160)) +  " porciento del total de datos")

######################################################################################################################
##                                                                                                                  ##
##                                     Cerrando las conexiones a la base de datos...                                ##
##                                                                                                                  ##
######################################################################################################################

print ("Se insertaron adecuadamente el 100 porciento de los datos del xls en la base de datos.")
cursor.close()
cnx.close()
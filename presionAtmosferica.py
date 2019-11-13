######################################################################################################################
##                                                                                                                  ##
##    Módulo Python 3.6.5 (32 bits) para leer un fichero xls y guardar la información en una base de datos MySQL    ##
##                                     mediante las librerías pandas y mysql                                        ##
##                                                                                                                  ##
##                   Se leen los datos pertenecientes a los valores de Presión Atmosférica (PA)                     ##
##                     de las estaciones de medición Ciudad de México y el Estado de México                         ##
##                  Actualmente se encuentran registrados los datos desde 01/01/2018 a 31/07/2019                   ##    
##                                                                                                                  ## 
##                Se muestran los primeros y últimos 5 registros para ver si la información es correcta             ##
##                            Se determina el número total de campos vacíos en los datos                            ##
##                         Los campos que no presentan medición se marcan con el valor '-99'                        ##
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

nombreBDPresionAtm = 'bancosexternos'  ## Configuración para la base de dato de contaminantes CO...
config = {
  'user': 'kike',
  'password': 'kike123',
  'host': '127.0.0.1',
  'database': 'bancosexternos',
  'raise_on_warnings': True,
}

tablaPresionAtm = {} ## Definición de la tabla de contaminantes CO...
tablaPresionAtm[nombreBDPresionAtm] = ( 
    "CREATE TABLE `presionatm` ("
    "   `IDPREATM` INT NOT NULL AUTO_INCREMENT,"
    "   `FECHA` TIMESTAMP NULL,"
    "   `HORA` INT NULL,"
    "   `AJM` DOUBLE NULL,"
    "   `CUT` DOUBLE NULL,"
    "   `HGM` DOUBLE NULL,"
    "   `INN` DOUBLE NULL,"
    "   `LAA` DOUBLE NULL,"
    "   `MER` DOUBLE NULL,"
    "   `MON` DOUBLE NULL,"
    "   `MPA` DOUBLE NULL,"
    "   `TLA` DOUBLE NULL,"
    "   `XAL` DOUBLE NULL,"
    "   PRIMARY KEY (`IDPREATM`));"
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
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(nombreBDPresionAtm))
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
    cnx.database = nombreBDPresionAtm  
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = nombreBDPresionAtm
    else:
        print ("   ")
        print(err)
        exit(1) 

######################################################################################################################
##                                                                                                                  ##
##                                  Se solicita crear todas las tablas definidas...                                 ##
##                                                                                                                  ##
######################################################################################################################

for name, ddl in tablaPresionAtm.items():
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
##                                       Cargando el fichero con la información...                                  ##
##                                                                                                                  ##
######################################################################################################################

direccionFichero = "C:/Users/eacar/Desktop/PA.xls"
xls = panda.read_excel(direccionFichero)

print ("    ")
print ("Cargando fichero de contaminantes CO, puede tardar un momento, por favor espere...")
if xls.empty: #Validando si los datos fueron cargados...
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
print (xls.head(5))

print ("    ")
print ("Imprimiendo los últimos 5 registros del registro de contaminantes CO...")
print (xls.tail(5))

######################################################################################################################
##                                                                                                                  ##
##                          Determinando cantidad de campos vacíos en los datos...                                  ##
##                                                                                                                  ##
######################################################################################################################

print ("    ")
print ("En los datos existen la siguientes cantidad de datos vacíos:")
info = xls.apply(lambda x: sum(x.isnull()),axis=0)
print (info)

######################################################################################################################
##                                                                                                                  ##
##                              Rellenando todos los valores vacios con el campo NULL...                            ##
##                 Esto es necesario para poder insertar correctamente los valores en la base de datos...           ##
##                                                                                                                  ##
######################################################################################################################

print ("    ")
print ("Rellenando los campos vacíos con el valor NULL ...")
xls = xls.fillna("NULL")

######################################################################################################################
##                                                                                                                  ##
##      Las variables corresponden a sus respectivos campos en la base de datos (Ver descripción anterior)...       ##
##           datosPA [Contiene la información necesaria para hacer la inserción en la base de datos]...             ##
##                    addPA [Consulta SQL que inserta la información en la base de datos]...                        ##
##                                                                                                                  ##
######################################################################################################################

fecha = ""
hora = ""
ajm = ""
cut = ""
hgm = ""
inn = ""
laa = ""
mer = ""
mon = ""
mpa = ""
tla = ""
xal = ""

datosPA = {
    'datoFecha' : fecha,
    'datoHora' : hora,
    'datoAJM' : ajm,
    'datoCUT' : cut,
    'datoHGM' : hgm,
    'datoINN' : inn,
    'datoLAA' : laa,
    'datoMER' : mer,
    'datoMON' : mon,
    'datoMPA' : mpa,
    'datoTLA' : tla,
    'datoXAL' : xal,
}

addPA = ("INSERT INTO presionatm"
                "(FECHA, HORA, AJM, CUT, HGM, INN, LAA, MER, MON, MPA, TLA, XAL)"
                "VALUES (%(datoFecha)s, %(datoHora)s, %(datoAJM)s, %(datoCUT)s, %(datoHGM)s, %(datoINN)s, %(datoLAA)s, %(datoMER)s, %(datoMON)s, %(datoMPA)s, %(datoTLA)s, %(datoXAL)s)"
            )

######################################################################################################################
##                                                                                                                  ##
##                             Se leen los valores del xls y se asignan a las variables...                          ##
##                 Esto es necesario para poder insertar correctamente los valores en la base de datos...           ##
##                                                                                                                  ##
######################################################################################################################

for i in range(0, len(xls)):
    fecha = datetime.date(xls.iloc[i,0])
    hora = xls.iloc[i,1]
    ajm = xls.iloc[i,2]
    cut = xls.iloc[i,3]
    hgm = xls.iloc[i,4]
    inn = xls.iloc[i,5]
    laa = xls.iloc[i,6]
    mer = xls.iloc[i,7]
    mon = xls.iloc[i,8]
    mpa = xls.iloc[i,9]
    tla = xls.iloc[i,10]
    xal = xls.iloc[i,11]
    
    datosPA = {
    'datoFecha' : fecha,
    'datoHora' : hora,
    'datoAJM' : ajm,
    'datoCUT' : cut,
    'datoHGM' : hgm,
    'datoINN' : inn,
    'datoLAA' : laa,
    'datoMER' : mer,
    'datoMON' : mon,
    'datoMPA' : mpa,
    'datoTLA' : tla,
    'datoXAL' : xal,
    }

    print ("Insertando registro " + str(i) + " de " + str(len(xls)))
    cursor.execute(addPA, datosPA)
    cnx.commit()
    print ("Registro " + str(i) +  " insertado, completado el " + str(int(i)*100/int(len(xls))) +  " porciento del total de datos")

######################################################################################################################
##                                                                                                                  ##
##                                     Cerrando las conexiones a la base de datos...                                ##
##                                                                                                                  ##
######################################################################################################################

print ("Se insertaron adecuadamente el 100 porciento de los datos del xls en la base de datos.")
cursor.close()
cnx.close()



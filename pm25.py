######################################################################################################################
##                                                                                                                  ##
##    Módulo Python 3.6.5 (32 bits) para leer un fichero xls y guardar la información en una base de datos MySQL    ##
##                                     mediante las librerías pandas y mysql                                        ##
##                                                                                                                  ##
##                 Se leen los datos pertenecientes a los valores de contaminación de PM 2.5 (PM25)                 ##
##                     de las estaciones de medición Ciudad de México y el Estado de México                         ##
##                  Actualmente se encuentran registrados los datos desde 01/01/2018 a 28/02/2019                   ##    
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

nombreBDPM25 = 'bancosexternos'  ## Configuración para la base de dato de contaminantes SO2...
config = {
  'user': 'kike',
  'password': 'kike123',
  'host': '127.0.0.1',
  'database': 'bancosexternos',
  'raise_on_warnings': True,
}

tablaPM25 = {} ## Definición de la tabla de contaminantes SO2...
tablaPM25[nombreBDPM25] = ( 
    "CREATE TABLE `pm25` ("
    "   `IDPM25` INT NOT NULL AUTO_INCREMENT,"
    "   `FECHA` TIMESTAMP NULL,"
    "   `HORA` DOUBLE NULL,"
    "   `AJM` DOUBLE NULL,"
    "   `AJU` DOUBLE NULL,"
    "   `BJU` DOUBLE NULL,"
    "   `CAM` DOUBLE NULL,"
    "   `CCA` DOUBLE NULL,"
    "   `COY` DOUBLE NULL,"
    "   `GAM` DOUBLE NULL,"
    "   `HGM` DOUBLE NULL,"
    "   `INN` DOUBLE NULL,"
    "   `MER` DOUBLE NULL,"
    "   `MGH` DOUBLE NULL,"
    "   `MPA` DOUBLE NULL,"
    "   `NEZ` DOUBLE NULL,"
    "   `PED` DOUBLE NULL,"
    "   `SAG` DOUBLE NULL,"
    "   `SFE` DOUBLE NULL,"
    "   `SJA` DOUBLE NULL,"
    "   `TLA` DOUBLE NULL,"
    "   `UAX` DOUBLE NULL,"
    "   `UIZ` DOUBLE NULL,"
    "   `XAL` DOUBLE NULL,"
    "   PRIMARY KEY (`IDPM25`));"
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
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(nombreBDPM25))
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
    cnx.database = nombreBDPM25  
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = nombreBDPM25
    else:
        print ("   ")
        print(err)
        exit(1) 

######################################################################################################################
##                                                                                                                  ##
##                                  Se solicita crear todas las tablas definidas...                                 ##
##                                                                                                                  ##
######################################################################################################################

for name, ddl in tablaPM25.items():
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

direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/PM25.xls"
xls = panda.read_excel(direccionFichero)

print ("    ")
print ("Cargando fichero de contaminantes PM 2.5, puede tardar un momento, por favor espere...")
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

print ("Imprimiendo los primeros 5 registros del registro de contaminante PM 2.5...")
print (xls.head(5))

print ("    ")
print ("Imprimiendo los últimos 5 registros del registro de contaminante PM 2.5...")
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
##         datosEgreso [Contiene la información necesaria para hacer la inserción en la base de datos]...           ##
##                 addEgreso [Consulta SQL que inserta la información en la base de datos]...                       ##
##                                                                                                                  ##
######################################################################################################################

fecha = ""
hora = ""
ajm = ""
aju = ""
bju = ""
cam = ""
cca = ""
coy = ""
gam = ""
hgm = ""
inn = ""
mer = ""
mgh = ""
mpa = ""
nez = ""
ped = ""
sag = ""
sfe = ""
sja = ""
tla = ""
uax = ""
uiz = ""
xal = ""

datosPM25 = {
    'datoFecha' : fecha,
    'datoHora' : hora,
    'datoAJM' : ajm,
    'datoAJU' : aju,
    'datoBJU' : bju,
    'datoCAM' : cam,
    'datoCCA' : cca,
    'datoCOY' : coy,
    'datoGAM' : gam,
    'datoHGM' : hgm,
    'datoINN' : inn,
    'datoMER' : mer,
    'datoMGH' : mgh,
    'datoMPA' : mpa,
    'datoNEZ' : nez,
    'datoPED' : ped,
    'datoSAG' : sag,
    'datoSFE' : sfe,
    'datoTJA' : sja,
    'datoTLA' : tla,
    'datoUAX' : uax,
    'datoUIZ' : uiz,
    'datoXAL' : xal,
}

addPM25 = ("INSERT INTO pm25"
                "(FECHA, HORA, AJM, AJU, BJU, CAM, CCA, COY, GAM, HGM, INN, MER, MGH, MPA, NEZ, PED, SAG, SFE, SJA, TLA, UAX, UIZ, XAL)"
                "VALUES (%(datoFecha)s, %(datoHora)s, %(datoAJM)s, %(datoAJU)s, %(datoBJU)s, %(datoCAM)s, %(datoCCA)s, %(datoCOY)s, %(datoGAM)s, %(datoHGM)s, %(datoINN)s, %(datoMER)s, %(datoMGH)s, %(datoMPA)s, %(datoNEZ)s, %(datoPED)s, %(datoSAG)s, %(datoSFE)s, %(datoSJA)s, %(datoTLA)s, %(datoUAX)s, %(datoUIZ)s, %(datoXAL)s)"
            )

######################################################################################################################
##                                                                                                                  ##
##                             Se leen los valores del xls y se asignan a las variables...                          ##
##                 Esto es necesario para poder insertar correctamente los valores en la base de datos...           ##
##                                                                                                                  ##
######################################################################################################################

for i in range(0, len(xls)):
    fecha = datetime.date(xls.iloc[i,0])
    hora = float(xls.iloc[i,1])
    ajm = float(xls.iloc[i,2])
    aju = float(xls.iloc[i,3])
    bju = float(xls.iloc[i,4])
    cam = float(xls.iloc[i,5])
    cca = float(xls.iloc[i,6])
    coy = float(xls.iloc[i,7])
    gam = float(xls.iloc[i,8])
    hgm = float(xls.iloc[i,9])
    inn = float(xls.iloc[i,10])
    mer = float(xls.iloc[i,11])
    mgh = float(xls.iloc[i,12])
    mpa = float(xls.iloc[i,13])
    nez = float(xls.iloc[i,14])
    ped = float(xls.iloc[i,15])
    sag = float(xls.iloc[i,16])
    sfe = float(xls.iloc[i,17])
    sja = float(xls.iloc[i,18])
    tla = float(xls.iloc[i,19])
    uax = float(xls.iloc[i,20])
    uiz = float(xls.iloc[i,21])
    xal = float(xls.iloc[i,22])

    datosPM25 = {
    'datoFecha' : fecha,
    'datoHora' : hora,
    'datoAJM' : ajm,
    'datoAJU' : aju,
    'datoBJU' : bju,
    'datoCAM' : cam,
    'datoCCA' : cca,
    'datoCOY' : coy,
    'datoGAM' : gam,
    'datoHGM' : hgm,
    'datoINN' : inn,
    'datoMER' : mer,
    'datoMGH' : mgh,
    'datoMPA' : mpa,
    'datoNEZ' : nez,
    'datoPED' : ped,
    'datoSAG' : sag,
    'datoSFE' : sfe,
    'datoSJA' : sja,
    'datoTLA' : tla,
    'datoUAX' : uax,
    'datoUIZ' : uiz,
    'datoXAL' : xal,
    }

    print ("Insertando registro " + str(i) + " de " + str(len(xls)))
    cursor.execute(addPM25, datosPM25)
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

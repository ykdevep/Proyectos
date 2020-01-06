import pandas as panda
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
from geopy import distance

nombreBDAlmacen = 'almacen'  ## Configuración para la base de dato de localización gegráfica...
configAlmacen = {
  'user' : 'kike',
  'password' : 'kike123',
  'host' : '127.0.0.1',
  'database' : 'almacen',
  'raise_on_warnings' : True,
}

configVariables = {
    'user' : 'kike',
    'password' : 'kike123',
    'host' : '127.0.0.1',
    'database' : 'wearables',
    'raise_on_warnings' : True,
}



tablaAlmacen = {} ## Definición de la tabla de localización...
tablaAlmacen[nombreBDAlmacen] = ( 
    "CREATE TABLE `almacenexp1` ("
    "   `IDALDA` INT NOT NULL AUTO_INCREMENT,"
    "   `IDUSUARIO` INT NULL,"
    "   `LATUSR` DOUBLE NULL,"
    "   `LONGUSR` DOUBLE NULL,"
    "   `MARCATIEMPO` DOUBLE NULL,"
    "   `SO2` DOUBLE NULL,"
    "   `NO2` DOUBLE NULL,"
    "   `RH` DOUBLE NULL,"
    "   `CO` DOUBLE NULL,"
    "   `NO` DOUBLE NULL,"
    "   `NOX` DOUBLE NULL,"
    "   `O3` DOUBLE NULL,"
    "   `PM10` DOUBLE NULL,"
    "   `PM25` DOUBLE NULL,"
    "   `PA` DOUBLE NULL,"
    "   `RUVA` DOUBLE NULL,"
    "   `RUVB` DOUBLE NULL,"
    "   `TEMPAMB` DOUBLE NULL,"
    "   `BVP` DOUBLE NULL,"
    "   `EDA` DOUBLE NULL,"
    "   `RC` DOUBLE NULL,"
    "   `TEMPC` DOUBLE NULL,"
    "   PRIMARY KEY (`IDALDA`));"
    "   ENGINE = InnoDB"
)


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



try:
    print ("Creando las variables de conexión...")
    cnx = mysql.connector.connect(**configAlmacen)
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

def create_database(cursor):  ## Función para la base de d...
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(nombreBDAlmacen))
    except mysql.connector.Error as err:
        print ("   ")
        print("Error al crear la base de datos señalada: {}".format(err))
        exit(1)


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

try:
    print ("Creando las variables de conexión...")
    cnx = mysql.connector.connect(**configVariables)
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



cursor.execute(
    "SELECT * FROM e4temp"
)
datosTEMP = cursor.fetchall()

cursor.execute(
    "SELECT * FROM e4hr"
)
datosHR = cursor.fetchall()

cursor.execute(
    "SELECT * FROM e4eda"
)
datosEDA = cursor.fetchall()
cursor.execute(
    "SELECT * FROM e4bvp"
)
datosBVP = cursor.fetchall()

cursor.close()
cnx.close()

valorGenerado = []

for i in datosTEMP:
    fecha = i[1]
    bvp = i[2]
    usuario = i[3]
    print("Fecha: " + str(fecha))
    print("BVP: " + str(bvp))
    print("Usuario: " + str(usuario))
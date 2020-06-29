import pandas as panda
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
import random


nombreBDWearable = 'datawarehouse'  ## Configuración para el almacen
config = {
  'user': 'kike',
  'password': 'kike123',
  'host': '127.0.0.1',
  'database': 'datawarehouse',
  'raise_on_warnings': True,
}

tablaHR = {} ## Definición de la tabla de temperatura ambiental...
tablaHR[nombreBDWearable] = ( 
    "CREATE TABLE `hrtemp` ("
    "   `IDHRTEMP` INT NOT NULL AUTO_INCREMENT,"
    "   `IDMAPS` INT NULL,"
    "   `IDTIEMPO` INT NULL,"
    "   `IDINFOAMBIENTAL` INT NULL,"
    "   `HR` DOUBLE NULL,"
    "   `TEMP` DOUBLE NULL,"
    "   PRIMARY KEY (`IDHRTEMP`));"
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

def create_database(cursor):  ## Función para la creación de la base de datos...
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(nombreBDWearable))
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
    cnx.database = nombreBDWearable  
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = nombreBDWearable
    else:
        print ("   ")
        print(err)
        exit(1) 

######################################################################################################################
##                                                                                                                  ##
##                                  Se solicita crear todas las tablas definidas...                                 ##
##                                                                                                                  ##
######################################################################################################################

for name, ddl in tablaHR.items():
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



cursor.execute("SELECT * FROM e4hrtemp")
e4hrtemp = cursor.fetchall()
cursor.execute("SELECT * FROM tiempo")
tiempo = cursor.fetchall()


idMapsDato = ""
idTiempoDato = 0
idInfoAmbDato = ""
hrDato = ""
tempDato = ""

datosHR = {
    'datoIdMaps' : idMapsDato,
    'datoIdTiempo' : idTiempoDato,
    'datoIdInfo' : idInfoAmbDato,
    'datoHR' : hrDato,
    'datoTemp' : tempDato,
}

addHR = ("INSERT INTO hrtemp"
                "(IDMAPS, IDTIEMPO, IDINFOAMBIENTAL, HR, TEMP)"
                "VALUES (%(datoIdMaps)s, %(datoIdTiempo)s, %(datoIdInfo)s, %(datoHR)s, %(datoTemp)s)"
            )



dia = e4hrtemp[0][1]
mes = e4hrtemp[0][2]
hora = e4hrtemp[0][4]
minuto = e4hrtemp[0][5]

for i in range(0, len(e4hrtemp)):
    idMapsDato = random.randint(95342, 118765)

    if( dia == e4hrtemp[i][1] and mes == e4hrtemp[i][2] and hora == e4hrtemp[i][4] and minuto == e4hrtemp[i][5]):
        idTiempoDato = idTiempoDato
    else:
        valorAgregado = False
        for j in range(60781, len(tiempo)):
            if(dia == tiempo[j][1] and mes == tiempo[j][2] and hora == tiempo[j][4] and minuto == tiempo[j][5] and valorAgregado == False):
                idTiempoDato = tiempo[j][0]
                valorAgregado = True

    idInfoAmbDato = i
    hrDato = e4hrtemp[i][7]
    tempDato = e4hrtemp[i][8]

    datosHR = {
    'datoIdMaps' : idMapsDato,
    'datoIdTiempo' : idTiempoDato,
    'datoIdInfo' : idInfoAmbDato,
    'datoHR' : hrDato,
    'datoTemp' : tempDato,
    }

    print ("Insertando registro " + str(i) + " de " + str(len(e4hrtemp)))
    cursor.execute(addHR, datosHR)
    cnx.commit()
    print ("Registro " + str(i) +  " insertado, completado el " + str(int(i)*100/int(len(e4hrtemp))) +  " porciento del total de datos HR")

print ("Se insertaron adecuadamente el 100 porciento de los datos del xls en la base de datos.")

cursor.close()
cnx.close()





    





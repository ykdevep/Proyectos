import pandas as panda
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

nombreBDSel = 'bancosexternos'  ## Configuración para la base de dato de localización gegráfica...
config = {
  'user': 'kike',
  'password': 'kike123',
  'host': '127.0.0.1',
  'database': 'bancosexternos',
  'raise_on_warnings': True,
}

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


cursor.execute("SELECT * FROM monoxnitrogeno")
monoxnitrogeno = cursor.fetchall()
cursor.execute("SELECT * FROM oxnitrogenos")
oxnitrogenos = cursor.fetchall()

cursor.close()
cnx.close()

nombreBDLoc = 'datawarehouse'  ## Configuración para la base de dato de localización gegráfica...
config = {
  'user': 'kike',
  'password': 'kike123',
  'host': '127.0.0.1',
  'database': 'datawarehouse',
  'raise_on_warnings': True,
}

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


cursor.execute("SELECT * FROM e4hrtemp")
e4HrTemp = cursor.fetchall()

cursor.close()
cnx.close()


dialista = []
meslista = []
annolista = []
horalista = []
minutolista = []
segundolista = []
hrlista = []
templista = []
monoxnitrogenolista = []
oxnitrogenoslista = []

valor = 0

for i in range(0, len(e4HrTemp)):
    print("Haciendo el " + str(i) + " de " + str(len(e4HrTemp)))
    diae4 = e4HrTemp[i][1]
    dialista.append(diae4)
    mese4 = e4HrTemp[i][2]
    meslista.append(mese4)
    annoe4 = e4HrTemp[i][3]
    annolista.append(annoe4)
    minutolista.append(e4HrTemp[i][5])
    segundolista.append(e4HrTemp[i][6])
    hrlista.append(e4HrTemp[i][7])
    templista.append(e4HrTemp[i][8])



    if(e4HrTemp[i][4] == None):
        horae4 = 24
        horalista.append(horae4)
    else:
        horae4 = e4HrTemp[i][4]
        horalista.append(horae4)

    valorNoInsertado = True

    for j in range(0, len(oxnitrogenos)):
        dia = (oxnitrogenos[j][1]).day
        dia = int(dia)
        mes = (oxnitrogenos[j][1]).month
        mes = int(mes)
        anno = (oxnitrogenos[j][1]).year
        anno = int(anno)
        hora = oxnitrogenos[j][2]
        hora = int(hora)

        if((int(diae4) == int(dia)) and (int(mese4) == int(mes)) and (int(annoe4) == int(anno)) and (int(horae4) == int(hora))):
            if(valorNoInsertado):
                oxnitrogenoslista.append(oxnitrogenos[j][31])
                valorNoInsertado = False

    valorNoInsertado = True

    for j in range(0, len(monoxnitrogeno)):
        dia = (monoxnitrogeno[j][1]).day
        dia = int(dia)
        mes = (monoxnitrogeno[j][1]).month
        mes = int(mes)
        anno = (monoxnitrogeno[j][1]).year
        anno = int(anno)
        hora = monoxnitrogeno[j][2]
        hora = int(hora)

        if((int(diae4) == int(dia)) and (int(mese4) == int(mes)) and (int(annoe4) == int(anno)) and (int(horae4) == int(hora))):
            if(valorNoInsertado):
                monoxnitrogenolista.append(monoxnitrogeno[j][31])
                valorNoInsertado = False



datosCSV2 = { 'DIA' : dialista,
              'MES': meslista,
              'ANNO' : annolista,
              'HORA' : horalista,
              'MINUTO' : minutolista,
              'SEGUNDO' : segundolista,
              'HR' : hrlista,
              'TEMP' : templista,
              'MONOXNITROGENO' : monoxnitrogenolista,
              'OXNITROGENOS' : oxnitrogenoslista
}

csv2 = panda.DataFrame(datosCSV2, columns= ['DIA', 'MES', 'ANNO', 'HORA', 'MINUTO', 'SEGUNDO', 'HR', 'TEMP', 'MONOXNITROGENO', 'OXNITROGENOS'])
csv2.to_csv('valoresCSV56.csv')

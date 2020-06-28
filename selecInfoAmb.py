import pandas as panda
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

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


cursor.execute("SELECT DIA, MES, HORA, MINUTO, HR, TEMP FROM e4hrtemp")
e4HrTemp = cursor.fetchall()

cursor.execute("SELECT DIA, MES, HORA, MINUTO, LATITUD, LONGITUD FROM localizacion")
localizacion = cursor.fetchall()

latitudAsignada = []
longitudAsignada = []



for i in range(0, len(e4HrTemp)):
    print("Entrando al primer for con valor de " + str(i))
    menorValor = 9999999999
    latitudTemporal = 0
    longitudTemporal = 0
    valorTemporal = 999999999999
    valoresAsignados = False
    while(valoresAsignados == False):
        for j in range(15700, len(localizacion)):
            print("Entrando al segundo for con valor de " + str(j))
            if(e4HrTemp[i][0] == localizacion[j][0] and e4HrTemp[i][1] == localizacion[j][1] and e4HrTemp[i][2] ==localizacion[j][2]):
                valorTemporal = abs(int(e4HrTemp[i][3]) - int(localizacion[j][4]))
                if(valorTemporal < menorValor):
                    latitudTemporal = localizacion[j][4]
                    longitudAsignada = localizacion[j][5]
                    menorValor = valorTemporal
                    valoresAsignados = True
                    break
            else:
                valoresAsignados = True

        if(latitudTemporal != 0 and longitudTemporal != 0):
            latitudAsignada.append(latitudTemporal)
            print(latitudTemporal)
            longitudAsignada.append(longitudTemporal)
            print(longitudTemporal)
            valoresAsignados = True



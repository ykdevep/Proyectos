import pandas as panda
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

nombreBDAlmacen = 'localizacionesexp'  ## Configuración para la base de dato de localización gegráfica...
configAlmacen = {
  'user' : 'kike',
  'password' : 'kike123',
  'host' : '127.0.0.1',
  'database' : 'localizacionesexp',
  'raise_on_warnings' : True,
}

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

print("Realizando consulta...")
cursor.execute(
    "SELECT * FROM localizaciones LIMIT 100"
)
datosTEMP = cursor.fetchall()

latitud = []
longitud = []
torreSO2 = []
torreNO2 = []
torreRH = []
torreCO = []
torreNO = []
torreNOX = []
torreO3 = []
torrePM10 = []
torrePM25 = []
torrePA = []
torreUVA = []
torreUVB = []
torreTEMP = []
print("Consulta realizada...")

for i in datosTEMP:
    #print(i)
    latitud.append(str(i[1]))
    longitud.append(str(i[2]))
    torreSO2.append(i[3])
    torreNO2.append(i[4])
    torreRH.append(i[5])
    torreCO.append(i[6])
    torreNO.append(i[7])
    torreNOX.append(i[8])
    torreO3.append(i[9])
    torrePM10.append(i[10])
    torrePM25.append(i[11])
    torrePA.append(i[12])
    torreUVA.append(i[13])
    torreUVB.append(i[14])
    torreTEMP.append(i[15])


print(latitud)
print("Agregando los datos al CSV...")
primerCSV = {'latitud' : latitud,
             'longitud' : longitud,
             'SO2' : torreSO2,
             'NO2' : torreNO2,
             'RH' : torreRH,
             'CO' : torreCO,
             'NO' : torreNO,
             'NOX' : torreNOX,
             'O3' : torreO3,
             'PM10' : torrePM10,
             'PM25' : torrePM25,
             'PA' : torrePA,
             'UVA' : torreUVA,
             'UVB' : torreUVB,
             'TEMP' : torreTEMP}

print("Guardando los datos en ubicación física en el PC...")
dataFrame = panda.DataFrame(primerCSV, columns= ['LATITUD', 'LONGITUD', 'SO2', 'NO2', 'RH', 'CO', 'NO', 'NOX', 'O3', 'PM10', 'PM25', 'PA', 'UVA', 'UVB', 'TEMP'])
dataFrame.to_csv('localizacionesCompleto11.csv')
print("Datos guardados en el CSV...")


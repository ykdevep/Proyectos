import pandas as panda
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

###
### Primera parte: Selección de los datos desde la base y creación del CSV original
###
'''
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
    "SELECT * FROM localizaciones"
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
    print(i)
    latitud.append(float(i[1]))
    longitud.append(float(i[2]))
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

print("Agregando los datos al CSV...")
primerCSV = {'LATITUD' : latitud,
             'LONGITUD' : longitud,
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
dataFrame.to_csv('localizacionesCompleto.csv', index=False)
print("Datos guardados en el CSV...")

###
### Fin de la primera parte...
###
'''

###
### Segunda parte: Creación de ficheros CSV a partir del original...
###
print ("Cargando CSV...")
direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/ExperimentoLocalizaciones/localizacionesCompleto.csv"
csv = panda.read_csv(direccionFichero)
print ("CSV cargado...")

latitud = []
longitud = []
claseCompleta = []
tamanno = len(csv)

'''
##
## Creando CSV de 100000 registros
total = int(tamanno)/100
for i in range(0, int(total)):
    print (i)
    latitud.append(csv.iloc[i, 0])
    longitud.append(csv.iloc[i, 1])
    claseCompleta.append(csv.iloc[i, 2] + csv.iloc[i, 3] + csv.iloc[i, 4] + csv.iloc[i, 5] + csv.iloc[i, 6] + csv.iloc[i, 7] + csv.iloc[i, 8] + csv.iloc[i, 9] + csv.iloc[i, 10] + csv.iloc[i, 11] + csv.iloc[i, 12] + csv.iloc[i, 13] + csv.iloc[i, 14])

print("Agregando los datos al CSV...")
segundoCSV = {'LATITUD' : latitud, 'LONGITUD' : longitud, 'CLASE' : claseCompleta}
print("Guardando los datos en ubicación física en el PC...")
dataFrame = panda.DataFrame(segundoCSV, columns= ['LATITUD', 'LONGITUD', 'CLASE'])
dataFrame.to_csv('localizaciones1Clase100000.csv', index=False)
print("Datos guardados en el CSV...")
'''

SO2 = []
NO2 = []
RH = []
CO = []
NO = []
NOX = []
O3 = []
PM10 = []
PM25 = []
PA = []
UVA = []
UVB = []
TEMP = []
total = int(tamanno)/10
for i in range(0, 100000):
    print (i)
    latitud.append(csv.iloc[i, 0])
    longitud.append(csv.iloc[i, 1])
    #claseCompleta.append(csv.iloc[i, 2] + csv.iloc[i, 3] + csv.iloc[i, 4] + csv.iloc[i, 5] + csv.iloc[i, 6] + csv.iloc[i, 7] + csv.iloc[i, 8] + csv.iloc[i, 9] + csv.iloc[i, 10] + csv.iloc[i, 11] + csv.iloc[i, 12] + csv.iloc[i, 13] + csv.iloc[i, 14])
    SO2.append(csv.iloc[i, 2])
    NO2.append(csv.iloc[i, 3])
    RH.append(csv.iloc[i, 4])
    CO.append(csv.iloc[i, 5])
    NO.append(csv.iloc[i, 6])
    NOX.append(csv.iloc[i, 7])
    O3.append(csv.iloc[i, 8])
    PM10.append(csv.iloc[i, 9])
    PM25.append(csv.iloc[i, 10])
    PA.append(csv.iloc[i, 11])
    UVA.append(csv.iloc[i, 12])
    UVB.append(csv.iloc[i, 13])
    TEMP.append(csv.iloc[i, 14])

print("Agregando los datos al CSV...")
segundoCSV = {'LATITUD' : latitud, 'LONGITUD' : longitud, 'SO2' : SO2, 'NO2' : NO2, 'RH' : RH,
              'CO' : CO, 'NO' : NO, 'NOX' : NOX, 'O3' : O3, 'PM10' : PM10, 'PM25' : PM25, 'PA' : PA,
              'UVA' : UVA, 'UVB' : UVB, 'TEMP' : TEMP}
print("Guardando los datos en ubicación física en el PC...")
dataFrame = panda.DataFrame(segundoCSV, columns= ['LATITUD', 'LONGITUD', 'SO2', 'NO2', 'RH', 'CO',
                                                  'NO', 'NOX', 'O3', 'PM10', 'PM25', 'PA', 'UVA',
                                                  'UVB', 'TEMP'])
dataFrame.to_csv('localizacionesCompleto100000.csv', index=False)
print("Datos guardados en el CSV...")


#### 1 millon

latitud = []
longitud = []
claseCompleta = []
SO2 = []
NO2 = []
RH = []
CO = []
NO = []
NOX = []
O3 = []
PM10 = []
PM25 = []
PA = []
UVA = []
UVB = []
TEMP = []

for i in range(0, 1000000):
    print (i)
    latitud.append(csv.iloc[i, 0])
    longitud.append(csv.iloc[i, 1])
    #claseCompleta.append(csv.iloc[i, 2] + csv.iloc[i, 3] + csv.iloc[i, 4] + csv.iloc[i, 5] + csv.iloc[i, 6] + csv.iloc[i, 7] + csv.iloc[i, 8] + csv.iloc[i, 9] + csv.iloc[i, 10] + csv.iloc[i, 11] + csv.iloc[i, 12] + csv.iloc[i, 13] + csv.iloc[i, 14])
    SO2.append(csv.iloc[i, 2])
    NO2.append(csv.iloc[i, 3])
    RH.append(csv.iloc[i, 4])
    CO.append(csv.iloc[i, 5])
    NO.append(csv.iloc[i, 6])
    NOX.append(csv.iloc[i, 7])
    O3.append(csv.iloc[i, 8])
    PM10.append(csv.iloc[i, 9])
    PM25.append(csv.iloc[i, 10])
    PA.append(csv.iloc[i, 11])
    UVA.append(csv.iloc[i, 12])
    UVB.append(csv.iloc[i, 13])
    TEMP.append(csv.iloc[i, 14])

print("Agregando los datos al CSV...")
segundoCSV = {'LATITUD' : latitud, 'LONGITUD' : longitud, 'SO2' : SO2, 'NO2' : NO2, 'RH' : RH,
              'CO' : CO, 'NO' : NO, 'NOX' : NOX, 'O3' : O3, 'PM10' : PM10, 'PM25' : PM25, 'PA' : PA,
              'UVA' : UVA, 'UVB' : UVB, 'TEMP' : TEMP}
print("Guardando los datos en ubicación física en el PC...")
dataFrame = panda.DataFrame(segundoCSV, columns= ['LATITUD', 'LONGITUD', 'SO2', 'NO2', 'RH', 'CO',
                                                  'NO', 'NOX', 'O3', 'PM10', 'PM25', 'PA', 'UVA',
                                                  'UVB', 'TEMP'])
dataFrame.to_csv('localizacionesCompleto1Millon.csv', index=False)
print("Datos guardados en el CSV...")

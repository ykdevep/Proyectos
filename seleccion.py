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


cursor.execute("SELECT * FROM dioxazufre")
dioxazufre = cursor.fetchall()
cursor.execute("SELECT * FROM dioxnitrogeno")
dioxnitrogeno = cursor.fetchall()
cursor.execute("SELECT * FROM humrelativa")
humrelativa = cursor.fetchall()
cursor.execute("SELECT * FROM monoxcarbono")
monoxcarbono = cursor.fetchall()
cursor.execute("SELECT * FROM monoxnitrogeno")
monoxnitrogeno = cursor.fetchall()
cursor.execute("SELECT * FROM oxnitrogenos")
oxnitrogenos = cursor.fetchall()
cursor.execute("SELECT * FROM ozono")
ozono = cursor.fetchall()
cursor.execute("SELECT * FROM pm10")
pm10 = cursor.fetchall()
cursor.execute("SELECT * FROM pm25")
pm25 = cursor.fetchall()
cursor.execute("SELECT * FROM presionatm")
presionatm = cursor.fetchall()
cursor.execute("SELECT * FROM raduva")
raduva = cursor.fetchall()
cursor.execute("SELECT * FROM raduvb")
raduvb = cursor.fetchall()
cursor.execute("SELECT * FROM tempamb")
tempamb = cursor.fetchall()

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
dioxazufrelista = []
dioxnitrogenolista = []
monoxcarbonolista = []
monoxnitrogenolista = []
oxnitrogenolista = []
ozonolista = []
pm10lista = []
pm25lista = []
humrelativalista = []
presionatmlista = []
raduvalista = []
raduvblista = []
tempamblista = []
hrlista = []
templista = []

for i in range(25130, 25133):
    print("Haciendo el " + str(i) + " de " + str(len(e4HrTemp)))
    dialista.append(e4HrTemp[i][1])
    meslista.append(e4HrTemp[i][2])
    annolista.append(e4HrTemp[i][3])
    horalista.append(e4HrTemp[i][4])
    minutolista.append(e4HrTemp[i][5])
    segundolista.append(e4HrTemp[i][6])
    hrlista.append(e4HrTemp[i][7])
    templista.append(e4HrTemp[i][8])

    valore4 = 0
    if(e4HrTemp[i][4] == None):
        valore4 = 24
    else:
        valore4 = int(e4HrTemp[i][4])

    print("El valor de la hora es " + str(valore4))

    for j in range(4631, 4658):
        print("EL valor de e4 es " + str(valore4))
        dia = (dioxazufre[j][1]).day
        dia = int(dia)
        mes = (dioxazufre[j][1]).month
        mes = int(mes)
        anno = (dioxazufre[j][1]).year
        anno = int(anno)
        hora = dioxazufre[j][2]
        hora = int(hora)
        print ("La hora es " + str(hora))
'''
        print ("Dia")
        print (int(e4HrTemp[i][1]))
        print(dia)
        print("Mes")
        print (int(e4HrTemp[i][2]))
        print(mes)
        print("Año")
        print (int(e4HrTemp[i][3]))
        print(anno)
        print("Hora")
        print(valore4)
        print(int(dioxazufre[j][2]))


        if (int(e4HrTemp[i][1]) == dia):
            print("EL DIA ES IGUAL") 
            if(int(e4HrTemp[i][2]) == mes):
                print("EL DIA Y EL MES SON IGUALES")
                if(int(e4HrTemp[i][3]) == anno):
                    print("EL DIA, EL MES Y EL AÑO SON IGUALES")
                    if(valore4 == hora):
                        print("El valor de e4 es: " + str(valore4))
                        print("EL DIA, EL MES, EL AÑO Y LA HORA SON IGUALES")
                        print(dioxazufre[j][32])
                        dioxazufrelista.append(dioxazufre[j][32])

    for j in range(0, len(dioxnitrogeno)):
        if (int(e4HrTemp[i][1]) == (dioxnitrogeno[j][1]).day and int(e4HrTemp[i][2]) == (dioxnitrogeno[j][1]).month and int(e4HrTemp[i][3]) == (dioxnitrogeno[j][1]).year and int(e4HrTemp[i][4]) == dioxnitrogeno[j][2]):
            dioxnitrogenolista.append(dioxnitrogeno[j][31])

    for j in range(0, len(humrelativa)):
        if (int(e4HrTemp[i][1]) == (humrelativa[j][1]).day and int(e4HrTemp[i][2]) == (humrelativa[j][1]).month and int(e4HrTemp[i][3]) == (humrelativa[j][1]).year and int(e4HrTemp[i][4]) == humrelativa[j][2]):
            humrelativalista.append(humrelativa[j][27])

    for j in range(0, len(monoxcarbono)):
        if (int(e4HrTemp[i][1]) == (monoxcarbono[j][1]).day and int(e4HrTemp[i][2]) == (monoxcarbono[j][1]).month and int(e4HrTemp[i][3]) == (monoxcarbono[j][1]).year and int(e4HrTemp[i][4]) == monoxcarbono[j][2]):
            monoxcarbonolista.append(monoxcarbono[j][31])

    for j in range(0, len(monoxnitrogeno)):
        if (int(e4HrTemp[i][1]) == (monoxnitrogeno[j][1]).day and int(e4HrTemp[i][2]) == (monoxnitrogeno[j][1]).month and int(e4HrTemp[i][3]) == (monoxnitrogeno[j][1]).year and int(e4HrTemp[i][4]) == monoxnitrogeno[j][2]):
            monoxnitrogenolista.append(monoxnitrogeno[j][31])

    for j in range(0, len(oxnitrogenos)):
        if (int(e4HrTemp[i][1]) == (oxnitrogenos[j][1]).day and int(e4HrTemp[i][2]) == (oxnitrogenos[j][1]).month and int(e4HrTemp[i][3]) == (oxnitrogenos[j][1]).year and int(e4HrTemp[i][4]) == oxnitrogenos[j][2]):
            oxnitrogenolista.append(oxnitrogenos[j][31])

    for j in range(0, len(ozono)):
        if (int(e4HrTemp[i][1]) == (ozono[j][1]).day and int(e4HrTemp[i][2]) == (ozono[j][1]).month and int(e4HrTemp[i][3]) == (ozono[j][1]).year and int(e4HrTemp[i][4]) == ozono[j][2]):
            ozonolista.append(ozono[j][31])

    for j in range(0, len(pm10)):
        if (int(e4HrTemp[i][1]) == (pm10[j][1]).day and int(e4HrTemp[i][2]) == (pm10[j][1]).month and int(e4HrTemp[i][3]) == (pm10[j][1]).year and int(e4HrTemp[i][4]) == pm10[j][2]):
            pm10lista.append(pm10[j][26])

    for j in range(0, len(pm25)):
        if (int(e4HrTemp[i][1]) == (pm25[j][1]).day and int(e4HrTemp[i][2]) == (pm25[j][1]).month and int(e4HrTemp[i][3]) == (pm25[j][1]).year and int(e4HrTemp[i][4]) == pm25[j][2]):
            pm25lista.append(pm25[j][16])

    for j in range(0, len(presionatm)):
        if (int(e4HrTemp[i][1]) == (presionatm[j][1]).day and int(e4HrTemp[i][2]) == (presionatm[j][1]).month and int(e4HrTemp[i][3]) == (presionatm[j][1]).year and int(e4HrTemp[i][4]) == presionatm[j][2]):
            presionatmlista.append(presionatm[j][7])

    for j in range(0, len(raduva)):
        if (int(e4HrTemp[i][1]) == (raduva[j][1]).day and int(e4HrTemp[i][2]) == (raduva[j][1]).month and int(e4HrTemp[i][3]) == (raduva[j][1]).year and int(e4HrTemp[i][4]) == raduva[j][2]):
            raduvalista.append(raduva[j][6])

    for j in range(0, len(raduvb)):
        if (int(e4HrTemp[i][1]) == (raduvb[j][1]).day and int(e4HrTemp[i][2]) == (raduvb[j][1]).month and int(e4HrTemp[i][3]) == (raduvb[j][1]).year and int(e4HrTemp[i][4]) == raduvb[j][2]):
            raduvblista.append(raduvb[j][6])

    for j in range(0, len(tempamb)):
        if (int(e4HrTemp[i][1]) == (tempamb[j][1]).day and int(e4HrTemp[i][2]) == (tempamb[j][1]).month and int(e4HrTemp[i][3]) == (tempamb[j][1]).year and int(e4HrTemp[i][4]) == tempamb[j][2]):
            tempamblista.append(tempamb[j][6])


datosCSV1 = { 'DIA' : dialista,
              'MES': meslista,
              'ANNO' : annolista,
              'HORA' : horalista,
              'DIOXAZUFRE' : dioxazufrelista,
              'DIOXNITROGENO' : dioxnitrogenolista,
              'MONOXCARBONO' : monoxcarbonolista,
              'MONOXNITROGENOS' : monoxnitrogenolista,
              'OXNITROGENO' : oxnitrogenolista,
              'OZONO' : ozonolista,
              'PM10' : pm10lista, 
              'PM25' : pm25lista,
              'HUMRELATIVA': humrelativalista,
              'PRESIONATM': presionatmlista,
              'RADUVA': raduvalista,
              'RADUVB' : raduvblista,
              'TEMPAMB': tempamblista
}

csv1 = panda.DataFrame(datosCSV1, columns= ['DIA', 'MES', 'ANNO', 'HORA', 'DIOXAZUFRE', 'DIOXNITROGENO', 'MONOXCARBONO', 'MONOXNITROGENOS', 'OXNITROGENO', 'OZONO', 'PM10', 'PM25', 'HUMRELATIVA', 'PRESIONATM', 'RADUVA', 'RADUVB', 'TEMPAMB'])
csv1.to_csv('infoAmbiental.csv')
'''
datosCSV2 = { 'DIA' : dialista,
              'MES': meslista,
              'ANNO' : annolista,
              'HORA' : horalista,
              'MINUTO' : minutolista,
              'SEGUNDO' : segundolista,
              'HR' : hrlista,
              'TEMP' : templista,
              'DIOXAZUFRE' : dioxazufrelista
}

print(len(templista))
print(len(dioxazufrelista))
'''
csv2 = panda.DataFrame(datosCSV2, columns= ['DIA', 'MES', 'ANN0', 'HORA', 'MINUTO', 'SEGUNDO', 'HR', 'TEMP', 'DIOXAZUFRE'])
csv2.to_csv('valoresDioxAzufre.csv')

datosCSV3 = { 'DIA' : dialista,
              'MES': meslista,
              'ANNO' : annolista,
              'HORA' : horalista,
              'MINUTO' : minutolista,
              'SEGUNDO' : segundolista,
              'HR' : hrlista,
              'TEMP' : templista,
              'DIOXAZUFRE' : dioxazufrelista,
              'DIOXNITROGENO' : dioxnitrogenolista
}

csv3 = panda.DataFrame(datosCSV3, columns= ['DIA', 'MES', 'ANN0', 'HORA', 'MINUTO', 'SEGUNDO', 'HR', 'TEMP', 'DIOXAZUFRE', 'DIOXNITROGENO'])
csv3.to_csv('valoresDioxAzDioxNi.csv')

datosCSV4 = { 'DIA' : dialista,
              'MES': meslista,
              'ANNO' : annolista,
              'HORA' : horalista,
              'MINUTO' : minutolista,
              'SEGUNDO' : segundolista,
              'HR' : hrlista,
              'TEMP' : templista,
              'DIOXAZUFRE' : dioxazufrelista,
              'DIOXNITROGENO' : dioxnitrogenolista,
              'MONOXCARBONO' : monoxcarbonolista
}

csv4 = panda.DataFrame(datosCSV4, columns= ['DIA', 'MES', 'ANN0', 'HORA', 'MINUTO', 'SEGUNDO', 'HR', 'TEMP', 'DIOXAZUFRE', 'DIOXNITROGENO', 'MONOXCARBONO'])
csv4.to_csv('valoresDioxAzufreDioxNiMonCa.csv')
'''


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
hrlista = []
templista = []
dioxazufrelista = []
dioxnitrogenolista = []
humrelativalista = []
monoxcarbonolista = []
monoxnitrogenolista = []
oxnitrogenoslista = []
ozonolista = []
pm10lista = []
pm25lista = []
presionatmlista = []
raduvalista = []
raduvblista = []
tempamblista = []

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

    for j in range(0, len(dioxazufre)):
        dia = (dioxazufre[j][1]).day
        dia = int(dia)
        mes = (dioxazufre[j][1]).month
        mes = int(mes)
        anno = (dioxazufre[j][1]).year
        anno = int(anno)
        hora = dioxazufre[j][2]
        hora = int(hora)

        if((int(diae4) == int(dia)) and (int(mese4) == int(mes)) and (int(annoe4) == int(anno)) and (int(horae4) == int(hora))):
            if(valorNoInsertado):
                dioxazufrelista.append(dioxazufre[j][32])
                valorNoInsertado = False

    valorNoInsertado = True

    for j in range(0, len(dioxnitrogeno)):
        dia = (dioxnitrogeno[j][1]).day
        dia = int(dia)
        mes = (dioxnitrogeno[j][1]).month
        mes = int(mes)
        anno = (dioxnitrogeno[j][1]).year
        anno = int(anno)
        hora = dioxnitrogeno[j][2]
        hora = int(hora)

        if((int(diae4) == int(dia)) and (int(mese4) == int(mes)) and (int(annoe4) == int(anno)) and (int(horae4) == int(hora))):
            if(valorNoInsertado):
                dioxnitrogenolista.append(dioxnitrogeno[j][31])
                valorNoInsertado = False

    valorNoInsertado = True

    for j in range(0, len(humrelativa)):
        dia = (humrelativa[j][1]).day
        dia = int(dia)
        mes = (humrelativa[j][1]).month
        mes = int(mes)
        anno = (humrelativa[j][1]).year
        anno = int(anno)
        hora = humrelativa[j][2]
        hora = int(hora)

        if((int(diae4) == int(dia)) and (int(mese4) == int(mes)) and (int(annoe4) == int(anno)) and (int(horae4) == int(hora))):
            if(valorNoInsertado):
                humrelativalista.append(humrelativa[j][27])
                valorNoInsertado = False

    valorNoInsertado = True

    for j in range(0, len(monoxcarbono)):
        dia = (monoxcarbono[j][1]).day
        dia = int(dia)
        mes = (monoxcarbono[j][1]).month
        mes = int(mes)
        anno = (monoxcarbono[j][1]).year
        anno = int(anno)
        hora = monoxcarbono[j][2]
        hora = int(hora)

        if((int(diae4) == int(dia)) and (int(mese4) == int(mes)) and (int(annoe4) == int(anno)) and (int(horae4) == int(hora))):
            if(valorNoInsertado):
                monoxcarbonolista.append(monoxcarbono[j][31])
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

    valorNoInsertado = True

    for j in range(0, len(ozono)):
        dia = (ozono[j][1]).day
        dia = int(dia)
        mes = (ozono[j][1]).month
        mes = int(mes)
        anno = (ozono[j][1]).year
        anno = int(anno)
        hora = ozono[j][2]
        hora = int(hora)

        if((int(diae4) == int(dia)) and (int(mese4) == int(mes)) and (int(annoe4) == int(anno)) and (int(horae4) == int(hora))):
            if(valorNoInsertado):
                ozonolista.append(ozono[j][31])
                valorNoInsertado = False

    valorNoInsertado = True

    for j in range(0, len(pm10)):
        dia = (pm10[j][1]).day
        dia = int(dia)
        mes = (pm10[j][1]).month
        mes = int(mes)
        anno = (pm10[j][1]).year
        anno = int(anno)
        hora = pm10[j][2]
        hora = int(hora)

        if((int(diae4) == int(dia)) and (int(mese4) == int(mes)) and (int(annoe4) == int(anno)) and (int(horae4) == int(hora))):
            if(valorNoInsertado):
                pm10lista.append(pm10[j][26])
                valorNoInsertado = False

    valorNoInsertado = True

    for j in range(0, len(pm25)):
        dia = (pm25[j][1]).day
        dia = int(dia)
        mes = (pm25[j][1]).month
        mes = int(mes)
        anno = (pm25[j][1]).year
        anno = int(anno)
        hora = pm25[j][2]
        hora = int(hora)

        if((int(diae4) == int(dia)) and (int(mese4) == int(mes)) and (int(annoe4) == int(anno)) and (int(horae4) == int(hora))):
            if(valorNoInsertado):
                pm25lista.append(pm25[j][16])
                valorNoInsertado = False

    valorNoInsertado = True

    for j in range(0, len(presionatm)):
        dia = (presionatm[j][1]).day
        dia = int(dia)
        mes = (presionatm[j][1]).month
        mes = int(mes)
        anno = (presionatm[j][1]).year
        anno = int(anno)
        hora = presionatm[j][2]
        hora = int(hora)

        if((int(diae4) == int(dia)) and (int(mese4) == int(mes)) and (int(annoe4) == int(anno)) and (int(horae4) == int(hora))):
            if(valorNoInsertado):
                presionatmlista.append(presionatm[j][7])
                valorNoInsertado = False

    valorNoInsertado = True

    for j in range(0, len(raduva)):
        dia = (raduva[j][1]).day
        dia = int(dia)
        mes = (raduva[j][1]).month
        mes = int(mes)
        anno = (raduva[j][1]).year
        anno = int(anno)
        hora = raduva[j][2]
        hora = int(hora)

        if((int(diae4) == int(dia)) and (int(mese4) == int(mes)) and (int(annoe4) == int(anno)) and (int(horae4) == int(hora))):
            if(valorNoInsertado):
                raduvalista.append(raduva[j][6])
                valorNoInsertado = False

    valorNoInsertado = True

    for j in range(0, len(raduvb)):
        dia = (raduvb[j][1]).day
        dia = int(dia)
        mes = (raduvb[j][1]).month
        mes = int(mes)
        anno = (raduvb[j][1]).year
        anno = int(anno)
        hora = raduvb[j][2]
        hora = int(hora)

        if((int(diae4) == int(dia)) and (int(mese4) == int(mes)) and (int(annoe4) == int(anno)) and (int(horae4) == int(hora))):
            if(valorNoInsertado):
                raduvblista.append(raduvb[j][6])
                valorNoInsertado = False

    valorNoInsertado = True

    for j in range(0, len(tempamb)):
        dia = (tempamb[j][1]).day
        dia = int(dia)
        mes = (tempamb[j][1]).month
        mes = int(mes)
        anno = (tempamb[j][1]).year
        anno = int(anno)
        hora = tempamb[j][2]
        hora = int(hora)

        if((int(diae4) == int(dia)) and (int(mese4) == int(mes)) and (int(annoe4) == int(anno)) and (int(horae4) == int(hora))):
            if(valorNoInsertado):
                tempamblista.append(tempamb[j][27])
                valorNoInsertado = False



datosCSV2 = { 'DIA' : dialista,
              'MES': meslista,
              'ANNO' : annolista,
              'HORA' : horalista,
              'MINUTO' : minutolista,
              'SEGUNDO' : segundolista,
              'HR' : hrlista,
              'TEMP' : templista,
              'DIOXAZUFRE' : dioxazufrelista,
              'DIOXNITROGENO': dioxnitrogenolista,
              'HUMRELATIVA': humrelativalista,
              'MONOXCARBONO' : monoxcarbonolista,
              'MONOXNITROGENO' : monoxnitrogenolista,
              'OXNITROGENOS' : oxnitrogenoslista,
              'OZONO' : ozonolista,
              'PM10': pm10lista,
              'PM25' : pm25lista,
              'PRESIONATM' : presionatmlista,
              'RADUVA' : raduvalista,
              'RADUVB' : raduvblista,
              'TEMPAMB': tempamblista
}

csv2 = panda.DataFrame(datosCSV2, columns= ['DIA', 'MES', 'ANNO', 'HORA', 'MINUTO', 'SEGUNDO', 'HR', 'TEMP', 'DIOXAZUFRE', 'DIOXNITROGENO', 
                                            'HUMRELATIVA', 'MONOXCARBONO', 'MONOXNITROGENO', 'OXNITROGENOS', 'OZONO', 'PM10', 'PM25',
                                            'PRESIONATM', 'RADUVA', 'RADUVB', 'TEMPAMB'])
csv2.to_csv('valoresCSVCompleto.csv')

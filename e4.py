######################################################################################################################
##                                                                                                                  ##
##        Módulo Python 3.6.5 para leer un fichero csv y guardar la información  en una base de datos MySQL         ##
##                                     mediante las librerías pandas y mysql                                        ##
##                                                                                                                  ##
##                     Se leen los csv pertenecientes al Wearable Empatica obteniendo registros de:                 ##    
##                                                 1) IBI                                                           ##
##                                                 2) HRV                                                           ##
##                                                 3) EDA                                                           ##
##                                                 4) ACC                                                           ##
##                                                 5) BVP                                                           ##
##                                                                                                                  ## 
##                Se muestran los primeros y últimos 5 registros para ver si la información es correcta             ##
##                           Se determina el número total de campos vacíos en los datos                             ##
##                                                 Versión 1.8.1                                                    ##
##                                          Fecha creación: 1/02/2018                                               ##
##                                        Última modificación: 19/02/2019                                           ##
##                                         Enrique Alfonso Carmona García                                           ##
##                                          eacarmona860920@gmail.com                                               ##
##                         La información relativa a la librería pandas puede ser consultada en:                    ##
##                                    http://pandas.pydata.org/pandas-docs/stable/index.html                        ##
##             La información relativa a la librería numpy (necesaria para pandas) puede ser consultada en:         ##
##                                          https://docs.scipy.org/doc/                                             ##
##                           La información relativa a mysql.conector puede ser consultada en:                      ##
##                                   https://dev.mysql.com/doc/connector-python/en/                                 ##
##                                                                                                                  ##
##                                 Se requiere:  "pip install mysql-connector-python"                               ##
##                                               "pip install geopy"                                                ##
##                                               "pip install numpy"                                                ##
##                                               "pip install pandas"                                               ##
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

nombreBDWearable = 'wearables'  ## Configuración para la base de dato de temperatura ambiental TMP...
config = {
  'user': 'kike',
  'password': 'kike123',
  'host': '127.0.0.1',
  'database': 'wearables',
  'raise_on_warnings': True,
}

tablaBVP = {} ## Definición de la tabla de temperatura ambiental...
tablaBVP[nombreBDWearable] = ( 
    "CREATE TABLE `e4bvp` ("
    "   `IDBVP` INT NOT NULL AUTO_INCREMENT,"
    "   `FECHATIME` DOUBLE NULL,"
    "   `BVP` DOUBLE NULL,"
    "   `IDUSUARIO` DOUBLE NULL,"
    "   PRIMARY KEY (`IDBVP`));"
    "   ENGINE = InnoDB"
)

tablaEDA = {} ## Definición de la tabla de temperatura ambiental...
tablaEDA[nombreBDWearable] = ( 
    "CREATE TABLE `e4eda` ("
    "   `IDEDA` INT NOT NULL AUTO_INCREMENT,"
    "   `FECHATIME` DOUBLE NULL,"
    "   `EDA` DOUBLE NULL,"
    "   `IDUSUARIO` DOUBLE NULL,"
    "   PRIMARY KEY (`IDEDA`));"
    "   ENGINE = InnoDB"
)

tablaHR = {} ## Definición de la tabla de temperatura ambiental...
tablaHR[nombreBDWearable] = ( 
    "CREATE TABLE `e4hr` ("
    "   `IDHR` INT NOT NULL AUTO_INCREMENT,"
    "   `FECHATIME` DOUBLE NULL,"
    "   `HR` DOUBLE NULL,"
    "   `IDUSUARIO` DOUBLE NULL,"
    "   PRIMARY KEY (`IDHR`));"
    "   ENGINE = InnoDB"
)

tablaTEMP = {} ## Definición de la tabla de temperatura ambiental...
tablaTEMP[nombreBDWearable] = ( 
    "CREATE TABLE `e4temp` ("
    "   `IDTEMP` INT NOT NULL AUTO_INCREMENT,"
    "   `FECHATIME` DOUBLE NULL,"
    "   `TEMP` DOUBLE NULL,"
    "   `IDUSUARIO` DOUBLE NULL,"
    "   PRIMARY KEY (`IDTEMP`));"
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

for name, ddl in tablaBVP.items():
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

for name, ddl in tablaEDA.items():
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

for name, ddl in tablaTEMP.items():
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

direccionFicheroUsuario = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/IDUSER.xlsx"
xls = panda.read_excel(direccionFicheroUsuario)

direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/E4/BVP.csv"
bvp = panda.read_csv(direccionFichero)

print ("    ")
print ("Cargando fichero de BVP, puede tardar un momento, por favor espere...")
if bvp.empty: #Validando si los datos fueron cargados...
    print ("    ")
    print ("Fichero se encuentra vacío, por favor verifique que sea el correcto...")
else:
    print ("    ")
    print ("Fichero cargado exitosamente...")

direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/E4/EDA.csv"
eda = panda.read_csv(direccionFichero)

print ("    ")
print ("Cargando fichero de EDA, puede tardar un momento, por favor espere...")
if eda.empty: #Validando si los datos fueron cargados...
    print ("    ")
    print ("Fichero se encuentra vacío, por favor verifique que sea el correcto...")
else:
    print ("    ")
    print ("Fichero cargado exitosamente...")

direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/E4/HR.csv"
hr = panda.read_csv(direccionFichero)

print ("    ")
print ("Cargando fichero de HR, puede tardar un momento, por favor espere...")
if hr.empty: #Validando si los datos fueron cargados...
    print ("    ")
    print ("Fichero se encuentra vacío, por favor verifique que sea el correcto...")
else:
    print ("    ")
    print ("Fichero cargado exitosamente...")

direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/E4/TEMP.csv"
temp = panda.read_csv(direccionFichero)

print ("    ")
print ("Cargando fichero de temperatura, puede tardar un momento, por favor espere...")
if temp.empty: #Validando si los datos fueron cargados...
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

print ("Imprimiendo los primeros 5 registros del registro de temperatura...")
print (bvp.head(5))

print ("    ")
print ("Imprimiendo los últimos 5 registros del registro de temperatura...")
print (bvp.tail(5))

print ("Imprimiendo los primeros 5 registros del registro de temperatura...")
print (eda.head(5))

print ("    ")
print ("Imprimiendo los últimos 5 registros del registro de temperatura...")
print (eda.tail(5))

print ("Imprimiendo los primeros 5 registros del registro de temperatura...")
print (hr.head(5))

print ("    ")
print ("Imprimiendo los últimos 5 registros del registro de temperatura...")
print (hr.tail(5))

print ("Imprimiendo los primeros 5 registros del registro de temperatura...")
print (temp.head(5))

print ("    ")
print ("Imprimiendo los últimos 5 registros del registro de temperatura...")
print (temp.tail(5))

######################################################################################################################
##                                                                                                                  ##
##                          Determinando cantidad de campos vacíos en los datos...                                  ##
##                                                                                                                  ##
######################################################################################################################

print ("    ")
print ("En los datos existen la siguientes cantidad de datos vacíos:")
info = bvp.apply(lambda x: sum(x.isnull()),axis=0)
print (info)

print ("    ")
print ("En los datos existen la siguientes cantidad de datos vacíos:")
info = eda.apply(lambda x: sum(x.isnull()),axis=0)
print (info)

print ("    ")
print ("En los datos existen la siguientes cantidad de datos vacíos:")
info = hr.apply(lambda x: sum(x.isnull()),axis=0)
print (info)

print ("    ")
print ("En los datos existen la siguientes cantidad de datos vacíos:")
info = temp.apply(lambda x: sum(x.isnull()),axis=0)
print (info)

######################################################################################################################
##                                                                                                                  ##
##                              Rellenando todos los valores vacios con el campo NULL...                            ##
##                 Esto es necesario para poder insertar correctamente los valores en la base de datos...           ##
##                                                                                                                  ##
######################################################################################################################

print ("    ")
print ("Rellenando los campos vacíos con el valor NULL ...")
bvp = bvp.fillna("NULL")

print ("    ")
print ("Rellenando los campos vacíos con el valor NULL ...")
eda = eda.fillna("NULL")

print ("    ")
print ("Rellenando los campos vacíos con el valor NULL ...")
hr = hr.fillna("NULL")

print ("    ")
print ("Rellenando los campos vacíos con el valor NULL ...")
temp = temp.fillna("NULL")

######################################################################################################################
##                                                                                                                  ##
##      Las variables corresponden a sus respectivos campos en la base de datos (Ver descripción anterior)...       ##
##         datosEgreso [Contiene la información necesaria para hacer la inserción en la base de datos]...           ##
##                 addEgreso [Consulta SQL que inserta la información en la base de datos]...                       ##
##                                                                                                                  ##
######################################################################################################################

fechaTimeBVP = ""
bvpDatos = ""
idUsuario = ""

datosBVP = {
    'datoFechaTimeBVP' : fechaTimeBVP,
    'datoBVPDato' : bvpDatos,
    'datoIdUsuario' : idUsuario,
}

addBVP = ("INSERT INTO e4bvp"
                "(FECHATIME, BVP, IDUSUARIO)"
                "VALUES (%(datoFechaTimeBVP)s, %(datoBVPDato)s, %(datoIdUsuario)s)"
            )

fechaTimeEDA = ""
edaDatos = ""
idUsuario = ""

datosEDA = {
    'datoFechaTimeEDA' : fechaTimeEDA,
    'datoEDADato' : edaDatos,
    'datoIdUsuario' : idUsuario,
}

addEDA = ("INSERT INTO e4eda"
                "(FECHATIME, EDA, IDUSUARIO)"
                "VALUES (%(datoFechaTimeEDA)s, %(datoEDADato)s, %(datoIdUsuario)s)"
            )

fechaTimeHR = ""
hrDatos = ""
idUsuario =""

datosHR = {
    'datoFechaTimeHR' : fechaTimeHR,
    'datoHRDato' : hrDatos,
    'datoIdUsuario' : idUsuario,
}

addHR = ("INSERT INTO e4hr"
                "(FECHATIME, HR, IDUSUARIO)"
                "VALUES (%(datoFechaTimeHR)s, %(datoHRDato)s, %(datoIdUsuario)s)"
            )

fechaTimeTEMP = ""
tempDatos = ""
idUsuario = ""

datosTEMP = {
    'datoFechaTimeTEMP' : fechaTimeTEMP,
    'datoTEMPDato' : tempDatos,
    'datoIdUsuario' : idUsuario,
}

addTEMP = ("INSERT INTO e4temp"
                "(FECHATIME, TEMP, IDUSUARIO)"
                "VALUES (%(datoFechaTimeTEMP)s, %(datoTEMPDato)s, %(datoIdUsuario)s)"
            )

######################################################################################################################
##                                                                                                                  ##
##                             Se leen los valores del xls y se asignan a las variables...                          ##
##                 Esto es necesario para poder insertar correctamente los valores en la base de datos...           ##
##                                                                                                                  ##
######################################################################################################################

for i in range(0, len(xls)):
    idUsuario = float(xls.iloc[i,0])

fechaTimeBVP = bvp.iloc[0,0]
fechaTimeBVP = fechaTimeBVP * 1000
for i in range(24, len(bvp)):
    fechaTimeBVP = fechaTimeBVP + 15
    bvpDatos = bvp.iloc[i,0]
 
    datosBVP = {
    'datoFechaTimeBVP' : fechaTimeBVP,
    'datoBVPDato' : bvpDatos,
    'datoIdUsuario' : idUsuario,
    }

    print ("Insertando registro " + str(i) + " de " + str(len(bvp)))
    cursor.execute(addBVP, datosBVP)
    cnx.commit()
    print ("Registro " + str(i) +  " insertado, completado el " + str(int(i)*100/int(len(bvp))) +  " porciento del total de datos")

print ("Se insertaron adecuadamente el 100 porciento de los datos del xls en la base de datos.")

for i in range(0, len(xls)):
    idUsuario = float(xls.iloc[i,0])

fechaTimeEDA = eda.iloc[0,0]
fechaTimeEDA = fechaTimeEDA * 1000
for i in range(5, len(eda)):
    fechaTimeEDA = fechaTimeEDA + 250
    edaDatos = eda.iloc[i,0]
 
    datosEDA = {
    'datoFechaTimeEDA' : fechaTimeEDA,
    'datoEDADato' : edaDatos,
    'datoIdUsuario' : idUsuario,
    }

    print ("Insertando registro " + str(i) + " de " + str(len(eda)))
    cursor.execute(addEDA, datosEDA)
    cnx.commit()
    print ("Registro " + str(i) +  " insertado, completado el " + str(int(i)*100/int(len(eda))) +  " porciento del total de datos")

print ("Se insertaron adecuadamente el 100 porciento de los datos del xls en la base de datos.")

for i in range(0, len(xls)):
    idUsuario = float(xls.iloc[i,0])

fechaTimeHR = hr.iloc[0,0]
fechaTimeHR = fechaTimeHR * 1000
for i in range(4, len(hr)):
    fechaTimeHR = fechaTimeHR + 1000
    hrDatos = hr.iloc[i,0]
 
    datosHR = {
    'datoFechaTimeHR' : fechaTimeHR,
    'datoHRDato' : hrDatos,
    'datoIdUsuario' : idUsuario,
    }

    print ("Insertando registro " + str(i) + " de " + str(len(hr)))
    cursor.execute(addHR, datosHR)
    cnx.commit()
    print ("Registro " + str(i) +  " insertado, completado el " + str(int(i)*100/int(len(hr))) +  " porciento del total de datos")

print ("Se insertaron adecuadamente el 100 porciento de los datos del xls en la base de datos.")

for i in range(0, len(xls)):
    idUsuario = float(xls.iloc[i,0])

fechaTimeTEMP = temp.iloc[0,0]
fechaTimeTEMP = fechaTimeTEMP * 1000
for i in range(4, len(temp)):
    fechaTimeTEMP = fechaTimeTEMP + 250
    tempDatos = temp.iloc[i,0]
 
    datosTEMP = {
    'datoFechaTimeTEMP' : fechaTimeTEMP,
    'datoTEMPDato' : tempDatos,
    'datoIdUsuario' : idUsuario,
    }

    print ("Insertando registro " + str(i) + " de " + str(len(temp)))
    cursor.execute(addTEMP, datosTEMP)
    cnx.commit()
    print ("Registro " + str(i) +  " insertado, completado el " + str(int(i)*100/int(len(temp))) +  " porciento del total de datos")

print ("Se insertaron adecuadamente el 100 porciento de los datos del xls en la base de datos.")

cursor.close()
cnx.close()

import pandas as panda
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime


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
    "CREATE TABLE `e4hrtemp` ("
    "   `IDHR` INT NOT NULL AUTO_INCREMENT,"
    "   `DIA` DOUBLE NULL,"
    "   `MES` DOUBLE NULL,"
    "   `ANNO` DOUBLE NULL,"
    "   `HORA` DOUBLE NULL,"
    "   `MINUTO` DOUBLE NULL,"
    "   `SEGUNDO` DOUBLE NULL,"
    "   `HR` DOUBLE NULL,"
    "   `TEMP` DOUBLE NULL,"
    "   PRIMARY KEY (`IDHR`));"
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


######################################################################################################################
##                                                                                                                  ##
##                                       Cargando el fichero con la información...                                  ##
##                                                                                                                  ##
######################################################################################################################

direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/E4/2018/HR.csv"
hr = panda.read_csv(direccionFichero)

print ("    ")
print ("Cargando fichero de HR, puede tardar un momento, por favor espere...")
if hr.empty: #Validando si los datos fueron cargados...
    print ("    ")
    print ("Fichero se encuentra vacío, por favor verifique que sea el correcto...")
else:
    print ("    ")
    print ("Fichero cargado exitosamente...")

direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/E4/2018/TEMP.csv"
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
##                              Rellenando todos los valores vacios con el campo NULL...                            ##
##                 Esto es necesario para poder insertar correctamente los valores en la base de datos...           ##
##                                                                                                                  ##
######################################################################################################################

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

diaDato = ""
mesDato = ""
annoDato = ""
horaDato = ""
minutoDato = ""
segundoDato = ""
hrDato = ""
tempDato = ""

datosHR = {
    'datoDia' : diaDato,
    'datoMes' : mesDato,
    'datoAnno' : annoDato,
    'datoHora' : horaDato,
    'datoMinuto' : minutoDato,
    'datoSegundo' : segundoDato,
    'datoHR' : hrDato,
    'datoTemp' : tempDato,
}

addHR = ("INSERT INTO e4hrtemp"
                "(DIA, MES, ANNO, HORA, MINUTO, SEGUNDO, HR, TEMP)"
                "VALUES (%(datoDia)s, %(datoMes)s, %(datoAnno)s, %(datoHora)s, %(datoMinuto)s, %(datoSegundo)s, %(datoHR)s, %(datoTemp)s)"
            )

datosTempSeg = []
for i in range(4, len(temp)):

    datosTempSeg.append(temp.iloc[i,0])
    i = i + 4

fechaTimeHR = int(hr.iloc[0,0])

for i in range(4, len(hr)):
    fechaTimeHR = fechaTimeHR + 1
    fechaPandas = datetime.fromtimestamp(fechaTimeHR)
    diaDato = fechaPandas.day
    mesDato = fechaPandas.month
    annoDato = fechaPandas.year
    horaDato = fechaPandas.hour
    minutoDato = fechaPandas.minute
    segundoDato = fechaPandas.second
    hrDato = hr.iloc[i,0]
    tempDato = datosTempSeg[i - 4]
 
    datosHR = {
    'datoDia' : diaDato,
    'datoMes' : mesDato,
    'datoAnno' : annoDato,
    'datoHora' : horaDato,
    'datoMinuto' : minutoDato,
    'datoSegundo' : segundoDato,
    'datoHR' : hrDato,
    'datoTemp' : tempDato,
    }

    print ("Insertando registro " + str(i) + " de " + str(len(hr)))
    cursor.execute(addHR, datosHR)
    cnx.commit()
    print ("Registro " + str(i) +  " insertado, completado el " + str(int(i)*100/int(len(hr))) +  " porciento del total de datos HR")

print ("Se insertaron adecuadamente el 100 porciento de los datos del xls en la base de datos.")

cursor.close()
cnx.close()



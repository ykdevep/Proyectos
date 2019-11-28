######################################################################################################################
##                                                                                                                  ##
## -> Módulo Python para generar aleatoriamente un millón (1000000) de coordenadas geográficas aleatorias de        ##
##           acuerdo a las coordenadas de las estaciones de monitoreo de calidad del aire de la CDMX y área         ##
##           metropolitana cercana. Con la finalidad de crear un banco de datos de coordenadas geográficas que      ##
##           pueda ser empleado para entrenar un algoritmo de clasificación que determine la estación de monitoreo  ##
##           más cercana a las coordenadas seleccionadas...                                                         ##
##             -> Fue probado para versiones de Python  de 3.6.5 a 3.7.4 (32 bits y 64 bits)...                     ##    
##             -> Se usa de manera indistinta "torres" y "estaciones de monitoreo" para referirse al mismo          ##
##                objeto físico...                                                                                  ##
##                                                                                                                  ##
## -> Las coordenadas generadas se encuentran dentro del rango siguiente:                                           ##
##                         latitudes ["19.079559" - "19.857710"]                                                    ##
##                         longitudes ["-98.763194" - "-99.495169"]                                                 ## 
##                                                                                                                  ##
##                                                  Versión 1.3                                                     ##
##                                          Fecha creación: 15/09/2019                                              ##
##                                        Última modificación: 29/10/2019                                           ##
##                                         Enrique Alfonso Carmona García                                           ##
##                                          eacarmona860920@gmail.com                                               ##
##                                                                                                                  ##
## -> La información relativa a la librería numpy (necesaria para pandas) puede ser consultada en:                  ##
##       https://docs.scipy.org/doc/                                                                                ##
## -> La información relativa a mysql.conector puede ser consultada en:                                             ##
##       https://dev.mysql.com/doc/connector-python/en/                                                             ##
##       Se requiere instalar "pip install mysql-connector-python"                                                  ## 
## -> La información relativa a la librería random puede ser consultada en:                                         ##
##       https://docs.python.org/2/library/random.html                                                              ##
## -> La información relativa a la librería geopy puede ser consultada en:                                          ##
##       https://pypi.org/project/geopy/                                                                            ##
##                                                                                                                  ##
######################################################################################################################

######################################################################################################################
##                                                                                                                  ##
## -> Cargando las librerías y funcionalidades necesarias...                                                        ##
##                                                                                                                  ##
###################################################################################################################### 

import mysql.connector
import random
from mysql.connector import errorcode
from geopy import distance

######################################################################################################################
##                                                                                                                  ##
## -> Listado de variables utilizadas...                                                                            ##
##           config [Contiene la información de configuración del servidor de base de datos MySQL]                  ##
##           nombreBd [Contiene el nombre de la base de datos]                                                      ##
##           tabla [Contiene las instrucciones SQL necesarias para crear las tablas en la base de datos]            ##
##           datos [Contiene toda la información necesaria para insertar un nuevo registro en la base de datos]     ##
##           add [Contiene las instrucciones SQL para insertar un registro nuevo en la base de datos]               ##
##           cnx [Para manejar la conección al servidor MySQL]                                                      ##
##           cursor [Para indicar las instrucciones al servidor MySQL]                                              ##
##                                                                                                                  ##
## -> Estableciendo las variables de configuración necesarias...                                                    ##
## -> Estableciendo la esctructura de las tablas en la base de datos...                                             ##
##                                                                                                                  ##
######################################################################################################################

nombreBDLocalizaciones = 'localizacionesexp'  ## Configuración para la base de datos de localización geográfica...
config = {
  'user': 'kike',
  'password': 'kike123',
  'host': '127.0.0.1',
  'database': 'localizacionesexp',
  'raise_on_warnings': True,
}

tablaLocalizaciones = {} ## Definición de la tabla de localización...
tablaLocalizaciones[nombreBDLocalizaciones] = ( 
    "CREATE TABLE `localizaciones` ("
    "   `IDLOC` INT NOT NULL AUTO_INCREMENT,"
    "   `LATITUD` DOUBLE NULL,"
    "   `LONGITUD` DOUBLE NULL,"
    "   `TORRESO2` TEXT NULL,"
    "   `TORRENO2` TEXT NULL,"
    "   `TORRERH` TEXT NULL,"
    "   `TORRECO` TEXT NULL,"
    "   `TORRENO` TEXT NULL,"
    "   `TORRENOX` TEXT NULL,"
    "   `TORREO3` TEXT NULL,"
    "   `TORREPM10` TEXT NULL,"
    "   `TORREPM25` TEXT NULL,"
    "   `TORREPA` TEXT NULL,"
    "   `TORREUVA` TEXT NULL,"
    "   `TORREUVB` TEXT NULL,"
    "   `TORRETEMP` TEXT NULL,"
    "   PRIMARY KEY (`IDLOC`));"
    "   ENGINE = InnoDB"
)

######################################################################################################################
##                                                                                                                  ##
## -> Creando una clase para convertir los tipos de datos a tipos MySQL...                                          ##
##                                                                                                                  ##
######################################################################################################################

class NumpyMySQLConverter(mysql.connector.conversion.MySQLConverter):
    
    """ A mysql.connector Converter que es capaz de manejar los tipos de datos de numpy... """

    def _float32_to_mysql(self, value):
        return float(value)

    def _float64_to_mysql(self, value):
        return float(value)

    def _int32_to_mysql(self, value):
        return int(value)

    def _int64_to_mysql(self, value):
        return int(value) 

######################################################################################################################
##                                                                                                                  ##
## -> Conectando al SGBD MySQL y creando las tablas definidas...                                                    ##
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
## -> Función para crear la base de datos en el formato correspondiente...                                          ##
##                                                                                                                  ##
######################################################################################################################

def create_database(cursor):  ## Función para la base de datos definida...
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(nombreBDLocalizaciones))
    except mysql.connector.Error as err:
        print ("   ")
        print("Error al crear la base de datos señalada: {}".format(err))
        exit(1)

######################################################################################################################
##                                                                                                                  ##
## -> Se solicita crear las base de datos...                                                                        ##
##                                                                                                                  ##
######################################################################################################################

try:  
    cnx.database = nombreBDLocalizaciones  
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = nombreBDLocalizaciones
    else:
        print ("   ")
        print(err)
        exit(1) 

######################################################################################################################
##                                                                                                                  ##
## -> Se solicita crear todas las tablas definidas...                                                               ##
##                                                                                                                  ##
######################################################################################################################

for name, ddl in tablaLocalizaciones.items():
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
## -> Generación de las coordenas aleatoriamente y almacenándolas en una estructura de lista...                     ##
## -> Se emplearán las estructuras:                                                                                 ##
##                            latitudes["Contendrá las latitudes generadas"]                                        ##
##                            longitudes["Contendrá las longitudes generadas"]                                      ##
##                            torreAsignada["Contendrá la torre asignada a cada coordenada"]                        ##
##                            torreXXXXXX["Contendrá los identificadores de las torres"]                            ##
##                            torreLatitud["Contendrá las latitudes de las torres"]                                 ##
##                            torreLongitud["Contendrá las longitudes de las torres"]                               ##
##                                                                                                                  ##
## -> Las latitudes se generarán entre los valores [19.079559 y 19.857710]...                                       ##
## -> Las longitudes se generarán entre los valores [-98.763194 y -99495169]...                                     ##
## -> Se generarán un total de 1 millón de coordenadas y se asignarán a cada torre, se seleccionará la torre con    ##
##       menor cantidad de coordenadas asignadas y esa será la máxima cantidad de coordenadas por cada torre a      ## 
##       guardar en la base de datos. [Este proceso se puede repetir las veces deseadas]...                         ##
##                                                                                                                  ##
######################################################################################################################

latitudes = []
longitudes = []
torreSO2 = ["ACO", "AJM", "ATI", "BJU", "CAM", "CCA", "CHO", "CUA", "CUT", "FAC", "HGM", "INN", "IZT", "LPR", 
            "LLA", "MER", "MGH", "MPA", "MON", "NEZ", "PED", "SAG", "SJA", "SFE", "TAH", "TLA", "TLI", "UIZ",
            "UAX", "VIF", "XAL"]
torreNO2 = ["ACO", "AJM", "ATI", "BJU", "CAM", "CCA", "CHO", "COY", "CUA", "CUT", "FAC", "HGM", "INN", "IZT",
            "LPR", "LLA", "MER", "MGH", "MPA", "MON", "NEZ", "PED", "SAG", "SJA", "SFE", "TAH", "TLA", "TLI",
            "UIZ", "UAX", "VIF", "XAL"]
torreRH = ["ACO", "AJU", "AJM", "BJU", "CHO", "CUA", "CUT", "FAC", "GAM", "HGM", "INN", "LAA", "MER", "MGH",
           "MPA", "MON", "NEZ", "PED", "SAG", "SFE", "TAH", "TLA", "UIZ", "UAX", "VIF", "XAL"]
torreCO = ["ACO", "AJM", "ATI", "BJU", "CAM", "CCA", "CHO", "CUA", "CUT", "FAC", "HGM", "INN", "IZT", "LPR",
           "LLA", "MER", "MGH", "MPA", "MON", "NEZ", "PED", "SAG", "SJA", "SFE", "TAH", "TLA", "TLI", "UIZ",
           "UAX", "VIF", "XAL"]
torreNO = ["ACO", "AJM", "ATI", "CAM", "CCA", "CHO", "COY", "CUA", "CUT", "FAC", "HGM", "INN", "IZT", "LPR",
           "LLA", "MER", "MGH", "MPA", "MON", "NEZ", "PED", "SAG", "SJA", "SFE", "TAH", "TLA", "TLI", "UIZ",
           "UAX", "VIF", "XAL"]
torreNOX = ["ACO", "AJM", "ATI", "CAM", "CCA", "CHO", "COY", "CUA", "CUT", "FAC", "HGM", "INN", "IZT", "LPR",
            "LLA", "MER", "MGH", "MPA", "MON", "NEZ", "PED", "SAG", "SJA", "SFE", "TAH", "TLA", "TLI", "UIZ",
            "UAX", "VIF", "XAL"]
torreO3 = ["ACO", "AJU", "AJM", "ATI", "BJU", "CAM", "CCA", "CHO", "COY", "CUA", "CUT", "FAC", "GAM", "HGM",
           "INN", "IZT", "LPR", "LLA", "MER", "MGH", "MPA", "MON", "NEZ", "PED", "SAG", "SJA", "SFE", "TAH",
           "TLA", "TLI", "UIZ", "UAX", "VIF", "XAL"]
torrePM10 = ["ACO", "AJM", "ATI", "BJU", "CAM", "CHO", "CUA", "CUT", "FAC", "HGM", "INN", "IZT", "LPR", "LLA",
             "MER", "MGH", "MPA", "PED", "SAG", "SFE", "TAH", "TLA", "TLI", "UIZ", "VIF", "XAL"]
torrePM25 = ["AJU", "AJM", "BJU", "CAM", "CCA", "COY", "CUA", "CUT", "FAC", "GAM", "HGM", "INN", "MER", "MGH",
             "MPA", "MON", "NEZ", "PED", "SAG", "SJA", "SFE", "TLA", "UIZ", "UAX", "XAL"]
torrePA = ["AJM", "CUT", "HGM", "INN", "LAA", "MER", "MPA", "MON", "TLA", "XAL"]
torreUVA = ["CHO", "CUT", "FAC", "LAA", "MER", "MPA", "MON", "PED", "SAG", "SFE", "TLA"]
torreUVB = ["CHO", "CUT", "FAC", "LAA", "MER", "MPA", "MON", "PED", "SAG", "SFE", "TLA"]
torreTEMP = ["ACO", "AJU", "AJM", "BJU", "CHO", "CUA", "CUT", "FAC", "GAM", "HGM", "INN", "LAA", "MER", "MGH",
             "MPA", "MON", "NEZ", "PED", "SAG", "SFE", "TAH", "TLA", "UIZ", "UAX", "VIF", "XAL"]
torreSO2Latitud = ["19.635501", "19.2721", "19.576963", "19.371612", "19.468404", "19.3262", "19.266948", 
                   "19.365313", "19.722186", "19.482473", "19.411617", "19.291968", "19.384413", "19.534727",
                   "19.578792", "1942461", "19.40405"]





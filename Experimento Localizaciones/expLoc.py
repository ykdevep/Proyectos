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
##                            torreAsignadaXXXXX["Contendrá la torre asignada a cada coordenada"]                   ##
##                            torreXXXXXX["Contendrá los identificadores de las torres"]                            ##
##                            torreXXXXLatitud["Contendrá las latitudes de las torres"]                             ##
##                            torreXXXXLongitud["Contendrá las longitudes de las torres"]                           ##
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
torreAsignadaSO2 = []
torreAsignadaNO2 = []
torreAsignadaRH = []
torreAsignadaCO = []
torreAsignadaNO = []
torreAsignadaNOX = []
torreAsignadaO3 = []
torreAsignadaPM10 = []
torreAsignadaPM25 = []
torreAsignadaPA = []
torreAsignadaUVA = []
torreAsignadaUVB = []
torreAsignadaTEMP = []
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
                   "19.578792", "19.42461", "19.40405", "19.1769", "19.460415", "19.393734", "19.325146", 
                   "19.532968", "19.452592", "19.357357", "19.246459", "19.529077", "19.602542", "19.360794",
                   "19.304441", "19.658223", "19.525995"]
torreSO2Longitud = ["-98.912003", "-99.207658", "-99.254133", "-99.158969", "-99.169794", "-99.1761", 
                    "-98.886088", "-99.291705", "-99.198602", "-99.243524", "-99.152207", "-99.38052", 
                    "-99.117641", "-99.11772", "-99.242062", "-99.119594", "-99.202603", "-98.990189",
                    "-98.902853", "-99.028212", "-99.204136", "-99.030324", "-99.086095", "-99.262865",
                    "-99.010564", "-99.204597", "-99.177173", "-99.07388", "-99.103629", "-99.09659", "-99.0824"]
torreNO2Latitud = ["19.635501", "19.2721", "19.576963", "19.371612", "19.468404", "19.3262", "19.266948",
                   "19.350258", "19.365313", "19.722186", "19.482473", "19.411617", "19.291968", "19.384413", 
                   "19.534727", "19.578792", "19.42461", "19.40405", "19.1769", "19.460415", "19.393734",
                   "19.325146", "19.532968", "19.452592", "19.357352", "19.246459", "19.529077", "19.602542",
                   "19.360794", "19.30441", "19.658223", "19.525995"]
torreNO2Longitud = ["-98.912003", "-99.207658", "-99.254133", "-99.158969", "-99.169794", "-99.1761",
                    "-98.886088", "-99.157101", "-99.291705", "-99.198602", "-99.243524", "-99.152207", "-99.38052", 
                    "-99.117641", "-99.11772", "-99.242062", "-99.119594", "-99.202603", "-98.990189",
                    "-98.902853", "-99.028212", "-99.204136", "-99.030324", "-99.086095", "-99.262865",
                    "-99.010564", "-99.204597", "-99.177173", "-99.07388", "-99.103629", "-99.09659", "-99.0824"]
torreRHLatitud = ["19.635501", "19.154674", "19.2721", "19.371612", "19.266948", "19.365313", "19.722186",
                  "19.482473", "19.4827", "19.411617", "19.291968", "19.483781", "19.42461", "19.40405",
                  "19.1769", "19.460415", "19.393734", "19.325146", "19.532968", "19.357357", "19.246459",
                  "19.529077", "19.360794", "19.304441", "19.658223", "19.525995"]
torreRHLongitud = ["-98.912003", "-99.162459", "-99.207658", "-99.158969", "-98.886088", "-99.291705",
                   "-99.198602", "-99.243524", "-99.094517", "-99.152207", "-99.38052", "-99.147312",
                   "-99.119594", "-99.202603", "-98.990189", "-98.902853", "-99.028212", "-99.204136",
                   "-99.030324", "-99.262865", "-99.010564", "-99.204597", "-99.07388", "-99.103629",
                   "-99.09659", "-99.0824"]
torreCOLatitud = ["19.635501", "19.2721", "19.576963", "19.371612", "19.468404", "19.3262", "19.266948",
                   "19.350258", "19.365313", "19.722186", "19.482473", "19.411617", "19.291968", "19.384413", 
                   "19.534727", "19.578792", "19.42461", "19.40405", "19.1769", "19.460415", "19.393734",
                   "19.325146", "19.532968", "19.452592", "19.357352", "19.246459", "19.529077", "19.602542",
                   "19.360794", "19.30441", "19.658223", "19.525995"]
torreCOLongitud = ["-98.912003", "-99.207658", "-99.254133", "-99.158969", "-99.169794", "-99.1761",
                    "-98.886088", "-99.157101", "-99.198602", "-99.243524", "-99.152207", "-99.38052", 
                    "-99.117641", "-99.11772", "-99.242062", "-99.119594", "-99.202603", "-98.990189",
                    "-98.902853", "-99.028212", "-99.204136", "-99.030324", "-99.086095", "-99.262865",
                    "-99.010564", "-99.204597", "-99.177173", "-99.07388", "-99.103629", "-99.09659", "-99.0824"]
torreNOLatitud = ["19.635501", "19.2721", "19.576963", "19.468404", "19.3262", "19.266948", "19.350258",
                  "19.365313", "19.722186", "19.482473", "19.411617", "19.291968", "19.384413", "19.534727",
                  "19.578792", "19.42461", "19.40405", "19.1769", "19.460415", "19.393734", "19.325146", 
                  "19.532968", "19.452592", "19.357357", "19.246459", "19.529077", "19.602542", "19.360794",
                  "19.304441", "19.658223", "19.525995"]
torreNOLongitud = ["-98.912003", "-99.207658", "-99.254133", "-99.169794", "-99.1761", "-98.886088", "-99.157101",
                   "-99.291705", "-99.198602", "-99.243524", "-99.152207", "-99.38052", "-99.117641", "-99.11772",
                   "-99.242062", "-99.119594", "-99.202603", "-98.990189", "-98.902853", "-99.028212", "-99.204136",
                   "-99.030324", "-99.086095", "-99.262865", "-99.010564", "-99.204597", "-99.177173", "-99.07388",
                   "-99.103629", "-99.09659", "-99.0824"]
torreNOXLatitud = ["19.635501", "19.2721", "19.576963", "19.468404", "19.3262", "19.266948", "19.350258",
                  "19.365313", "19.722186", "19.482473", "19.411617", "19.291968", "19.384413", "19.534727",
                  "19.578792", "19.42461", "19.40405", "19.1769", "19.460415", "19.393734", "19.325146", 
                  "19.532968", "19.452592", "19.357357", "19.246459", "19.529077", "19.602542", "19.360794",
                  "19.304441", "19.658223", "19.525995"]
torreNOXLongitud = ["-98.912003", "-99.207658", "-99.254133", "-99.169794", "-99.1761", "-98.886088", "-99.157101",
                   "-99.291705", "-99.198602", "-99.243524", "-99.152207", "-99.38052", "-99.117641", "-99.11772",
                   "-99.242062", "-99.119594", "-99.202603", "-98.990189", "-98.902853", "-99.028212", "-99.204136",
                   "-99.030324", "-99.086095", "-99.262865", "-99.010564", "-99.204597", "-99.177173", "-99.07388",
                   "-99.103629", "-99.09659", "-99.0824"]
torreO3Latitud = ["19.635501", "19.154674", "19.2721", "19.576963", "19.371612", "19.468404", "19.3262", "19.266948",
                  "19.350258", "19.365313", "19.722196", "19.482473", "19.4827", "19.411617", "19.291968", "19.384413",
                  "19.534727", "19.578792", "19.42461", "19.40405", "19.1769", "19.460415", "19.393734", "19.325146",
                  "19.532968", "19.452592", "19.357357", "19.246459", "19.529077", "19.602542", "19.360794",
                  "19.304441", "19.658223", "19.525995"]
torreO3Longitud = ["-98.912003", "-99.162459", "-99.206758", "-99.254133", "-99.158969", "-99.169794", "-99.1761",
                   "-98.886088", "-99.157101", "-99.291705", "-99.198602", "-99.243524", "-99.094517", "-99.152207",
                   "-99.38052", "-99.117641", "-99.11772", "-99.242062", "-99.119594", "-99.202603", "-98.990189",
                   "-98.902853", "-99.028212", "-99.204136", "-99.030324", "-99.086095", "-99.262865", "-99.010564",
                   "-99.204597", "-99.177173", "-99.07388", "-99.103629", "-99.09659", "-99.0824"]
torrePM10Latitud = ["19.635501", "19.2721", "19.576963", "19.371612", "19.468404", "19.266948", "19.365313",
                    "19.722186", "19.482473", "19.411617", "19.291986", "19.384413", "19.534727", "19.578792",
                    "19.42461", "19.40405","19.1769", "19.325146", "19.532968", "19.357357", "19.246459",
                    "19.529077", "19.602542", "19.360794", "19.658223", "19.525995"]
torrePM10Longitud = ["-98.912003", "-99.207658", "-99.254133", "-99.158969", "-99.169794", "-98.886088", "-99.291705",
                     "-99.198602", "-99.243524", "-99.152207", "-99.38052", "-99.117641", "-99.11772", "-99.039644",
                     "-99.119594", "-99.202603", "-98.990189", "-99.204136", "-99.030324", "-99.262865", "-99.010564",
                     "-99.204597", "-99.177173", "-99.07388", "-99.09659", "-99.0824"]
torrePM25Latitud = ["19.154674", "19.2721", "19.371612", "19.468404", "19.3262", "19.350258", "19.365313", "19.722186",
                    "19.482473", "19.4827", "19.411617", "19.291968", "19.42461", "19.40405", "19.1769", "19.460415",
                    "19.393734", "19.325146", "19.532968", "19.452592", "19.357357", "19.529077", "19.360794",
                    "19.304441", "19.525995"]
torrePM25Longitud = ["-99.162459", "-99.207658", "-99.158969", "-99.169794", "-99.1761", "-99.157101", "-99.291705",
                     "-99.198602", "-99.243524", "-99.094517", "-99.152207", "-99.38052", "-99.119594", "-99.202603",
                     "-98.990189", "-98.902853", "-99.028212", "-99.204136", "-99.030324", "-99.086095", "-99.262865",
                     "-99.204597", "-99.07388", "-99.103629", "-99.0824"]
torrePALatitud = ["19.2721", "19.722186", "19.411617", "19.291968", "19.483781", "19.42461", "19.1769", "19.460415",
                  "19.529077", "19.525995"]
torrePALongitud = ["-99.207658", "-99.198602", "-99.152207", "-99.38052", "-99.147312", "-99.119594", "-98.990189",
                   "-98.902853", "-99.204597", "-99.0824"]
torreUVALatitud = ["19.266948", "19.722186", "19.482473", "19.483781", "19.42461", "19.1769", "19.460415", "19.325146",
                   "19.532968", "19.357357", "19.529077"]
torreUVALongitud = ["-98.886088", "-99.198602", "-99.243524", "-99.147312", "-99.119594", "-98.990189", "-98.902853",
                    "-99.204136", "-99.030324", "-99.262865", "-99.204597"]
torreUVBLatitud = ["19.266948", "19.722186", "19.482473", "19.483781", "19.42461", "19.1769", "19.460415", "19.325146",
                   "19.532968", "19.357357", "19.529077"]
torreUVBLongitud = ["-98.886088", "-99.198602", "-99.243524", "-99.147312", "-99.119594", "-98.990189", "-98.902853",
                    "-99.204136", "-99.030324", "-99.262865", "-99.204597"]
torreTEMPLatitud = ["19.635501", "19.154674", "19.2721", "19.371612", "19.266948", "19.365313", "19.722186", "19.482473",
                    "19.4827", "19.411617", "19.291968", "19.483781", "19.42461", "19.40405", "19.1769", "19.460415",
                    "19.393734", "19.325146", "19.532968", "19.357357", "19.246459", "19.529077", "19.360794",
                    "19.304441", "19.658223", "19.525995"]
torreTEMPLongitud = ["-98.912003", "-99.162459", "-99.207658", "-99.158969", "-98.886088", "-99.291705", "-99.198602",
                     "-99.243524", "-99.094517", "-99.152207", "-99.38052", "-99.147312", "-99.119594", "-99.202603",
                     "-98.990189", "-98.902853", "-99.028212", "-99.204136", "-99.030324", "-99.262865", "-99.010564",
                     "-99.204597", "-99.07388", "-99.103629", "-99.09659", "-99.0824"]

######################################################################################################################
##                                                                                                                  ##
##  -> Generación aleatoria de coordenadas geográficas a partir de los límites establecidos...                      ##
##  -> Conversión para el entero generado a un valor de coordenada geográfica...                                    ##
##                    -> valoresTotales (Es la cantidad de valores a generar aleatoriamente)                        ##
##                                                                                                                  ##
######################################################################################################################

valoresTotales = 5000
for i in range(0, valoresTotales):
    latitudes.append(random.randint(19079559, 19857710))
    longitudes.append(random.randint(98763194, 99495169))
    longitudes[i] = longitudes[i] * (-1)
    latitudes[i] = (str(latitudes[i])[0:2] + "." + str(latitudes[i])[2:])
    longitudes[i] = (str(longitudes[i])[0:3] + "." + str(longitudes[i])[3:])

######################################################################################################################
##                                                                                                                  ##
## -> Las variables corresponden a sus respectivos campos en la base de datos (Ver descripción anterior)...         ##
##        datosLoc [Contiene la información de la latitud, longitud y de la torre asignada]...                      ##
##                 (La torre seleccionada es la más cercana a las coordenadas seleccionadas)...                     ##
## -> Consulta SQL necesaria para insertar los valores en la base de datos...  [addLoc]                             ##
##                                                                                                                  ##
######################################################################################################################

latit = ""
longit = ""
torreDSO2 = ""
torreDNO2 = ""
torreDRH = ""
torreDCO = ""
torreDNO = ""
torreDNOX = ""
torreDO3 = ""
torreDPM10 = ""
torreDPM25 = ""
torreDPA = ""
torreDUVA = ""
torreDUVB = ""
torreDTEMP = ""

datosLoc = {
    'datoLatitud' : latit,
    'datoLongitud' : longit,
    'datoTorreSO2' : torreDSO2,
    'datoTorreNO2' : torreDNO2,
    'datoTorreRH' : torreDRH,
    'datoTorreCO' : torreDCO,
    'datoTorreNO' : torreDNO,
    'datoTorreNOX' : torreDNOX,
    'datoTorreO3' : torreDO3,
    'datoTorrePM10' : torreDPM10,
    'datoTorrePM25' : torreDPM25,
    'datoTorrePA' : torreDPA,
    'datoTorreUVA' : torreDUVA,
    'datoTorreUVB' : torreDUVB,
    'datoTorreTEMP' : torreDTEMP,
}

addLoc = ("INSERT INTO localizaciones"
                "(LATITUD, LONGITUD, TORRESO2, TORRENO2, TORRERH, TORRECO, TORRENO, TORRENOX, TORREO3, TORREPM10, TORREPM25, TORREPA, TORREUVA, TORREUVB, TORRETEMP)"
                "VALUES (%(datoLatitud)s, %(datoLongitud)s, %(datoTorreSO2)s, %(datoTorreNO2)s, %(datoTorreRH)s, %(datoTorreCO)s, %(datoTorreNO)s, %(datoTorreNOX)s, %(datoTorreO3)s, %(datoTorrePM10)s, %(datoTorrePM25)s, %(datoTorrePA)s, %(datoTorreUVA)s, %(datoTorreUVB)s, %(datoTorreTEMP)s)"
            )

######################################################################################################################
##                                                                                                                  ##
## -> Se calculan las distancias a cada una de las torres y se selecciona la torre más cercana para cada una de     ##
##       las coordenadas generadas por cada uno de los contaminantes...                                             ##      
##                                                                                                                  ##
######################################################################################################################

for i in range(0, valoresTotales):

    ###
    ### Se determina la menor distancia para las torres de contaminantes SO2...
    ###

    distanciasAtorresSO2 = []
    menorDistanciaSO2 = 9999999999999
    posicionMenorDistanciaSO2 = -99
    for j in range(len(torreSO2)):
        coordenada1 = (latitudes[i], longitudes[i])
        coordenada2 = (torreSO2Latitud[j], torreSO2Longitud[j])
        distanciasAtorresSO2.append(distance.distance(coordenada1, coordenada2))
        if(distanciasAtorresSO2[j] < menorDistanciaSO2):
            menorDistanciaSO2 = distanciasAtorresSO2[j]
            posicionMenorDistanciaSO2 = j
    torreAsignadaSO2.append(torreSO2[posicionMenorDistanciaSO2])

    ###
    ### Se determina la menor distancia para las torres de contaminantes NO2...
    ###

    distanciasAtorresNO2 = []
    menorDistanciaNO2 = 9999999999999
    posicionMenorDistanciaNO2 = -99
    for j in range(len(torreNO2)):
        coordenada1 = (latitudes[i], longitudes[i])
        coordenada2 = (torreNO2Latitud[j], torreNO2Longitud[j])
        distanciasAtorresNO2.append(distance.distance(coordenada1, coordenada2))
        if(distanciasAtorresNO2[j] < menorDistanciaNO2):
            menorDistanciaNO2 = distanciasAtorresNO2[j]
            posicionMenorDistanciaNO2 = j
    torreAsignadaNO2.append(torreNO2[posicionMenorDistanciaNO2])

    ###
    ### Se determina la menor distancia para las torres de contaminantes RH...
    ###

    distanciasAtorresRH = []
    menorDistanciaRH = 9999999999999
    posicionMenorDistanciaRH = -99
    for j in range(len(torreRH)):
        coordenada1 = (latitudes[i], longitudes[i])
        coordenada2 = (torreRHLatitud[j], torreRHLongitud[j])
        distanciasAtorresRH.append(distance.distance(coordenada1, coordenada2))
        if(distanciasAtorresRH[j] < menorDistanciaRH):
            menorDistanciaRH = distanciasAtorresRH[j]
            posicionMenorDistanciaRH = j
    torreAsignadaRH.append(torreSO2[posicionMenorDistanciaRH])

    ###
    ### Se determina la menor distancia para las torres de contaminantes CO...
    ###

    distanciasAtorresCO = []
    menorDistanciaCO = 9999999999999
    posicionMenorDistanciaCO = -99
    for j in range(len(torreCO)):
        coordenada1 = (latitudes[i], longitudes[i])
        coordenada2 = (torreCOLatitud[j], torreCOLongitud[j])
        distanciasAtorresCO.append(distance.distance(coordenada1, coordenada2))
        if(distanciasAtorresCO[j] < menorDistanciaCO):
            menorDistanciaCO = distanciasAtorresCO[j]
            posicionMenorDistanciaCO = j
    torreAsignadaCO.append(torreCO[posicionMenorDistanciaCO])

    ###
    ### Se determina la menor distancia para las torres de contaminantes NO...
    ###

    distanciasAtorresNO = []
    menorDistanciaNO = 9999999999999
    posicionMenorDistanciaNO = -99
    for j in range(len(torreNO)):
        coordenada1 = (latitudes[i], longitudes[i])
        coordenada2 = (torreNOLatitud[j], torreNOLongitud[j])
        distanciasAtorresNO.append(distance.distance(coordenada1, coordenada2))
        if(distanciasAtorresNO[j] < menorDistanciaNO):
            menorDistanciaNO = distanciasAtorresNO[j]
            posicionMenorDistanciaNO = j
    torreAsignadaNO.append(torreNO[posicionMenorDistanciaNO])

    ###
    ### Se determina la menor distancia para las torres de contaminantes NOX...
    ###

    distanciasAtorresNOX = []
    menorDistanciaNOX = 9999999999999
    posicionMenorDistanciaNOX = -99
    for j in range(len(torreNOX)):
        coordenada1 = (latitudes[i], longitudes[i])
        coordenada2 = (torreNOXLatitud[j], torreNOXLongitud[j])
        distanciasAtorresNOX.append(distance.distance(coordenada1, coordenada2))
        if(distanciasAtorresNOX[j] < menorDistanciaNOX):
            menorDistanciaNOX = distanciasAtorresNOX[j]
            posicionMenorDistanciaNOX = j
    torreAsignadaNOX.append(torreNOX[posicionMenorDistanciaNOX])

    ###
    ### Se determina la menor distancia para las torres de contaminantes O3...
    ###

    distanciasAtorresO3 = []
    menorDistanciaO3 = 9999999999999
    posicionMenorDistanciaO3 = -99
    for j in range(len(torreO3)):
        coordenada1 = (latitudes[i], longitudes[i])
        coordenada2 = (torreO3Latitud[j], torreO3Longitud[j])
        distanciasAtorresO3.append(distance.distance(coordenada1, coordenada2))
        if(distanciasAtorresO3[j] < menorDistanciaO3):
            menorDistanciaO3 = distanciasAtorresO3[j]
            posicionMenorDistanciaO3 = j
    torreAsignadaO3.append(torreO3[posicionMenorDistanciaO3])

    ###
    ### Se determina la menor distancia para las torres de contaminantes PM10...
    ###

    distanciasAtorresPM10 = []
    menorDistanciaPM10 = 9999999999999
    posicionMenorDistanciaPM10 = -99
    for j in range(len(torrePM10)):
        coordenada1 = (latitudes[i], longitudes[i])
        coordenada2 = (torrePM10Latitud[j], torrePM10Longitud[j])
        distanciasAtorresPM10.append(distance.distance(coordenada1, coordenada2))
        if(distanciasAtorresPM10[j] < menorDistanciaPM10):
            menorDistanciaPM10 = distanciasAtorresPM10[j]
            posicionMenorDistanciaPM10 = j
    torreAsignadaPM10.append(torrePM10[posicionMenorDistanciaPM10])

    ###
    ### Se determina la menor distancia para las torres de contaminantes PM25...
    ###

    distanciasAtorresPM25 = []
    menorDistanciaPM25 = 9999999999999
    posicionMenorDistanciaPM25 = -99
    for j in range(len(torrePM25)):
        coordenada1 = (latitudes[i], longitudes[i])
        coordenada2 = (torrePM25Latitud[j], torrePM25Longitud[j])
        distanciasAtorresPM25.append(distance.distance(coordenada1, coordenada2))
        if(distanciasAtorresPM25[j] < menorDistanciaPM25):
            menorDistanciaPM25 = distanciasAtorresPM25[j]
            posicionMenorDistanciaPM25 = j
    torreAsignadaPM25.append(torrePM25[posicionMenorDistanciaPM25])

    ###
    ### Se determina la menor distancia para las torres de contaminantes PA...
    ###

    distanciasAtorresPA = []
    menorDistanciaPA = 9999999999999
    posicionMenorDistanciaPA = -99
    for j in range(len(torrePA)):
        coordenada1 = (latitudes[i], longitudes[i])
        coordenada2 = (torrePALatitud[j], torrePALongitud[j])
        distanciasAtorresPA.append(distance.distance(coordenada1, coordenada2))
        if(distanciasAtorresPA[j] < menorDistanciaPA):
            menorDistanciaPA = distanciasAtorresPA[j]
            posicionMenorDistanciaPA = j
    torreAsignadaPA.append(torrePA[posicionMenorDistanciaPA])

    ###
    ### Se determina la menor distancia para las torres de contaminantes UVA...
    ###

    distanciasAtorresUVA = []
    menorDistanciaUVA = 9999999999999
    posicionMenorDistanciaUVA = -99
    for j in range(len(torreUVA)):
        coordenada1 = (latitudes[i], longitudes[i])
        coordenada2 = (torreUVALatitud[j], torreUVALongitud[j])
        distanciasAtorresUVA.append(distance.distance(coordenada1, coordenada2))
        if(distanciasAtorresUVA[j] < menorDistanciaUVA):
            menorDistanciaUVA = distanciasAtorresUVA[j]
            posicionMenorDistanciaUVA = j
    torreAsignadaUVA.append(torreUVA[posicionMenorDistanciaUVA])

    ###
    ### Se determina la menor distancia para las torres de contaminantes UVB...
    ###

    distanciasAtorresUVB = []
    menorDistanciaUVB = 9999999999999
    posicionMenorDistanciaUVB = -99
    for j in range(len(torreUVB)):
        coordenada1 = (latitudes[i], longitudes[i])
        coordenada2 = (torreUVBLatitud[j], torreUVBLongitud[j])
        distanciasAtorresUVB.append(distance.distance(coordenada1, coordenada2))
        if(distanciasAtorresUVB[j] < menorDistanciaUVB):
            menorDistanciaUVB = distanciasAtorresUVB[j]
            posicionMenorDistanciaUVB = j
    torreAsignadaUVB.append(torreUVB[posicionMenorDistanciaUVB])

    ###
    ### Se determina la menor distancia para las torres de contaminantes TEMP...
    ###

    distanciasAtorresTEMP = []
    menorDistanciaTEMP = 9999999999999
    posicionMenorDistanciaTEMP = -99
    for j in range(len(torreTEMP)):
        coordenada1 = (latitudes[i], longitudes[i])
        coordenada2 = (torreTEMPLatitud[j], torreTEMPLongitud[j])
        distanciasAtorresTEMP.append(distance.distance(coordenada1, coordenada2))
        if(distanciasAtorresTEMP[j] < menorDistanciaTEMP):
            menorDistanciaTEMP = distanciasAtorresTEMP[j]
            posicionMenorDistanciaTEMP = j
    torreAsignadaTEMP.append(torreTEMP[posicionMenorDistanciaTEMP])

######################################################################################################################
##                                                                                                                  ##
## -> Se asignan los valores a cada una de las variables para insertar los valores adecuados en la base de datos    ##
##                                                                                                                  ##
######################################################################################################################

for i in range(0, valoresTotales):
    latit = float(latitudes[i])
    longit = float(longitudes[i])
    torreDSO2 = torreAsignadaSO2[i]
    torreDNO2 = torreAsignadaNO2[i]
    torreDRH = torreAsignadaRH[i]
    torreDCO = torreAsignadaCO[i]
    torreDNO = torreAsignadaNO[i]
    torreDNOX = torreAsignadaNOX[i]
    torreDO3 = torreAsignadaO3[i]
    torreDPM10 = torreAsignadaPM10[i]
    torreDPM25 = torreAsignadaPM25[i]
    torreDPA = torreAsignadaPA[i]
    torreDUVA = torreAsignadaUVA[i]
    torreDUVB = torreAsignadaUVB[i]
    torreDTEMP = torreAsignadaTEMP[i]

    datosLoc = {
    'datoLatitud' : latit,
    'datoLongitud' : longit,
    'datoTorreSO2' : torreDSO2,
    'datoTorreNO2' : torreDNO2,
    'datoTorreRH' : torreDRH,
    'datoTorreCO' : torreDCO,
    'datoTorreNO' : torreDNO,
    'datoTorreNOX' : torreDNOX,
    'datoTorreO3' : torreDO3,
    'datoTorrePM10' : torreDPM10,
    'datoTorrePM25' : torreDPM25,
    'datoTorrePA' : torreDPA,
    'datoTorreUVA' : torreDUVA,
    'datoTorreUVB' : torreDUVB,
    'datoTorreTEMP' : torreDTEMP,
    }

    print ("Insertando registro " + str(i) + " de " + str(valoresTotales))
    cursor.execute(addLoc, datosLoc)
    cnx.commit()
    print ("Registro " + str(i) +  " insertado, completado el " + str(int(i)*100/int(valoresTotales)) +  " porciento del total de datos")

######################################################################################################################
##                                                                                                                  ##
##                                     Cerrando las conexiones a la base de datos...                                ##
##                                                                                                                  ##
######################################################################################################################

print ("Se insertaron adecuadamente el 100 porciento de los datos en la base de datos.")
cursor.close()
cnx.close()

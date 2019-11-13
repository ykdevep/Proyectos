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
    "   `TORRE` TEXT NULL,"
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
##                            torreNombre["Contendrá los identificadores de las torres"]                            ##
##                            torreLatitud["Contendrá las latitudes de las torres"]                                 ##
##                            torreLongitud["Contendrá las longitudes de las torres"]                               ##
##                            cantidadTorre["Contendrá la cantidad de valores asignados a cada torre"]              ##
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
torreAsignada = []
torreNombre = ["ACO", "AJU", "AJM", "ATI", "BJU", "CAM", "CCA", "TEC", "CHO", "COR", "COY", "CUA", "CUT", "DIC",
               "EAJ", "EDL", "FAC", "GAM", "HGM", "INN", "IZT", "LPR", "LAA", "IBM", "LOM", "LLA", "MER", "MGH", 
               "MPA", "MON", "MCM", "NEZ", "PED", "SAG", "SJA", "SNT", "SFE", "SHA", "TAH", "TLA", "TLI", "UIZ", 
               "UAX", "VIF", "XAL"]
torreLatitud = ["19.635501", "19.154674", "19.2721", "19.576963", "19.371612", "19.468404", "19.3262", "19.487227",
                "19.266948", "19.265346", "19.350258", "19.365313", "19.722186", "19.298819", "19.271222", 
                "19.313357", "19.482473", "19.4827", "19.40405", "19.291968", "19.384413", "19.534727", "19.483781",
                "19.443319", "19.403", "19.578792", "19.42461", "19.40405", "19.1769", "19.460415", "19.429071", 
                "19.393734", "19.325146", "19.532968", "19.452592", "19.250385", "19.357357", "19.446203", "19.246459", 
                "19.529077", "19.602542", "19.360794", "19.304441", "19.658223", "19.525995"]
torreLongitud = ["-98.912003", "-99.162459", "-99.207658", "-99.254133", "-99.158969", "-99.169794", "-99.1761",
                 "-99.114229", "-98.886088", "-99.02604", "-99.157101", "-99.291705", "-99.198602", "-99.185774",
                 "-99.203971", "-99.310635", "-99.243524", "-99.094517", "-99.202603", "-99.38052", "-99.117641", 
                 "-99.11772", "-99.147312", "-99.21536", "-99.242062", "-99.039644", "-99.119594", "-99.202603", 
                 "-98.990189", "-98.902853", "-99.131924", "-99.028212", "-99.204136", "-99.030324", "-99.086095", 
                 "-99.256462", "-99.262865", "-99.207868", "-99.010564", "-99.204597", "-99.177173", "-99.07388", 
                 "-99.103629", "-99.09659", "-99.0824"]
cantidadTorre = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cantidadTorreAInsertar = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

######################################################################################################################
##                                                                                                                  ##
##  -> Generación aleatoria de 1 millón de coordenadas geográficas a partir de los límites establecidos...          ##
##  -> Conversión para el entero generado a un valor de coordenada geográfica...                                    ##
##                                                                                                                  ##
######################################################################################################################

for i in range(0, 1000000):
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
torre = ""

datosLoc = {
    'datoLatitud' : latit,
    'datoLongitud' : longit,
    'datoTorre' : torre,
}

addLoc = ("INSERT INTO localizaciones"
                "(LATITUD, LONGITUD, TORRE)"
                "VALUES (%(datoLatitud)s, %(datoLongitud)s, %(datoTorre)s)"
            )

######################################################################################################################
##                                                                                                                  ##
## -> Se calculan las distancias a cada una de las torres y se selecciona la torre más cercana para cada una de     ##
##       las coordenadas generadas...                                                                               ##      
##                                                                                                                  ##
######################################################################################################################

for i in range(0, 1000000):
    distanciasATorres = []
    menorDistancia = 9999999999999
    posicionMenorDistancia = -99
    for j in range(0,45):
        coordenada1 = (latitudes[i], longitudes[i])
        coordenada2 = (torreLatitud[j], torreLongitud[j])
        distanciasATorres.append(distance.distance(coordenada1, coordenada2))
        if (distanciasATorres[j] < menorDistancia):
            menorDistancia = distanciasATorres[j]
            posicionMenorDistancia = j
    
    torreAsignada.append(torreNombre[posicionMenorDistancia])
    cantidadTorre[posicionMenorDistancia] = cantidadTorre[posicionMenorDistancia] + 1

cantidadTorre.sort()
menorTotalTorres = cantidadTorre[0]
print ("Se insertaran un total de " + str(menorTotalTorres) + " en la base de datos.")

for i in range(0, 1000000):
    if (torreAsignada[i] == "ACO" and cantidadTorreAInsertar[0] <= menorTotalTorres):
        cantidadTorreAInsertar[0] = cantidadTorreAInsertar[0] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "AJU" and cantidadTorreAInsertar[1] <= menorTotalTorres):
        cantidadTorreAInsertar[1] = cantidadTorreAInsertar[1] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "AJM" and cantidadTorreAInsertar[2] <= menorTotalTorres):
        cantidadTorreAInsertar[2] = cantidadTorreAInsertar[2] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "ATI" and cantidadTorreAInsertar[3] <= menorTotalTorres):
        cantidadTorreAInsertar[3] = cantidadTorreAInsertar[3] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "BJU" and cantidadTorreAInsertar[4] <= menorTotalTorres):
        cantidadTorreAInsertar[4] = cantidadTorreAInsertar[4] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "CAM" and cantidadTorreAInsertar[5] <= menorTotalTorres):
        cantidadTorreAInsertar[5] = cantidadTorreAInsertar[5] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "CCA" and cantidadTorreAInsertar[6] <= menorTotalTorres):
        cantidadTorreAInsertar[6] = cantidadTorreAInsertar[6] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "TEC" and cantidadTorreAInsertar[7] <= menorTotalTorres):
        cantidadTorreAInsertar[7] = cantidadTorreAInsertar[7] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "CHO" and cantidadTorreAInsertar[8] <= menorTotalTorres):
        cantidadTorreAInsertar[8] = cantidadTorreAInsertar[8] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "COR" and cantidadTorreAInsertar[9] <= menorTotalTorres):
        cantidadTorreAInsertar[9] = cantidadTorreAInsertar[9] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "COY" and cantidadTorreAInsertar[10] <= menorTotalTorres):
        cantidadTorreAInsertar[10] = cantidadTorreAInsertar[10] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "CUA" and cantidadTorreAInsertar[11] <= menorTotalTorres):
        cantidadTorreAInsertar[11] = cantidadTorreAInsertar[11] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "CUT" and cantidadTorreAInsertar[12] <= menorTotalTorres):
        cantidadTorreAInsertar[12] = cantidadTorreAInsertar[12] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "DIC" and cantidadTorreAInsertar[13] <= menorTotalTorres):
        cantidadTorreAInsertar[13] = cantidadTorreAInsertar[13] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "EAJ" and cantidadTorreAInsertar[14] <= menorTotalTorres):
        cantidadTorreAInsertar[14] = cantidadTorreAInsertar[14] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "EDL" and cantidadTorreAInsertar[15] <= menorTotalTorres):
        cantidadTorreAInsertar[15] = cantidadTorreAInsertar[15] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "FAC" and cantidadTorreAInsertar[16] <= menorTotalTorres):
        cantidadTorreAInsertar[16] = cantidadTorreAInsertar[16] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "GAM" and cantidadTorreAInsertar[17] <= menorTotalTorres):
        cantidadTorreAInsertar[17] = cantidadTorreAInsertar[17] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "HGM" and cantidadTorreAInsertar[18] <= menorTotalTorres):
        cantidadTorreAInsertar[18] = cantidadTorreAInsertar[18] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "INN" and cantidadTorreAInsertar[19] <= menorTotalTorres):
        cantidadTorreAInsertar[19] = cantidadTorreAInsertar[19] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "IZT" and cantidadTorreAInsertar[20] <= menorTotalTorres):
        cantidadTorreAInsertar[20] = cantidadTorreAInsertar[20] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "LPR" and cantidadTorreAInsertar[21] <= menorTotalTorres):
        cantidadTorreAInsertar[21] = cantidadTorreAInsertar[21] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "LAA" and cantidadTorreAInsertar[22] <= menorTotalTorres):
        cantidadTorreAInsertar[22] = cantidadTorreAInsertar[22] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "IBM" and cantidadTorreAInsertar[23] <= menorTotalTorres):
        cantidadTorreAInsertar[23] = cantidadTorreAInsertar[23] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")
    
    if (torreAsignada[i] == "LOM" and cantidadTorreAInsertar[24] <= menorTotalTorres):
        cantidadTorreAInsertar[24] = cantidadTorreAInsertar[24] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "LLA" and cantidadTorreAInsertar[25] <= menorTotalTorres):
        cantidadTorreAInsertar[25] = cantidadTorreAInsertar[25] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "MER" and cantidadTorreAInsertar[26] <= menorTotalTorres):
        cantidadTorreAInsertar[26] = cantidadTorreAInsertar[26] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "MGH" and cantidadTorreAInsertar[27] <= menorTotalTorres):
        cantidadTorreAInsertar[27] = cantidadTorreAInsertar[27] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "MPA" and cantidadTorreAInsertar[28] <= menorTotalTorres):
        cantidadTorreAInsertar[28] = cantidadTorreAInsertar[28] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "MON" and cantidadTorreAInsertar[29] <= menorTotalTorres):
        cantidadTorreAInsertar[29] = cantidadTorreAInsertar[29] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "MCM" and cantidadTorreAInsertar[30] <= menorTotalTorres):
        cantidadTorreAInsertar[30] = cantidadTorreAInsertar[30] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "NEZ" and cantidadTorreAInsertar[31] <= menorTotalTorres):
        cantidadTorreAInsertar[31] = cantidadTorreAInsertar[31] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "PED" and cantidadTorreAInsertar[32] <= menorTotalTorres):
        cantidadTorreAInsertar[32] = cantidadTorreAInsertar[32] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "SAG" and cantidadTorreAInsertar[33] <= menorTotalTorres):
        cantidadTorreAInsertar[33] = cantidadTorreAInsertar[33] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "SJA" and cantidadTorreAInsertar[34] <= menorTotalTorres):
        cantidadTorreAInsertar[34] = cantidadTorreAInsertar[34] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "SNT" and cantidadTorreAInsertar[35] <= menorTotalTorres):
        cantidadTorreAInsertar[35] = cantidadTorreAInsertar[35] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "SFE" and cantidadTorreAInsertar[36] <= menorTotalTorres):
        cantidadTorreAInsertar[36] = cantidadTorreAInsertar[36] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "SHA" and cantidadTorreAInsertar[37] <= menorTotalTorres):
        cantidadTorreAInsertar[37] = cantidadTorreAInsertar[37] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "TAH" and cantidadTorreAInsertar[38] <= menorTotalTorres):
        cantidadTorreAInsertar[38] = cantidadTorreAInsertar[38] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "TLA" and cantidadTorreAInsertar[39] <= menorTotalTorres):
        cantidadTorreAInsertar[39] = cantidadTorreAInsertar[39] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "TLI" and cantidadTorreAInsertar[40] <= menorTotalTorres):
        cantidadTorreAInsertar[40] = cantidadTorreAInsertar[40] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "UIZ" and cantidadTorreAInsertar[41] <= menorTotalTorres):
        cantidadTorreAInsertar[41] = cantidadTorreAInsertar[41] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "UAX" and cantidadTorreAInsertar[42] <= menorTotalTorres):
        cantidadTorreAInsertar[42] = cantidadTorreAInsertar[42] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "VIF" and cantidadTorreAInsertar[43] <= menorTotalTorres):
        cantidadTorreAInsertar[43] = cantidadTorreAInsertar[43] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

    if (torreAsignada[i] == "XAL" and cantidadTorreAInsertar[44] <= menorTotalTorres):
        cantidadTorreAInsertar[44] = cantidadTorreAInsertar[44] + 1
        latit = latitudes[i]
        longit = longitudes[i]
        torre = torreAsignada[i]

        datosLoc = {
                    'datoLatitud' : latit,
                    'datoLongitud' : longit,
                    'datoTorre' : torre,
                    }

        print ("Insertando registro")
        cursor.execute(addLoc, datosLoc)
        cnx.commit()
        print ("Registro insertado")

######################################################################################################################
##                                                                                                                  ##
## -> Cerrando las conexiones a la base de datos...                                                                 ##
##                                                                                                                  ##
######################################################################################################################

print (cantidadTorreAInsertar)
print ("Se insertaron adecuadamente el 100 porciento de los datos en la base de datos.")
cursor.close()
cnx.close()


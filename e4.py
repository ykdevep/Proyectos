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

######################################################################################################################
##                                                                                                                  ##
##                                      Listado de variables utilizadas...                                          ##
##                                                                                                                  ##
## direccionFichero [Contiene la ruta donde se encuentra el fichero csv a leer]...                                  ##
## (direccionFicheroIBI, direccionFicheroHRV, direccionFicheroEDA, direccionFicheroACC, direccionFicheroBVP)...     ##
## csv [Contiene la información del fichero csv cargado]...                                                         ##
## (csvIBI, csvHRV, csvEDA, csvACC, csvBVP)...                                                                      ##
##                                                                                                                  ##
## config [Contiene la información de configuración del servidor de base de datos MySQL]...                         ##
## nombreBd [Contiene el nombre de la base de datos]...                                                             ##
## (nombreBdUsuario, nombreBdWearable, nombreBdAlmacenWearable)...                                                  ##
## tabla [Contiene las instrucciones SQL necesarias para crear las tablas en la base de datos]...                   ##
## (tablaUsuario, tablaWearable, tablaALmacenWearable)...                                                           ##
##                                                                                                                  ##
## Las variables (idUsuario, nombreUsuario, primerApellidoUsuario, segundoApellidoUsuario, sexoUsuario,             ##
## edadUsuario, pesoUsuario, frecuenciaEjercicioUsuario) contienen la información de los usuarios...                ##
## Las variables (idWearable, tiempoWearable, ibiWearable, hrvWearable, edaWearable, bvpWearable, accXWearable,     ##
## accYWearable, accZWearable) contienen la información de cada uno de los registros del csv cargado...             ##
##                                                                                                                  ##                                                        
## datosUsuario [Contiene toda la información necesaria para insertar un nuevo registro en la base de datos]...     ##
## datosWearable [Contiene toda la información necesaria para insertar un nuevo registro en la base de datos]...    ##
## datosAlmacenWearable [Contiene toda la información para insertar un nuevo registro en la base de datos]...       ##
## addUsuario [Contiene las instrucciones SQL necesarias para insertar un registro nuevo en la base de datos]...    ##
## addWearable [Contiene las instrucciones SQL necesarias para insertar un registro nuevo en la base de datos]...   ##
## addAlmacenWearable [Contiene las instrucciones SQL para insertar un registro nuevo en la base de datos]...       ##
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


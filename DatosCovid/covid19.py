##########################################################################################################################
##                                                                                                                      ##
## -> Módulo Python 3.7.4 (64 bits) para cargar la información relacionada al COVID-19 en México en un SGBD MySQL       ##
## -> La información será almacenada en las siguientes tablas:                                                          ##
##                       -> covid19original [Contiene la información de la misma manera que se obtiene]                 ##
##                       -> covid19modificado [Se emplean los valores correspondientes de los catálogos descriptivos    ##
##                                             ("ORIGEN", "SECTOR", "SEXO", "TIPO_PACIENTE", "SI_NO", "NACIONALIDAD",   ##
##                                              "RESULTADO", "ENTIDADES", "MUNICIPIOS")]                                ##
##                       -> catorigen [Contiene la información del catálogo "ORIGEN"]                                   ##
##                       -> catsector [Contiene la información del catálogo "SECTOR"]                                   ##
##                       -> catsexo [Contiene la información del catálogo "SEXO"]                                       ##
##                       -> cattipopaciente [Contiene la información del catálogo "TIPO_PACIENTE"]                      ##
##                       -> catsino [Contiene la información del catálogo "SI_NO"]                                      ##
##                       -> catnacionalidad [Contiene la información del catálogo "NACIONALIDAD"]                       ##
##                       -> catresultado [Contiene la información del catálogo "RESULTADO"]                             ##
##                       -> catentidades [Contiene la información del catálogo "ENTIDADES"]                             ##
##                       -> catmunicipios [Contiene la información del catálogo "MUNICIPIOS"]                           ##
##                                                                                                                      ##
## -> Versión 1.0.0                                                                                                     ##
## -> Fecha creación: 14/04/2020                                                                                        ##
## -> Última modificación: 14/04/2020                                                                                   ##
## -> Autor: M. en C. Enrique Alfonso Carmona García                                                                    ##
## -> Contacto: eacarmona860920@gmail.com                                                                               ##
##                                                                                                                      ##
## -> La información relacionada a la librería pandas puede ser consultada en:                                          ##
##                       http://pandas.pydata.org/pandas-docs/stable/index.html                                         ##
## -> La información relacionada a la librería numpy (necesaria para pandas) puede ser consultada en:                   ##
##                       https://docs.scipy.org/doc/                                                                    ##
## -> La información relacionada a mysql.conector puede ser consultada en:                                              ##
##                       https://dev.mysql.com/doc/connector-python/en/                                                 ##
##                       "Se requiere  "pip install mysql-connector-python"                                             ##
## -> La información relacionada a la versión de Python puede ser consultada en:                                        ##
##                       https://www.python.org/                                                                        ##
## -> La información relacionada a COVID-19 en Méxco puede ser consultada en:                                           ##
##                       https://datos.gob.mx/busca/dataset/informacion-referente-a-casos-covid-19-en-mexico            ##
##                       https://www.gob.mx/salud/documentos/datos-abiertos-152127                                      ##
##########################################################################################################################
 
##########################################################################################################################
## -> Cargando las librerías necesarias...                                                                              ##
########################################################################################################################## 

import pandas as panda
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

##########################################################################################################################
## -> Estableciendo las variables de configuración para el acceso al SGBD...                                            ##
## -> Estableciendo la esctructura de las tablas...                                                                     ##
##########################################################################################################################

nombreBDCovid = 'covid19mexico'  
config = {
  'user': 'kike',
  'password': 'kike123',
  'host': '127.0.0.1',
  'database': 'covid19mexico',
  'raise_on_warnings': True,
}

##########################################################################################################################
## -> Estableciendo la esctructura de las tablas...                                                                     ##
## -> La tabla covid19original tiene los siguientes campos:                                                             ##
##                          IDCOVID: Valor de identificación del registro en la tabla.                                  ##
##                          FECHAACTUALIZACION: Permite identificar la fecha de la última actualización.                ##
##                          ORIGEN: La vigilancia sentinela se realiza a través del sistema de unidades de salud        ##
##                                 monitoras de enfermedades respiratorias (USMER). Ver información de catálogo         ## 
##                                 "ORIGEN".                                                                            ##
##                          SECTOR: Identifica el tipo de institución del Sistema Nacional de Salud que brindó la       ##
##                                 atención. Ver información de catálogo "SECTOR".                                      ##
##                          ENTIDADUM: Identifica la entidad donde se ubica la unidad médica que brindó la atención.    ##
##                                    Ver información de catálogo "ENTIDADES".                                          ##
##                          SEXO: Identifica el sexo del paciente. Ver información de catálogo "SEXO".                  ##
##                          ENTIDADNAC: Identifica la entidad de nacimiento del paciente. Ver información de catálogo   ##
##                                     "ENTIDADES".                                                                     ## 
##                          ENTIDADRES: Identifica la entidad de residencia del paciente. Ver información de catálogo   ##
##                                     "ENTIDADES".                                                                     ##
##                          MUNICIPIORES: Identifica el municipio de residencia del paciente. Ver información de        ## 
##                                       catálogo "MUNICIPIOS".                                                         ##
##                          TIPOPACIENTE: Identifica el tipo de atención que recibió el paciente en la unidad. Ver      ##
##                                       información de catálogo "TIPO_PACIENTE".                                       ##
##                          FECHAINGRESO: Identifica la fecha de ingreso del paciente a la unidad de atención.          ##
##                          FECHASINTOMAS: Identifica la fecha en que inició la sintomatología del paciente.            ##
##                          FECHADEF: Identifica la fecha en que el paciente falleció.                                  ##
##                          INTUBADO: Identifica si el paciente requirió de intubación. Ver información de catálogo     ##
##                                   "SI_NO".                                                                           ##
##                          NEUMONIA: Identifica si el paciente se diagnosticó con neumonía. Ver información de         ##
##                                   catálogo "SI_NO".                                                                  ##
##                          EDAD: Identifica la edad del paciente en años.                                              ##
##                          NACIONALIDAD: Identifica si el paciente es mexicano o extranjero. Ver información de        ##
##                                       catálogo "NACIONALIDAD".                                                       ## 
##                          EMBARAZO: Identifica si la paciente está embarazada. Ver información de catálogo "SI_NO"    ##
##                          HABLALENGUAINDI: Identifica si el paciente habla lengua indígena. Ver información de        ##
##                                          catálogo "SI_NO".                                                           ##
##                          DIABETES: Identifica si el paciente tiene un diagnóstico de diabetes. Ver información de    ##
##                                   catálogo "SI_NO".                                                                  ##
##                          EPOC: Identifica si el paciente tiene un diagnóstico de EPOC. Ver información de catálogo   ##
##                               "SI_NO".                                                                               ##     
##                          ASMA: Identifica si el paciente tiene un diagnóstico de asma. Ver información de catálogo   ##
##                               "SI_NO".                                                                               ##
##                          INMUSUPR: Identifica si el paciente presenta inmunosupresión. Ver información de catálogo   ##
##                                   "SI_NO".                                                                           ##
##                          HIPERTENSION: Identifica si el paciente tiene un diagnóstico de hipertensión. Ver           ##
##                                       información de catálogo "SI_NO".                                               ##
##                          OTRACON: Identifica si el paciente tiene diagnóstico de otras enfermedades. Ver             ##
##                                  información de catálogo "SI_NO".                                                    ##
##                          CARDIOVASCULAR: Identifica si el paciente tiene un diagnóstico de enfermedades              ##
##                                         cardiovasculares. Ver información de catálogo "SI_NO".                       ##              
##                          OBESIDAD: Identifica si el paciente tiene diagnóstico de obesidad. Ver información de       ##
##                                   catálogo "SI_NO".                                                                  ##
##                          RENALCRONICA: Identifica si el paciente tiene diagnóstico de insuficiencia renal crónica.   ##
##                                       Ver información de catálogo "SI_NO".                                           ##
##                          TABAQUISMO: Identifica si el paciente tiene hábito de tabaquismo. Ver información de        ##
##                                     catálogo "SI_NO".                                                                ##
##                          OTROCASO: Identifica si el paciente tuvo contacto con algún otro caso diagnosticado con     ##
##                                   SARS CoV-2. Ver información de catálogo "SI_NO".                                   ##
##                          RESULTADO: Identifica el resultado del análisis de la muestra reportado por el laboratorio  ##
##                                    de la Red Nacional de Laboratorios de Vigilancia Epidemiológica {INDRE, LESP,     ##
##                                    LAVE}. Ver información de catálogo "RESULTADO".                                   ##                     
##                          MIGRANTE: Identifica si el paciente es una persona migrante. Ver información de catálogo    ##
##                                   "SI_NO".                                                                           ##
##                          PAISNACIONALIDAD: Identifica la nacionalidad del paciente. [99 = Se ignora]                 ##
##                          PAISORIGEN: Identifica el país del que partió el paciente rumbo a México- [97 = No aplica]  ##
##                          UCI: Identifica si el paciente requirió ingresar a una Unidad de Cuidados Intensivos. Ver   ##
##                              información de catálogo "SI_NO".                                                        ##
##########################################################################################################################

tablaCovid19Original = {}
tablaCovid19Original[nombreBDCovid] = (
    "CREATE TABLE `covid19original` ("
    "   `IDCOVID` INT NOT NULL AUTO_INCREMENT,"
    "   `FECHAACTUALIZACION` TEXT NULL,"
    "   `ORIGEN` TEXT NULL,"
    "   `SECTOR` TEXT NULL,"
    "   `ENTIDADUM` TEXT NULL,"
    "   `SEXO` TEXT NULL,"
    "   `ENTIDADNAC` TEXT NULL,"
    "   `ENTIDADRES` TEXT NULL,"
    "   `MUNICIPIORES` TEXT NULL,"
    "   `TIPOPACIENTE` TEXT NULL,"
    "   `FECHAINGRESO` TEXT NULL,"
    "   `FECHASINTOMAS` TEXT NULL,"
    "   `FECHADEF` TEXT NULL,"
    "   `INTUBADO` TEXT NULL,"
    "   `NEUMONIA` TEXT NULL,"
    "   `EDAD` TEXT NULL,"
    "   `NACIONALIDAD` TEXT NULL,"
    "   `EMBARAZO` TEXT NULL,"
    "   `HABLALENGUAINDI` TEXT NULL,"
    "   `DIABETES` TEXT NULL,"
    "   `EPOC` TEXT NULL,"
    "   `ASMA` TEXT NULL,"
    "   `INMUSUPR` TEXT NULL,"
    "   `HIPERTENSION` TEXT NULL,"
    "   `OTRACON` TEXT NULL,"
    "   `CARDIOVASCULAR` TEXT NULL,"
    "   `OBESIDAD` TEXT NULL,"
    "   `RENALCRONICA` TEXT NULL,"
    "   `TABAQUISMO` TEXT NULL,"
    "   `OTROCASO` TEXT NULL,"
    "   `RESULTADO` TEXT NULL,"
    "   `MIGRANTE` TEXT NULL,"
    "   `PAISNACIONALIDAD` TEXT NULL,"
    "   `PAISORIGEN` TEXT NULL,"
    "   `UCI` TEXT NULL,"
    "   PRIMARY KEY (`IDCOVID`));"
    "   ENGINE = InnoDB"
)

##########################################################################################################################
## -> La tabla covid19modificado tiene los siguientes campos:                                                           ##
##                          IDCOVID: Valor de identificación del registro en la tabla.                                  ##
##                          FECHAACTUALIZACION: Permite identificar la fecha de la última actualización.                ##
##                          ORIGEN: La vigilancia sentinela se realiza a través del sistema de unidades de salud        ##
##                                 monitoras de enfermedades respiratorias (USMER). Información de catálogo  "ORIGEN".  ##
##                          SECTOR: Identifica el tipo de institución del Sistema Nacional de Salud que brindó la       ##
##                                 atención. Información de catálogo "SECTOR".                                          ##
##                          ENTIDADUM: Identifica la entidad donde se ubica la unidad médica que brindó la atención.    ##
##                                    Información de catálogo "ENTIDADES".                                              ##
##                          SEXO: Identifica el sexo del paciente. Información de catálogo "SEXO".                      ##
##                          ENTIDADNAC: Identifica la entidad de nacimiento del paciente. Información de catálogo       ##
##                                     "ENTIDADES".                                                                     ## 
##                          ENTIDADRES: Identifica la entidad de residencia del paciente. Información de catálogo       ##
##                                     "ENTIDADES".                                                                     ##
##                          MUNICIPIORES: Identifica el municipio de residencia del paciente. Información de catálogo   ##
##                                       "MUNICIPIOS".                                                                  ##
##                          TIPOPACIENTE: Identifica el tipo de atención que recibió el paciente en la unidad.          ##
##                                       Información de catálogo "TIPO_PACIENTE".                                       ##
##                          FECHAINGRESO: Identifica la fecha de ingreso del paciente a la unidad de atención.          ##
##                          FECHASINTOMAS: Identifica la fecha en que inició la sintomatología del paciente.            ##
##                          FECHADEF: Identifica la fecha en que el paciente falleció.                                  ##
##                          INTUBADO: Identifica si el paciente requirió de intubación. Información de catálogo         ##
##                                   "SI_NO".                                                                           ##
##                          NEUMONIA: Identifica si el paciente se diagnosticó con neumonía. Información de catálogo    ##
##                                   "SI_NO".                                                                           ##
##                          EDAD: Identifica la edad del paciente en años.                                              ##
##                          NACIONALIDAD: Identifica si el paciente es mexicano o extranjero. Información de catálogo   ##
##                                       "NACIONALIDAD".                                                                ## 
##                          EMBARAZO: Identifica si la paciente está embarazada. Información de catálogo "SI_NO"        ##
##                          HABLALENGUAINDI: Identifica si el paciente habla lengua indígena. Información de catálogo   ##
##                                          "SI_NO".                                                                    ##
##                          DIABETES: Identifica si el paciente tiene un diagnóstico de diabetes. Información de        ##
##                                   catálogo "SI_NO".                                                                  ##
##                          EPOC: Identifica si el paciente tiene un diagnóstico de EPOC. Información de catálogo       ##
##                               "SI_NO".                                                                               ##     
##                          ASMA: Identifica si el paciente tiene un diagnóstico de asma. Información de catálogo       ##
##                               "SI_NO".                                                                               ##
##                          INMUSUPR: Identifica si el paciente presenta inmunosupresión. Información de catálogo       ##
##                                   "SI_NO".                                                                           ##
##                          HIPERTENSION: Identifica si el paciente tiene un diagnóstico de hipertensión. Información   ##
##                                       de catálogo "SI_NO".                                                           ##
##                          OTRACON: Identifica si el paciente tiene diagnóstico de otras enfermedades. Información de  ##
##                                  catálogo "SI_NO".                                                                   ##
##                          CARDIOVASCULAR: Identifica si el paciente tiene un diagnóstico de enfermedades              ##
##                                         cardiovasculares. Información de catálogo "SI_NO".                           ##              
##                          OBESIDAD: Identifica si el paciente tiene diagnóstico de obesidad. Información de           ##
##                                   catálogo "SI_NO".                                                                  ##
##                          RENALCRONICA: Identifica si el paciente tiene diagnóstico de insuficiencia renal crónica.   ##
##                                       Información de catálogo "SI_NO".                                               ##
##                          TABAQUISMO: Identifica si el paciente tiene hábito de tabaquismo. Información de catálogo   ##
##                                     "SI_NO".                                                                         ##
##                          OTROCASO: Identifica si el paciente tuvo contacto con algún otro caso diagnosticado con     ##
##                                   SARS CoV-2. Información de catálogo "SI_NO".                                       ##
##                          RESULTADO: Identifica el resultado del análisis de la muestra reportado por el laboratorio  ##
##                                    de la Red Nacional de Laboratorios de Vigilancia Epidemiológica {INDRE, LESP,     ##
##                                    LAVE}. Información de catálogo "RESULTADO".                                       ##                     
##                          MIGRANTE: Identifica si el paciente es una persona migrante. Información de catálogo        ##
##                                   "SI_NO".                                                                           ##
##                          PAISNACIONALIDAD: Identifica la nacionalidad del paciente. [99 = Se ignora]                 ##
##                          PAISORIGEN: Identifica el país del que partió el paciente rumbo a México- [97 = No aplica]  ##
##                          UCI: Identifica si el paciente requirió ingresar a una Unidad de Cuidados Intensivos.       ##
##                              Información de catálogo "SI_NO".                                                        ##
##########################################################################################################################

tablaCovid19Modificado = {}
tablaCovid19Modificado[nombreBDCovid] = (
    "CREATE TABLE `covid19modificado` ("
    "   `IDCOVID` INT NOT NULL AUTO_INCREMENT,"
    "   `FECHAACTUALIZACION` TEXT NULL,"
    "   `ORIGEN` TEXT NULL,"
    "   `SECTOR` TEXT NULL,"
    "   `ENTIDADUM` TEXT NULL,"
    "   `SEXO` TEXT NULL,"
    "   `ENTIDADNAC` TEXT NULL,"
    "   `ENTIDADRES` TEXT NULL,"
    "   `MUNICIPIORES` TEXT NULL,"
    "   `TIPOPACIENTE` TEXT NULL,"
    "   `FECHAINGRESO` TEXT NULL,"
    "   `FECHASINTOMAS` TEXT NULL,"
    "   `FECHADEF` TEXT NULL,"
    "   `INTUBADO` TEXT NULL,"
    "   `NEUMONIA` TEXT NULL,"
    "   `EDAD` TEXT NULL,"
    "   `NACIONALIDAD` TEXT NULL,"
    "   `EMBARAZO` TEXT NULL,"
    "   `HABLALENGUAINDI` TEXT NULL,"
    "   `DIABETES` TEXT NULL,"
    "   `EPOC` TEXT NULL,"
    "   `ASMA` TEXT NULL,"
    "   `INMUSUPR` TEXT NULL,"
    "   `HIPERTENSION` TEXT NULL,"
    "   `OTRACON` TEXT NULL,"
    "   `CARDIOVASCULAR` TEXT NULL,"
    "   `OBESIDAD` TEXT NULL,"
    "   `RENALCRONICA` TEXT NULL,"
    "   `TABAQUISMO` TEXT NULL,"
    "   `OTROCASO` TEXT NULL,"
    "   `RESULTADO` TEXT NULL,"
    "   `MIGRANTE` TEXT NULL,"
    "   `PAISNACIONALIDAD` TEXT NULL,"
    "   `PAISORIGEN` TEXT NULL,"
    "   `UCI` TEXT NULL,"
    "   PRIMARY KEY (`IDCOVID`));"
    "   ENGINE = InnoDB"
)

##########################################################################################################################
## -> La tabla catorigen tiene los siguientes campos:                                                                   ##
##                          IDCAT: Valor de identificación del registro en la tabla.                                    ##
##                          CLAVE: Valor numérico identificativo de la clave.                                           ##
##                          DESCRIPCION: Descripción del valor CLAVE correspondiente.                                   ##
##########################################################################################################################

tablaCatOrigen = {}
tablaCatOrigen[nombreBDCovid] = (
    "CREATE TABLE `catorigen` ("
    "   `IDCAT` INT NOT NULL AUTO_INCREMENT,"
    "   `CLAVE` TEXT NULL,"
    "   `DESCRIPCION` TEXT NULL,"
    "   PRIMARY KEY (`IDCAT`));"
    "   ENGINE = InnoDB"
)

##########################################################################################################################
## -> La tabla catsector tiene los siguientes campos:                                                                   ##
##                          IDCAT: Valor de identificación del registro en la tabla.                                    ##
##                          CLAVE: Valor numérico identificativo de la clave.                                           ##
##                          DESCRIPCION: Descripción del valor CLAVE correspondiente.                                   ##
##########################################################################################################################

tablaCatSector = {}
tablaCatSector[nombreBDCovid] = (
    "CREATE TABLE `catsector` ("
    "   `IDCAT` INT NOT NULL AUTO_INCREMENT,"
    "   `CLAVE` TEXT NULL,"
    "   `SECTOR` TEXT NULL,"
    "   PRIMARY KEY (`IDCAT`));"
    "   ENGINE = InnoDB"
)

##########################################################################################################################
## -> La tabla catsexo tiene los siguientes campos:                                                                     ##
##                          IDCAT: Valor de identificación del registro en la tabla.                                    ##
##                          CLAVE: Valor numérico identificativo de la clave.                                           ##
##                          DESCRIPCION: Descripción del valor CLAVE correspondiente.                                   ##
##########################################################################################################################

tablaCatSexo = {}
tablaCatSexo[nombreBDCovid] = (
    "CREATE TABLE `catsexo` ("
    "   `IDCAT` INT NOT NULL AUTO_INCREMENT,"
    "   `CLAVE` TEXT NULL,"
    "   `DESCRIPCION` TEXT NULL,"
    "   PRIMARY KEY (`IDCAT`));"
    "   ENGINE = InnoDB"
)

##########################################################################################################################
## -> La tabla cattipopaciente tiene los siguientes campos:                                                             ##
##                          IDCAT: Valor de identificación del registro en la tabla.                                    ##
##                          CLAVE: Valor numérico identificativo de la clave.                                           ##
##                          DESCRIPCION: Descripción del valor CLAVE correspondiente.                                   ##
##########################################################################################################################

tablaCatTipoPaciente = {}
tablaCatTipoPaciente[nombreBDCovid] = (
    "CREATE TABLE `cattipopaciente` ("
    "   `IDCAT` INT NOT NULL AUTO_INCREMENT,"
    "   `CLAVE` TEXT NULL,"
    "   `DESCRIPCION` TEXT NULL,"
    "   PRIMARY KEY (`IDCAT`));"
    "   ENGINE = InnoDB"
)

##########################################################################################################################
## -> La tabla catsino tiene los siguientes campos:                                                                     ##
##                          IDCAT: Valor de identificación del registro en la tabla.                                    ##
##                          CLAVE: Valor numérico identificativo de la clave.                                           ##
##                          DESCRIPCION: Descripción del valor CLAVE correspondiente.                                   ##
##########################################################################################################################

tablaCatSiNo = {}
tablaCatSiNo[nombreBDCovid] = (
    "CREATE TABLE `catsino` ("
    "   `IDCAT` INT NOT NULL AUTO_INCREMENT,"
    "   `CLAVE` TEXT NULL,"
    "   `DESCRIPCION` TEXT NULL,"
    "   PRIMARY KEY (`IDCAT`));"
    "   ENGINE = InnoDB"
)

##########################################################################################################################
## -> La tabla catnacionalidad tiene los siguientes campos:                                                             ##
##                          IDCAT: Valor de identificación del registro en la tabla.                                    ##
##                          CLAVE: Valor numérico identificativo de la clave.                                           ##
##                          DESCRIPCION: Descripción del valor CLAVE correspondiente.                                   ##
##########################################################################################################################

tablaCatNacionalidad = {}
tablaCatNacionalidad[nombreBDCovid] = (
    "CREATE TABLE `catnacionalidad` ("
    "   `IDCAT` INT NOT NULL AUTO_INCREMENT,"
    "   `CLAVE` TEXT NULL,"
    "   `DESCRIPCION` TEXT NULL,"
    "   PRIMARY KEY (`IDCAT`));"
    "   ENGINE = InnoDB"
)

##########################################################################################################################
## -> La tabla catresultado tiene los siguientes campos:                                                                ##
##                          IDCAT: Valor de identificación del registro en la tabla.                                    ##
##                          CLAVE: Valor numérico identificativo de la clave.                                           ##
##                          DESCRIPCION: Descripción del valor CLAVE correspondiente.                                   ##
##########################################################################################################################

tablaCatResultado = {}
tablaCatResultado[nombreBDCovid] = (
    "CREATE TABLE `catresultado` ("
    "   `IDCAT` INT NOT NULL AUTO_INCREMENT,"
    "   `CLAVE` TEXT NULL,"
    "   `DESCRIPCION` TEXT NULL,"
    "   PRIMARY KEY (`IDCAT`));"
    "   ENGINE = InnoDB"
)

##########################################################################################################################
## -> La tabla catentidades tiene los siguientes campos:                                                                ##
##                          IDCAT: Valor de identificación del registro en la tabla.                                    ##
##                          CLAVEENTIDAD: Valor numérico identificativo de la clave.                                    ##
##                          ENTIDADFEDERATIVA: Nombre de la entidad asociada a la clave.                                ##
##                          ABREVIATURA: Abreviatura del nombre de la entidad.                                          ##
##########################################################################################################################

tablaCatEntidades = {}
tablaCatEntidades[nombreBDCovid] = (
    "CREATE TABLE `catentidades` ("
    "   `IDCAT` INT NOT NULL AUTO_INCREMENT,"
    "   `CLAVEENTIDAD` TEXT NULL,"
    "   `ENTIDADFEDERATIVA` TEXT NULL,"
    "   `ABREVIATURA` TEXT NULL,"
    "   PRIMARY KEY (`IDCAT`));"
    "   ENGINE = InnoDB"
)

##########################################################################################################################
## -> La tabla catmunicipios tiene los siguientes campos:                                                               ##
##                          IDCAT: Valor de identificación del registro en la tabla.                                    ##
##                          CLAVEMUNICIPIO: Valor numérico identificativo de la clave.                                  ##
##                          MUNICIPIO: Nombre del municipio asociado a la clave.                                        ##
##                          CLAVEENTIDAD: Clave de la entidad a la que pertenece el municipio.                          ##
##########################################################################################################################

tablaCatMunicipios = {}
tablaCatMunicipios[nombreBDCovid] = (
    "CREATE TABLE `catmunicipios` ("
    "   `IDCAT` INT NOT NULL AUTO_INCREMENT,"
    "   `CLAVEMUNICIPIO` TEXT NULL,"
    "   `MUNICIPIO` TEXT NULL,"
    "   `CLAVEENTIDAD` TEXT NULL,"
    "   PRIMARY KEY (`IDCAT`));"
    "   ENGINE = InnoDB"
)

##########################################################################################################################
## -> Creando una clase para convertir los tipos de datos a tipos MySQL (Mendiante la librería numpy)...                ##
##########################################################################################################################

class NumpyMySQLConverter(mysql.connector.conversion.MySQLConverter):
    
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

##########################################################################################################################
## -> Conectando al SGBD MySQL mediante la configuración definida...                                                    ##
##########################################################################################################################

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
'''
##########################################################################################################################
## -> Función para crear las bases de datos en el formato correspondiente...                                            ##
##########################################################################################################################

def create_database(cursor): 
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(nombreBDCovid))
    except mysql.connector.Error as err:
        print ("   ")
        print("Error al crear la base de datos señalada: {}".format(err))
        exit(1)

##########################################################################################################################
## -> Se solicita crear las base de datos...                                                                            ##
##########################################################################################################################

try:  
    cnx.database = nombreBDCovid  
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = nombreBDCovid
    else:
        print ("   ")
        print(err)
        exit(1) 

##########################################################################################################################
## -> Se solicita crear todas las tablas definidas ["covid19original", "covid19modificado", "catorigen", "catsector",   ##
##                                                  "catsexo", "cattipopaciente", "catsino", "catnacionalidad",         ##
##                                                  "catresultado", "catentidades", "catmunicipios"]                    ##
##########################################################################################################################

def CrearTablasEnSGBD(tablaACrear):
    for name, ddl in tablaACrear.items():
        try:
            print ("Creando la tabla {}: ".format(name), end = '')
            cursor.execute(ddl)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print ("Ya existe la tabla especificada.")
            else:
                print (err.msg)
        else:
            print ("La tabla fue creada.")

##########################################################################################################################
## -> Se le solicita al usuario la confirmación para la creación de la tabla covid19original...                         ##
##########################################################################################################################

crearTabla = input ("¿Desea crear la tabla Covid19Original? [S/N]: ")
try:
    if crearTabla == "S":
        print ("Se procede a crear la tabla Covid19Original.")
        CrearTablasEnSGBD(tablaCovid19Original)
    if crearTabla == "N":
        print ("La tabla Covid19Original no será creada.")
    if crearTabla != "S" and crearTabla != "N":
        print ("La entrada proporcionada no fue válida. No se realizará ninguna acción.")
except ValueError:
    print ("Opss, un error inesperado ah ocurrido. No se realizará ninguna acción.")

##########################################################################################################################
## -> Se le solicita al usuario la confirmación para la creación de la tabla covid19modificado...                       ##
##########################################################################################################################

crearTabla = input ("¿Desea crear la tabla Covid19Modificado? [S/N]: ")
try:
    if crearTabla == "S":
        print ("Se procede a crear la tabla Covid19Modificado.")
        CrearTablasEnSGBD(tablaCovid19Modificado)
    if crearTabla == "N":
        print ("La tabla Covid19Modificado no será creada.")
    if crearTabla != "S" and crearTabla != "N":
        print ("La entrada proporcionada no fue válida. No se realizará ninguna acción.")
except ValueError:
    print ("Opss, un error inesperado ah ocurrido. No se realizará ninguna acción.")

##########################################################################################################################
## -> Se le solicita al usuario la confirmación para la creación de la tabla catOrigen...                               ##
##########################################################################################################################

crearTabla = input ("¿Desea crear la tabla CatOrigen? [S/N]: ")
try:
    if crearTabla == "S":
        print ("Se procede a crear la tabla CatOrigen.")
        CrearTablasEnSGBD(tablaCatOrigen)
    if crearTabla == "N":
        print ("La tabla CatOrigen no será creada.")
    if crearTabla != "S" and crearTabla != "N":
        print ("La entrada proporcionada no fue válida. No se realizará ninguna acción.")
except ValueError:
    print ("Opss, un error inesperado ah ocurrido. No se realizará ninguna acción.")

##########################################################################################################################
## -> Se le solicita al usuario la confirmación para la creación de la tabla catSector...                               ##
##########################################################################################################################

crearTabla = input ("¿Desea crear la tabla CatSector? [S/N]: ")
try:
    if crearTabla == "S":
        print ("Se procede a crear la tabla CatSector.")
        CrearTablasEnSGBD(tablaCatSector)
    if crearTabla == "N":
        print ("La tabla CatSector no será creada.")
    if crearTabla != "S" and crearTabla != "N":
        print ("La entrada proporcionada no fue válida. No se realizará ninguna acción.")
except ValueError:
    print ("Opss, un error inesperado ah ocurrido. No se realizará ninguna acción.")

##########################################################################################################################
## -> Se le solicita al usuario la confirmación para la creación de la tabla catSexo...                                 ##
##########################################################################################################################

crearTabla = input ("¿Desea crear la tabla CatSexo? [S/N]: ")
try:
    if crearTabla == "S":
        print ("Se procede a crear la tabla CatSexo.")
        CrearTablasEnSGBD(tablaCatSexo)
    if crearTabla == "N":
        print ("La tabla CatSexo no será creada.")
    if crearTabla != "S" and crearTabla != "N":
        print ("La entrada proporcionada no fue válida. No se realizará ninguna acción.")
except ValueError:
    print ("Opss, un error inesperado ah ocurrido. No se realizará ninguna acción.")

##########################################################################################################################
## -> Se le solicita al usuario la confirmación para la creación de la tabla catTipoPaciente...                         ##
##########################################################################################################################

crearTabla = input ("¿Desea crear la tabla CatTipoPaciente? [S/N]: ")
try:
    if crearTabla == "S":
        print ("Se procede a crear la tabla CatTipoPaciente.")
        CrearTablasEnSGBD(tablaCatTipoPaciente)
    if crearTabla == "N":
        print ("La tabla CatTipoPaciente no será creada.")
    if crearTabla != "S" and crearTabla != "N":
        print ("La entrada proporcionada no fue válida. No se realizará ninguna acción.")
except ValueError:
    print ("Opss, un error inesperado ah ocurrido. No se realizará ninguna acción.")

##########################################################################################################################
## -> Se le solicita al usuario la confirmación para la creación de la tabla catSiNo...                                 ##
##########################################################################################################################

crearTabla = input ("¿Desea crear la tabla CatSiNo? [S/N]: ")
try:
    if crearTabla == "S":
        print ("Se procede a crear la tabla CatSiNo.")
        CrearTablasEnSGBD(tablaCatSiNo)
    if crearTabla == "N":
        print ("La tabla CatSiNo no será creada.")
    if crearTabla != "S" and crearTabla != "N":
        print ("La entrada proporcionada no fue válida. No se realizará ninguna acción.")
except ValueError:
    print ("Opss, un error inesperado ah ocurrido. No se realizará ninguna acción.")

##########################################################################################################################
## -> Se le solicita al usuario la confirmación para la creación de la tabla catNacionalidad...                         ##
##########################################################################################################################

crearTabla = input ("¿Desea crear la tabla CatNacionalidad? [S/N]: ")
try:
    if crearTabla == "S":
        print ("Se procede a crear la tabla CatNacionalidad.")
        CrearTablasEnSGBD(tablaCatNacionalidad)
    if crearTabla == "N":
        print ("La tabla CatNacionalidad no será creada.")
    if crearTabla != "S" and crearTabla != "N":
        print ("La entrada proporcionada no fue válida. No se realizará ninguna acción.")
except ValueError:
    print ("Opss, un error inesperado ah ocurrido. No se realizará ninguna acción.")

##########################################################################################################################
## -> Se le solicita al usuario la confirmación para la creación de la tabla catResultado...                            ##
##########################################################################################################################

crearTabla = input ("¿Desea crear la tabla CatResultado? [S/N]: ")
try:
    if crearTabla == "S":
        print ("Se procede a crear la tabla CatResultado.")
        CrearTablasEnSGBD(tablaCatResultado)
    if crearTabla == "N":
        print ("La tabla CatResultado no será creada.")
    if crearTabla != "S" and crearTabla != "N":
        print ("La entrada proporcionada no fue válida. No se realizará ninguna acción.")
except ValueError:
    print ("Opss, un error inesperado ah ocurrido. No se realizará ninguna acción.")

##########################################################################################################################
## -> Se le solicita al usuario la confirmación para la creación de la tabla catEntidades...                            ##
##########################################################################################################################

crearTabla = input ("¿Desea crear la tabla CatEntidades? [S/N]: ")
try:
    if crearTabla == "S":
        print ("Se procede a crear la tabla CatEntidades.")
        CrearTablasEnSGBD(tablaCatEntidades)
    if crearTabla == "N":
        print ("La tabla CatEntidades no será creada.")
    if crearTabla != "S" and crearTabla != "N":
        print ("La entrada proporcionada no fue válida. No se realizará ninguna acción.")
except ValueError:
    print ("Opss, un error inesperado ah ocurrido. No se realizará ninguna acción.")

##########################################################################################################################
## -> Se le solicita al usuario la confirmación para la creación de la tabla catMunicipios...                           ##
##########################################################################################################################

crearTabla = input ("¿Desea crear la tabla CatMunicipios? [S/N]: ")
try:
    if crearTabla == "S":
        print ("Se procede a crear la tabla CatMunicipios.")
        CrearTablasEnSGBD(tablaCatMunicipios)
    if crearTabla == "N":
        print ("La tabla CatMunicipios no será creada.")
    if crearTabla != "S" and crearTabla != "N":
        print ("La entrada proporcionada no fue válida. No se realizará ninguna acción.")
except ValueError:
    print ("Opss, un error inesperado ah ocurrido. No se realizará ninguna acción.")

##########################################################################################################################
## -> Cargando el fichero con la información de los catálogos para ser almacenada...                                    ##  
## -> Se carga cada Hoja por separado ya que cada Hoja es un catálogo...                                                ##
## -> En el caso que existan campos vacios se les adiciona el valor "NULL"                                              ##
##########################################################################################################################

direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/DatosCovid/diccionario/Catalogos.xlsx"

catalogoOrigen = panda.read_excel(direccionFichero, sheet_name="ORIGEN")
print ("Cargando fichero de catálogo ORIGEN, puede tardar un momento, por favor espere...")
if catalogoOrigen.empty:
    print ("Fichero se encuentra vacío, por favor verifique que sea el correcto...")
else:
    print ("Fichero cargado exitosamente...")
catalogoOrigen = catalogoOrigen.fillna("NULL")

catalogoSector = panda.read_excel(direccionFichero, sheet_name="SECTOR")
print ("Cargando fichero de catálogo SECTOR, puede tardar un momento, por favor espere...")
if catalogoSector.empty:
    print ("Fichero se encuentra vacío, por favor verifique que sea el correcto...")
else:
    print ("Fichero cargado exitosamente...")
catalogoSector = catalogoSector.fillna("NULL")

catalogoSexo = panda.read_excel(direccionFichero, sheet_name="SEXO")
print ("Cargando fichero de catálogo SEXO, puede tardar un momento, por favor espere...")
if catalogoSexo.empty:
    print ("Fichero se encuentra vacío, por favor verifique que sea el correcto...")
else:
    print ("Fichero cargado exitosamente...")
catalogoSexo = catalogoSexo.fillna("NULL")

catalogoTipoPaciente = panda.read_excel(direccionFichero, sheet_name="TIPOPACIENTE")
print ("Cargando fichero de catálogo TIPOPACIENTE, puede tardar un momento, por favor espere...")
if catalogoTipoPaciente.empty:
    print ("Fichero se encuentra vacío, por favor verifique que sea el correcto...")
else:
    print ("Fichero cargado exitosamente...")
catalogoTipoPaciente = catalogoTipoPaciente.fillna("NULL")

catalogoSiNo = panda.read_excel(direccionFichero, sheet_name="SINO")
print ("Cargando fichero de catálogo SI_NO, puede tardar un momento, por favor espere...")
if catalogoSiNo.empty:
    print ("Fichero se encuentra vacío, por favor verifique que sea el correcto...")
else:
    print ("Fichero cargado exitosamente...")
catalogoSiNo = catalogoSiNo.fillna("NULL")

catalogoNacionalidad = panda.read_excel(direccionFichero, sheet_name="NACIONALIDAD")
print ("Cargando fichero de catálogo NACIONALIDAD, puede tardar un momento, por favor espere...")
if catalogoNacionalidad.empty:
    print ("Fichero se encuentra vacío, por favor verifique que sea el correcto...")
else:
    print ("Fichero cargado exitosamente...")
catalogoNacionalidad = catalogoNacionalidad.fillna("NULL")

catalogoResultado = panda.read_excel(direccionFichero, sheet_name="RESULTADO")
print ("Cargando fichero de catálogo RESULTADO, puede tardar un momento, por favor espere...")
if catalogoResultado.empty:
    print ("Fichero se encuentra vacío, por favor verifique que sea el correcto...")
else:
    print ("Fichero cargado exitosamente...")
catalogoResultado = catalogoResultado.fillna("NULL")

catalogoEntidades = panda.read_excel(direccionFichero, sheet_name="ENTIDADES")
print ("Cargando fichero de catálogo ENTIDADES, puede tardar un momento, por favor espere...")
if catalogoEntidades.empty:
    print ("Fichero se encuentra vacío, por favor verifique que sea el correcto...")
else:
    print ("Fichero cargado exitosamente...")
catalogoEntidades = catalogoEntidades.fillna("NULL")

catalogoMunicipios = panda.read_excel(direccionFichero, sheet_name="MUNICIPIOS")
print ("Cargando fichero de catálogo MUNICIPIOS, puede tardar un momento, por favor espere...")
if catalogoMunicipios.empty:
    print ("Fichero se encuentra vacío, por favor verifique que sea el correcto...")
else:
    print ("Fichero cargado exitosamente...")
catalogoMunicipios = catalogoMunicipios.fillna("NULL")

##########################################################################################################################
## -> Preparando las consultas SQL y las variables necesarias para almacenar los datos en el SGBD...                    ##
## -> Las variables corresponden a sus respectivos campos en la base de datos...                                        ##
##               -> datosAAAA [Contiene la información necesaria para hacer la inserción en la base de datos]...        ##
##               -> addAAAAAA [Consulta SQL que inserta la información en la base de datos]...                          ##
## -> Catálogo "ORIGEN"                                                                                                 ##
##########################################################################################################################

claveOrigen = ""
descripcionOrigen = ""

datosOrigen = {
    'datoClave' : claveOrigen,
    'datoDescripcion' : descripcionOrigen,
}

addOrigen = ("INSERT INTO catorigen"
                "(CLAVE, DESCRIPCION)"
                "VALUES (%(datoClave)s, %(datoDescripcion)s)"
            )

##########################################################################################################################
## -> Catálogo "SECTOR"                                                                                                 ##
##########################################################################################################################

claveSector = ""
sector = ""

datosSector = {
    'datoClave' : claveSector,
    'datoSector' : sector,
}

addSector = ("INSERT INTO catsector"
                "(CLAVE, SECTOR)"
                "VALUES (%(datoClave)s, %(datoSector)s)"
            )

##########################################################################################################################
## -> Catálogo "SEXO"                                                                                                   ##
##########################################################################################################################

claveSexo = ""
descripcionSexo = ""

datosSexo = {
    'datoClave' : claveSexo,
    'datoDescripcion' : descripcionSexo,
}

addSexo = ("INSERT INTO catsexo"
                "(CLAVE, DESCRIPCION)"
                "VALUES (%(datoClave)s, %(datoDescripcion)s)"
            )

##########################################################################################################################
## -> Catálogo "TIPOPACIENTE"                                                                                           ##
##########################################################################################################################

claveTipoPaciente = ""
descripcionTipoPaciente = ""

datosTipoPaciente = {
    'datoClave' : claveTipoPaciente,
    'datoDescripcion' : descripcionTipoPaciente,
}

addTipoPaciente = ("INSERT INTO cattipopaciente"
                "(CLAVE, DESCRIPCION)"
                "VALUES (%(datoClave)s, %(datoDescripcion)s)"
            )

##########################################################################################################################
## -> Catálogo "SI_NO"                                                                                                  ##
##########################################################################################################################

claveSiNo = ""
descripcionSiNo = ""

datosSiNo = {
    'datoClave' : claveSiNo,
    'datoDescripcion' : descripcionSiNo,
}

addSiNo = ("INSERT INTO catsino"
                "(CLAVE, DESCRIPCION)"
                "VALUES (%(datoClave)s, %(datoDescripcion)s)"
            )

##########################################################################################################################
## -> Catálogo "NACIONALIDAD"                                                                                           ##
##########################################################################################################################

claveNacionalidad = ""
descripcionNacionalidad = ""

datosNacionalidad = {
    'datoClave' : claveNacionalidad,
    'datoDescripcion' : descripcionNacionalidad,
}

addNacionalidad = ("INSERT INTO catnacionalidad"
                "(CLAVE, DESCRIPCION)"
                "VALUES (%(datoClave)s, %(datoDescripcion)s)"
            )

##########################################################################################################################
## -> Catálogo "RESULTADO"                                                                                              ##
##########################################################################################################################

claveResultado = ""
descripcionResultado = ""

datosResultado = {
    'datoClave' : claveResultado,
    'datoDescripcion' : descripcionResultado,
}

addResultado = ("INSERT INTO catresultado"
                "(CLAVE, DESCRIPCION)"
                "VALUES (%(datoClave)s, %(datoDescripcion)s)"
            )

##########################################################################################################################
## -> Catálogo "ENTIDADES"                                                                                              ##
##########################################################################################################################

claveEntidad = ""
entidadFederativa = ""
abreviaturaEntidadFederativa = ""

datosEntidadFederativa = {
    'datoClave' : claveEntidad,
    'datoEntidadFederativa' : entidadFederativa,
    'datoAbreviaturaEntidadFederativa' : abreviaturaEntidadFederativa,
}

addEntidadFederativa = ("INSERT INTO catentidades"
                "(CLAVEENTIDAD, ENTIDADFEDERATIVA, ABREVIATURA)"
                "VALUES (%(datoClave)s, %(datoEntidadFederativa)s, %(datoAbreviaturaEntidadFederativa)s)"
            )

##########################################################################################################################
## -> Catálogo "MUNICIPIOS"                                                                                             ##
##########################################################################################################################

claveMunicipio = ""
municipio = ""
claveEntidadMunicipio = ""

datosMunicipio = {
    'datoClaveMunicipio' : claveMunicipio,
    'datoMunicipio' : municipio,
    'datoClaveEntidadMunicipio' : claveEntidadMunicipio,
}

addMunicipio = ("INSERT INTO catmunicipios"
                "(CLAVEMUNICIPIO, MUNICIPIO, CLAVEENTIDAD)"
                "VALUES (%(datoClaveMunicipio)s, %(datoMunicipio)s, %(datoClaveEntidadMunicipio)s)"
            )

##########################################################################################################################
##  -> Se leen los datos de cada uno de los catálogos y se ejecuntan las consultas SQL...                               ##
##  -> Catálogo "ORIGEN"...                                                                                             ##
##########################################################################################################################

for i in range(0, len(catalogoOrigen)):
    claveOrigen = int(catalogoOrigen.iloc[i,0])
    descripcionOrigen = catalogoOrigen.iloc[i,1]
    datosOrigen = {
    'datoClave' : claveOrigen,
    'datoDescripcion' : descripcionOrigen,
    }
    print ("Insertando registro " + str(i) + " de " + str(len(catalogoOrigen)))
    cursor.execute(addOrigen, datosOrigen)
    cnx.commit()
    print ("Registro " + str(i) +  " insertado, completado el " + str(int(i)*100/int(len(catalogoOrigen))) +  " porciento del total de datos")

##########################################################################################################################
##  -> Catálogo "SECTOR"...                                                                                             ##
##########################################################################################################################

for i in range(0, len(catalogoSector)):
    claveSector = int(catalogoSector.iloc[i,0])
    sector = catalogoSector.iloc[i,1]
    datosSector = {
    'datoClave' : claveSector,
    'datoSector' : sector,
    }
    print ("Insertando registro " + str(i) + " de " + str(len(catalogoSector)))
    cursor.execute(addSector, datosSector)
    cnx.commit()
    print ("Registro " + str(i) +  " insertado, completado el " + str(int(i)*100/int(len(catalogoSector))) +  " porciento del total de datos")

##########################################################################################################################
##  -> Catálogo "SEXO"...                                                                                               ##
##########################################################################################################################

for i in range(0, len(catalogoSexo)):
    claveSexo = int(catalogoSexo.iloc[i,0])
    descripcionSexo = catalogoSexo.iloc[i,1]
    datosSexo = {
    'datoClave' : claveSexo,
    'datoDescripcion' : descripcionSexo,
    }
    print ("Insertando registro " + str(i) + " de " + str(len(catalogoSexo)))
    cursor.execute(addSexo, datosSexo)
    cnx.commit()
    print ("Registro " + str(i) +  " insertado, completado el " + str(int(i)*100/int(len(catalogoSexo))) +  " porciento del total de datos")

##########################################################################################################################
##  -> Catálogo "TIPOPACIENTE"...                                                                                       ##
##########################################################################################################################

for i in range(0, len(catalogoTipoPaciente)):
    claveTipoPaciente = int(catalogoTipoPaciente.iloc[i,0])
    descripcionTipoPaciente = catalogoTipoPaciente.iloc[i,1]
    datosTipoPaciente = {
    'datoClave' : claveTipoPaciente,
    'datoDescripcion' : descripcionTipoPaciente,
    }
    print ("Insertando registro " + str(i) + " de " + str(len(catalogoTipoPaciente)))
    cursor.execute(addTipoPaciente, datosTipoPaciente)
    cnx.commit()
    print ("Registro " + str(i) +  " insertado, completado el " + str(int(i)*100/int(len(catalogoTipoPaciente))) +  " porciento del total de datos")

##########################################################################################################################
##  -> Catálogo "SI_NO"...                                                                                              ##
##########################################################################################################################

for i in range(0, len(catalogoSiNo)):
    claveSiNo = int(catalogoSiNo.iloc[i,0])
    descripcionSiNo = catalogoSiNo.iloc[i,1]
    datosSiNo = {
    'datoClave' : claveSiNo,
    'datoDescripcion' : descripcionSiNo,
    }
    print ("Insertando registro " + str(i) + " de " + str(len(catalogoSiNo)))
    cursor.execute(addSiNo, datosSiNo)
    cnx.commit()
    print ("Registro " + str(i) +  " insertado, completado el " + str(int(i)*100/int(len(catalogoSiNo))) +  " porciento del total de datos")

##########################################################################################################################
##  -> Catálogo "NACIONALIDAD"...                                                                                       ##
##########################################################################################################################

for i in range(0, len(catalogoNacionalidad)):
    claveNacionalidad = int(catalogoNacionalidad.iloc[i,0])
    descripcionNacionalidad = catalogoNacionalidad.iloc[i,1]
    datosNacionalidad = {
    'datoClave' : claveNacionalidad,
    'datoDescripcion' : descripcionNacionalidad,
    }
    print ("Insertando registro " + str(i) + " de " + str(len(catalogoNacionalidad)))
    cursor.execute(addNacionalidad, datosNacionalidad)
    cnx.commit()
    print ("Registro " + str(i) +  " insertado, completado el " + str(int(i)*100/int(len(catalogoNacionalidad))) +  " porciento del total de datos")

##########################################################################################################################
##  -> Catálogo "RESULTADO"...                                                                                          ##
##########################################################################################################################

for i in range(0, len(catalogoResultado)):
    claveResultado = int(catalogoResultado.iloc[i,0])
    descripcionResultado = catalogoResultado.iloc[i,1]
    datosResultado = {
    'datoClave' : claveResultado,
    'datoDescripcion' : descripcionResultado,
    }
    print ("Insertando registro " + str(i) + " de " + str(len(catalogoResultado)))
    cursor.execute(addResultado, datosResultado)
    cnx.commit()
    print ("Registro " + str(i) +  " insertado, completado el " + str(int(i)*100/int(len(catalogoResultado))) +  " porciento del total de datos")

##########################################################################################################################
##  -> Catálogo "ENTIDADES"...                                                                                          ##
##########################################################################################################################

for i in range(0, len(catalogoEntidades)):
    claveEntidad = int(catalogoEntidades.iloc[i,0])
    entidadFederativa = catalogoEntidades.iloc[i,1]
    abreviaturaEntidadFederativa = catalogoEntidades.iloc[i,2]
    datosEntidadFederativa = {
    'datoClave' : claveEntidad,
    'datoEntidadFederativa' : entidadFederativa,
    'datoAbreviaturaEntidadFederativa': abreviaturaEntidadFederativa,
    }
    print ("Insertando registro " + str(i) + " de " + str(len(catalogoEntidades)))
    cursor.execute(addEntidadFederativa, datosEntidadFederativa)
    cnx.commit()
    print ("Registro " + str(i) +  " insertado, completado el " + str(int(i)*100/int(len(catalogoEntidades))) +  " porciento del total de datos")

##########################################################################################################################
##  -> Catálogo "MUNICIPIOS"...                                                                                         ##
##########################################################################################################################

for i in range(0, len(catalogoMunicipios)):
    claveMunicipio = int(catalogoMunicipios.iloc[i,0])
    municipio = catalogoMunicipios.iloc[i,1]
    claveEntidadMunicipio = int(catalogoMunicipios.iloc[i,2])
    datosMunicipio = {
    'datoClaveMunicipio' : claveMunicipio,
    'datoMunicipio' : municipio,
    'datoClaveEntidadMunicipio': claveEntidadMunicipio,
    }
    print ("Insertando registro " + str(i) + " de " + str(len(catalogoMunicipios)))
    cursor.execute(addMunicipio, datosMunicipio)
    cnx.commit()
    print ("Registro " + str(i) +  " insertado, completado el " + str(int(i)*100/int(len(catalogoMunicipios))) +  " porciento del total de datos")

##########################################################################################################################
## -> Cargando el fichero con la información de los casos de COVID19 en México...                                       ##  
## -> En el caso que existan campos vacios se les adiciona el valor "NULL"                                              ##
##########################################################################################################################
'''
direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/DatosCovid/datos/COVID19Mexico.csv"

covid19Mexico = panda.read_csv(direccionFichero)
print ("Cargando fichero de datos de Covid-19 en México, puede tardar un momento, por favor espere...")
if covid19Mexico.empty:
    print ("Fichero se encuentra vacío, por favor verifique que sea el correcto...")
else:
    print ("Fichero cargado exitosamente...")
covid19Mexico = covid19Mexico.fillna("NULL")

print ("Imprimiendo los primeros 5 registros del registro de contaminantes SO2...")
print (covid19Mexico.head(5))

print ("    ")
print ("Imprimiendo los últimos 5 registros del registro de contaminantes SO2...")
print (covid19Mexico.tail(5))
































##########################################################################################################################
## -> Cerrando la conexión al SGBD...                                                                                   ##
##########################################################################################################################

cursor.close()
cnx.close()
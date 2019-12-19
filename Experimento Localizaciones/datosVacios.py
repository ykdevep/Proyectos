import pandas as panda

##
## Calculando CO...
##

direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/CO2018.xls"
xls2018 = panda.read_excel(direccionFichero)
direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/CO2019.xls"
xls2019 = panda.read_excel(direccionFichero)

contador2018 = 0
contador2019 = 0
for i in range(0, len(xls2018)):
    for j in range (2, 32):
        if (xls2018.iloc[i,j] == -99):
            contador2018 += 1

for i in range(0, len(xls2019)):
    for j in range (2, 32):
        if (xls2019.iloc[i,j] == -99):
            contador2019 += 1

total = len(xls2018) * 31 + len(xls2019)* 31
suma = contador2018 + contador2019
promedio = suma * 100 / total

print ("CO: " + str(promedio))

##
## Calculando NO...
##

direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/NO2018.xls"
xls2018 = panda.read_excel(direccionFichero)
direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/NO2019.xls"
xls2019 = panda.read_excel(direccionFichero)

contador2018 = 0
contador2019 = 0
for i in range(0, len(xls2018)):
    for j in range (2, 32):
        if (xls2018.iloc[i,j] == -99):
            contador2018 += 1

for i in range(0, len(xls2019)):
    for j in range (2, 32):
        if (xls2019.iloc[i,j] == -99):
            contador2019 += 1

total = len(xls2018) * 31 + len(xls2019)* 31
suma = contador2018 + contador2019
promedio = suma * 100 / total

print ("NO: " + str(promedio))

##
## Calculando NO2...
##

direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/NO22018.xls"
xls2018 = panda.read_excel(direccionFichero)
direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/NO22019.xls"
xls2019 = panda.read_excel(direccionFichero)

contador2018 = 0
contador2019 = 0
for i in range(0, len(xls2018)):
    for j in range (2, 33):
        if (xls2018.iloc[i,j] == -99):
            contador2018 += 1

for i in range(0, len(xls2019)):
    for j in range (2, 33):
        if (xls2019.iloc[i,j] == -99):
            contador2019 += 1

total = len(xls2018) * 32 + len(xls2019)* 32
suma = contador2018 + contador2019
promedio = suma * 100 / total

print ("NO2: " + str(promedio))

##
## Calculando NOX...
##

direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/NOX2018.xls"
xls2018 = panda.read_excel(direccionFichero)
direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/NOX2019.xls"
xls2019 = panda.read_excel(direccionFichero)

contador2018 = 0
contador2019 = 0
for i in range(0, len(xls2018)):
    for j in range (2, 32):
        if (xls2018.iloc[i,j] == -99):
            contador2018 += 1

for i in range(0, len(xls2019)):
    for j in range (2, 32):
        if (xls2019.iloc[i,j] == -99):
            contador2019 += 1

total = len(xls2018) * 31 + len(xls2019)* 31
suma = contador2018 + contador2019
promedio = suma * 100 / total

print ("NOX: " + str(promedio))

##
## Calculando O3...
##

direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/O32018.xls"
xls2018 = panda.read_excel(direccionFichero)
direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/O32019.xls"
xls2019 = panda.read_excel(direccionFichero)

contador2018 = 0
contador2019 = 0
for i in range(0, len(xls2018)):
    for j in range (2, 35):
        if (xls2018.iloc[i,j] == -99):
            contador2018 += 1

for i in range(0, len(xls2019)):
    for j in range (2, 35):
        if (xls2019.iloc[i,j] == -99):
            contador2019 += 1

total = len(xls2018) * 34 + len(xls2019)* 34
suma = contador2018 + contador2019
promedio = suma * 100 / total

print ("O3: " + str(promedio))

##
## Calculando PA...
##

direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/PA2018.xls"
xls2018 = panda.read_excel(direccionFichero)
direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/PA2019.xls"
xls2019 = panda.read_excel(direccionFichero)

contador2018 = 0
contador2019 = 0
for i in range(0, len(xls2018)):
    for j in range (2, 11):
        if (xls2018.iloc[i,j] == -99):
            contador2018 += 1

for i in range(0, len(xls2019)):
    for j in range (2, 11):
        if (xls2019.iloc[i,j] == -99):
            contador2019 += 1

total = len(xls2018) * 10 + len(xls2019)* 10
suma = contador2018 + contador2019
promedio = suma * 100 / total

print ("PA: " + str(promedio))

##
## Calculando PM10...
##

direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/PM102018.xls"
xls2018 = panda.read_excel(direccionFichero)
direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/PM102019.xls"
xls2019 = panda.read_excel(direccionFichero)

contador2018 = 0
contador2019 = 0
for i in range(0, len(xls2018)):
    for j in range (2, 27):
        if (xls2018.iloc[i,j] == -99):
            contador2018 += 1

for i in range(0, len(xls2019)):
    for j in range (2, 27):
        if (xls2019.iloc[i,j] == -99):
            contador2019 += 1

total = len(xls2018) * 26 + len(xls2019)* 26
suma = contador2018 + contador2019
promedio = suma * 100 / total

print ("PM10: " + str(promedio))

##
## Calculando PM25...
##

direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/PM252018.xls"
xls2018 = panda.read_excel(direccionFichero)
direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/PM252019.xls"
xls2019 = panda.read_excel(direccionFichero)

contador2018 = 0
contador2019 = 0
for i in range(0, len(xls2018)):
    for j in range (2, 26):
        if (xls2018.iloc[i,j] == -99):
            contador2018 += 1

for i in range(0, len(xls2019)):
    for j in range (2, 26):
        if (xls2019.iloc[i,j] == -99):
            contador2019 += 1

total = len(xls2018) * 25 + len(xls2019)* 25
suma = contador2018 + contador2019
promedio = suma * 100 / total

print ("PM25: " + str(promedio))

##
## Calculando PMCO...
##

direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/PMCO2018.xls"
xls2018 = panda.read_excel(direccionFichero)
direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/PMCO2019.xls"
xls2019 = panda.read_excel(direccionFichero)

contador2018 = 0
contador2019 = 0
for i in range(0, len(xls2018)):
    for j in range (2, 15):
        if (xls2018.iloc[i,j] == -99):
            contador2018 += 1

for i in range(0, len(xls2019)):
    for j in range (2, 15):
        if (xls2019.iloc[i,j] == -99):
            contador2019 += 1

total = len(xls2018) * 14 + len(xls2019)* 14
suma = contador2018 + contador2019
promedio = suma * 100 / total

print ("PMCO: " + str(promedio))

##
## Calculando RH...
##

direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/RH2018.xls"
xls2018 = panda.read_excel(direccionFichero)
direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/RH2019.xls"
xls2019 = panda.read_excel(direccionFichero)

contador2018 = 0
contador2019 = 0
for i in range(0, len(xls2018)):
    for j in range (2, 27):
        if (xls2018.iloc[i,j] == -99):
            contador2018 += 1

for i in range(0, len(xls2019)):
    for j in range (2, 27):
        if (xls2019.iloc[i,j] == -99):
            contador2019 += 1

total = len(xls2018) * 26 + len(xls2019)* 26
suma = contador2018 + contador2019
promedio = suma * 100 / total

print ("RH: " + str(promedio))

##
## Calculando SO2...
##

direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/SO22018.xls"
xls2018 = panda.read_excel(direccionFichero)
direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/SO22019.xls"
xls2019 = panda.read_excel(direccionFichero)

contador2018 = 0
contador2019 = 0
for i in range(0, len(xls2018)):
    for j in range (2, 32):
        if (xls2018.iloc[i,j] == -99):
            contador2018 += 1

for i in range(0, len(xls2019)):
    for j in range (2, 32):
        if (xls2019.iloc[i,j] == -99):
            contador2019 += 1

total = len(xls2018) * 31 + len(xls2019)* 31
suma = contador2018 + contador2019
promedio = suma * 100 / total

print ("SO2: " + str(promedio))

##
## Calculando TMP...
##

direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/TMP2018.xls"
xls2018 = panda.read_excel(direccionFichero)
direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/TMP2019.xls"
xls2019 = panda.read_excel(direccionFichero)

contador2018 = 0
contador2019 = 0
for i in range(0, len(xls2018)):
    for j in range (2, 27):
        if (xls2018.iloc[i,j] == -99):
            contador2018 += 1

for i in range(0, len(xls2019)):
    for j in range (2, 27):
        if (xls2019.iloc[i,j] == -99):
            contador2019 += 1

total = len(xls2018) * 26 + len(xls2019)* 26
suma = contador2018 + contador2019
promedio = suma * 100 / total

print ("TMP: " + str(promedio))

##
## Calculando UVA...
##

direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/UVA2018.xls"
xls2018 = panda.read_excel(direccionFichero)
direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/UVA2019.xls"
xls2019 = panda.read_excel(direccionFichero)

contador2018 = 0
contador2019 = 0
for i in range(0, len(xls2018)):
    for j in range (2, 12):
        if (xls2018.iloc[i,j] == -99):
            contador2018 += 1

for i in range(0, len(xls2019)):
    for j in range (2, 12):
        if (xls2019.iloc[i,j] == -99):
            contador2019 += 1

total = len(xls2018) * 11 + len(xls2019)* 11
suma = contador2018 + contador2019
promedio = suma * 100 / total

print ("UVA: " + str(promedio))

##
## Calculando UVB...
##

direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/UVB2018.xls"
xls2018 = panda.read_excel(direccionFichero)
direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/BancosDatos/18RAMA/UVB2019.xls"
xls2019 = panda.read_excel(direccionFichero)

contador2018 = 0
contador2019 = 0
for i in range(0, len(xls2018)):
    for j in range (2, 12):
        if (xls2018.iloc[i,j] == -99):
            contador2018 += 1

for i in range(0, len(xls2019)):
    for j in range (2, 12):
        if (xls2019.iloc[i,j] == -99):
            contador2019 += 1

total = len(xls2018) * 11 + len(xls2019)* 11
suma = contador2018 + contador2019
promedio = suma * 100 / total

print ("UVB: " + str(promedio))















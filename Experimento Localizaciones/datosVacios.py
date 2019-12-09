import pandas as panda

direccionFichero = "C:/Users/eacar/Desktop/18RAMA/CO2018.xls"
xls2018 = panda.read_excel(direccionFichero)
direccionFichero = "C:/Users/eacar/Desktop/18RAMA/CO2019.xls"
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

print (contador2018)
print (contador2019)
print (suma)
print (total)
print (promedio)


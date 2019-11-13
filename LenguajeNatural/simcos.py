import pandas as panda
import math as math

direccionFichero = "C:/Users/eacar/Desktop/vector.xls"
xls = panda.read_excel(direccionFichero)

similitud = []
sumatoriaSuperior = 0
sumatoriaInferior1 = 0
sumatoriaInferior2 = 0
resultado = 0

for i in range(0, len(xls)):
    for j in range(i + 1, len(xls)):
        valor1 = xls.iloc[i]
        valor2 = xls.iloc[j]
        for k in range(0,len(valor1)):
            sumatoriaSuperior = sumatoriaSuperior + valor1.iloc[k] * valor2.iloc[k]
            sumatoriaInferior1 = sumatoriaInferior1 + valor1.iloc[k] ** 2
            sumatoriaInferior2 = sumatoriaInferior2 + valor2.iloc[k] ** 2
        resultado = sumatoriaSuperior / (math.sqrt(sumatoriaInferior1) * math.sqrt(sumatoriaInferior2))
        similitud.append(resultado)
        sumatoriaSuperior = 0
        sumatoriaInferior1 = 0
        sumatoriaInferior2 = 0
        resultado = 0

for i in range(0,len(similitud)):
    print (similitud[i])
            

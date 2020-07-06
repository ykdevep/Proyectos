import pandas as pandas
import numpy as numpy
from scipy import stats
import matplotlib
import matplotlib.pyplot as plt
import statistics as estad
import statsmodels.stats.api as sms
import scipy

####
#### Cargando fichero de datos...
####

direccionFichero = "C:/Users/Cubano/Documents/GitHub/Proyectos/AnalisisEstadisticoHRTEMP/Semanas/N24-27.csv"
csv = pandas.read_csv(direccionFichero)

###
### Agregando datos a las listas correspondientes...
###

ritmoCardiaco = []
temperatura = []

for i in range(0, len(csv)):
    ritmoCardiaco.append(csv.iloc[i, 2])
    temperatura.append(csv.iloc[i, 3])

###
### Calculando valores de RC...
###

print("Información del ritmo cardíaco...")
histogramaRC = numpy.histogram(ritmoCardiaco, bins=4)
print("Cantidad de Muestras en cada contenedor del histograma (4 contenedores en total): " + str(histogramaRC[0]))
bordesHistogramaRC = histogramaRC[1]
print("Bordes de los contenedores del histograma: " + str(bordesHistogramaRC))
pruebaEstadisticas = stats.describe(ritmoCardiaco)
valorMaximoRC = pruebaEstadisticas[1][1]
print("Valor máximo: " + str(valorMaximoRC))
valorMinimoRC = pruebaEstadisticas[1][0]
print("Valor mínimo: " + str(valorMinimoRC))
intervalosConfRC = stats.bayes_mvs(ritmoCardiaco)
meanRC = numpy.mean(ritmoCardiaco)
print("Mean: " + str(meanRC))
medianRC = numpy.median(ritmoCardiaco)
print("Median: " + str(medianRC))
rangoRC = numpy.ptp(ritmoCardiaco)
print("Rango: " + str(rangoRC))
desvEstandarRC = numpy.std(ritmoCardiaco)
print("Desviación estándar: " + str(desvEstandarRC))
varianzaRC = intervalosConfRC[1]
print("Varianza: " + str(varianzaRC))
iqrRC = stats.iqr(ritmoCardiaco)
print("Rango intercuartil: " + str(iqrRC))
valorSkewnessRC = pruebaEstadisticas[4]
print("Valor de asimetría: " + str(valorSkewnessRC))
valorKurtosisRC = pruebaEstadisticas[5]
print("Valor de curtosis: " + str(valorKurtosisRC))
ci = scipy.stats.norm.interval(0.95, loc=meanRC, scale=desvEstandarRC)
print("Intervalo inferior de confianza: " + str(ci[0]))
print("Intervalo superior de confianza: " + str(ci[1]))


###
### Calculando valores de TEMP...
###

print("   ")
print("Información de la temperatura...")
histogramaTP = numpy.histogram(temperatura, bins=4)
print("Cantidad de Muestras en cada contenedor del histograma (4 contenedores en total): " + str(histogramaTP[0]))
bordesHistogramaTP = histogramaTP[1]
print("Bordes de los contenedores del histograma: " + str(bordesHistogramaTP))
pruebaEstadisticasTP = stats.describe(temperatura)
valorMaximoTP = pruebaEstadisticasTP[1][1]
print("Valor máximo: " + str(valorMaximoTP))
valorMinimoTP = pruebaEstadisticasTP[1][0]
print("Valor mínimo: " + str(valorMinimoTP))
intervalosConfTP = stats.bayes_mvs(temperatura)
meanTP = numpy.mean(temperatura)
print("Mean: " + str(meanTP))
medianTP = numpy.median(temperatura)
print("Median: " + str(medianTP))
rangoTP = numpy.ptp(temperatura)
print("Rango: " + str(rangoTP))
desvEstandarTP = numpy.std(temperatura)
print("Desviación estándar: " + str(desvEstandarTP))
varianzaTP = intervalosConfTP[1]
print("Varianza: " + str(varianzaTP))
iqrTP = stats.iqr(temperatura)
print("Rango intercuartil: " + str(iqrTP))
valorSkewnessTP = pruebaEstadisticasTP[4]
print("Valor de asimetría: " + str(valorSkewnessTP))
valorKurtosisTP = pruebaEstadisticasTP[5]
print("Valor de curtosis: " + str(valorKurtosisTP))
ciTP = scipy.stats.norm.interval(0.95, loc=meanTP, scale=desvEstandarTP)
print("Intervalo inferior de confianza: " + str(ciTP[0]))
print("Intervalo superior de confianza: " + str(ciTP[1]))


###
### Graficas para Ritmo Cardiaco
###

# Histograma

ax = plt.subplot()
_ = plt.hist(ritmoCardiaco,  bins=4)

# cnfidence interval left line
one_x12, one_y12 = [ci[0],ci[0]], [0, 500]
# cnfidence interval right line
two_x12, two_y12 = [ci[1],ci[1]], [0, 500]


ax.set_xlabel('Muestras')
ax.set_ylabel('Cantidad de valores de cada  muestra')
ax.set_title(r'Histograma de Ritmo Cardíaco e intervalos de confianza')

plt.plot(one_x12, one_y12, two_x12, two_y12, marker = "o")
plt.show()


percentileRC = numpy.percentile(ritmoCardiaco, 100)
quartileRC = numpy.quantile(ritmoCardiaco, 1)


# Grafica ritmo cardiaco

ax = plt.subplot()
_ = plt.plot(ritmoCardiaco)

ax.set_xlabel('Muestras')
ax.set_ylabel('Valor de Ritmo Cardíaco')
ax.set_title(r'Ritmo Cardíaco')
plt.show()

#Histograma 1 Prueba


# example data
mu = meanRC  # mean of distribution
sigma = desvEstandarRC  # standard deviation of distribution
x = mu + sigma * numpy.random.randn(437)

num_bins = 100

fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(ritmoCardiaco, num_bins, density=1)

# add a 'best fit' line
y = ((1 / (numpy.sqrt(2 * numpy.pi) * sigma)) *
     numpy.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')
ax.set_xlabel('Muestras')
ax.set_ylabel('Densidad de probabilidad')
ax.set_title(r'Histograma con función de ajuste para Ritmo Cardíaco')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()


###
### Graficas para Temperatura
###

# Histograma

ax = plt.subplot()
_ = plt.hist(temperatura,  bins=4)

# cnfidence interval left line
one_x12, one_y12 = [ciTP[0],ciTP[0]], [0, 500]
# cnfidence interval right line
two_x12, two_y12 = [ciTP[1],ciTP[1]], [0, 500]


ax.set_xlabel('Muestras')
ax.set_ylabel('Cantidad de valores de cada  muestra')
ax.set_title(r'Histograma de Temperatura e intervalos de confianza')

plt.plot(one_x12, one_y12, two_x12, two_y12, marker = "o")
plt.show()


percentileRC = numpy.percentile(ritmoCardiaco, 100)
quartileRC = numpy.quantile(ritmoCardiaco, 1)


# Grafica ritmo cardiaco

ax = plt.subplot()
_ = plt.plot(temperatura)

ax.set_xlabel('Muestras')
ax.set_ylabel('Valor de Temperatura')
ax.set_title(r'Tempertura')
plt.show()

#Histograma 1 Prueba


# example data
mu = meanTP  # mean of distribution
sigma = desvEstandarTP  # standard deviation of distribution
x = mu + sigma * numpy.random.randn(437)

num_bins = 100

fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(temperatura, num_bins, density=1)

# add a 'best fit' line
y = ((1 / (numpy.sqrt(2 * numpy.pi) * sigma)) *
     numpy.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')
ax.set_xlabel('Muestras')
ax.set_ylabel('Densidad de probabilidad')
ax.set_title(r'Histograma con función de ajuste para Temperatura')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()







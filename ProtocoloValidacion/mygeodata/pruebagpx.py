import gpxpy
import gpxpy.gpx
from pandas import DataFrame
import gpx_csv_converter
from gpx_csv_converter import Converter
import gpx_parser as parser

direccion = "C:/Users/Cubano/Documents/GitHub/Proyectos/ProtocoloValidacion/mygeodata/AAAA.gpx"
fichero = open(direccion, 'r')
fichgpx = gpxpy.parse(fichero)

print (" In the file are {} tracks".format(len(fichgpx.tracks)))
track = fichgpx.tracks[0]
print ("{} segmentos".format(len(track.segments)))
segment = track.segments[0]
print ("{} puntos".format(len(segment.points)))

print(segment.extensions)
data = []
segmentLength = segment.length_3d()
punto = []
for pointIdx, point in enumerate(segment.points):
    data.append([point.longitude, point.latitude, point.elevation, point.time, segment.get_speed(pointIdx)])
    punto.append(point.extensions)


columns = ['Longitude', 'Latitude', 'Altitude', 'Time', 'Speed']
df = DataFrame(data, columns=columns)


df.to_csv('pruebaCSVConvert.csv', header=True, index=False)

print("Iniciando conversion...")
#gpx_csv_converter.Converter(direccion, 'pruebacsv1.csv')
#Converter(direccion, 'pruebaCSVConverter.csv')
print("Terminado...")
import gpxpy
import gpxpy.gpx
from pandas import DataFrame
from gpx_csv_converter import Converter
import gpx_parser as parser



direccion = "C:/Users/Cubano/Documents/GitHub/Proyectos/ProtocoloValidacion/mygeodata/AAAA.gpx"

fichero = open(direccion, 'r')

fichgpx = gpxpy.parse(fichero)
#fichpars = parser.parse(fichero)
prueba1 = str(fichero)
prueba2 = str(fichgpx)
print(fichgpx)
print ("OTRO")
#print(fichpars)
print("FIN")

print (" asd ad as sas a {} tracks".format(len(fichgpx.tracks)))
track = fichgpx.tracks[0]
print ("{} segmentos".format(len(track.segments)))
segment = track.segments[0]
print ("{} puntos".format(len(segment.points)))



print(segment.extensions)
data = []
segmentLength = segment.length_3d()
punto = []
for pointIdx, point in enumerate(segment.points):
    data.append([point.longitude, point.latitude, point.elevation, point.time, point.extensions[0], segment.get_speed(pointIdx)])
    punto.append(point.extensions)


columns = ['Longitude', 'Latitude', 'Altitude', 'Time', 'HeartRate', 'Speed']
df = DataFrame(data, columns=columns)
df.head()

print (df)
print ("   ")
print( "   ")
print (punto[0])
print (type(punto))
print(punto[0][0])
asd = punto[0][0]
print(len(asd.items()))
for elem in range(0,len(asd.items())):
    print("algo")
    print(elem.tag)
    
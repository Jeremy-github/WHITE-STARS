
from os import utime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import utm 

#Carga de un archivo TLE
from skyfield.api import load, wgs84
tle_data_url = 'http://celestrak.com/NORAD/elements/stations.txt'
satellites = load.tle_file(tle_data_url)
print('\nLoaded', len(satellites), 'satellites\n') #carga todos los satelites de CELESTRAK TLE

#actualiza el archivo TLE
reload = True

#print('datos de todos los satelites: \n ',satellites)

#Seleccionar un solo satelite
#by_name = {sat.name: sat for sat in satellites}
#satellite = by_name['AEROCUBE 12A']
#print(satellite)

#Carga de un conjunto TLE desde cadenas
from skyfield.api import EarthSatellite
ts = load.timescale()
line1 = '1 25544U 98067A   14020.93268519  .00009878  00000-0  18200-3 0  5082'
line2 = '2 25544  51.6498 109.4756 0003572  55.9686 274.8005 15.49815350868473'
satellite1 = EarthSatellite(line1, line2, 'ISS (ZARYA)', ts)

line3 = '1 43556U 18046C   21276.80862477  .00006900  00000-0  22746-3 0  9991'
line4 = '2 43556  51.6411 346.9936 0007209 190.3860 169.6973 15.32572317179899'
satellite2 = EarthSatellite(line3, line4, 'AEROCUBE 12A', ts)
print('Obejeto espacial encontrado: ', satellite1,'\n')
print('Obejeto espacial encontrado: ', satellite2,'\n')

#comprobación de la epoca de un TLE metodo #1
#print(satellite1.epoch.utc_jpl(),'\n')
#comprobación de la epoca de un TLE metodo #2
t = ts.utc(2014, 1, 23, 11, 18, 7)
days = t - satellite1.epoch
print('{:.3f} days away from epoch\n'.format(days))
if abs(days) > 14:
    satellites = load.tle_file(tle_data_url, reload=True)


t = ts.utc(2014, 1, 23, 11, 18, 7)
days = t - satellite2.epoch
print('{:.3f} days away from epoch\n'.format(days))
if abs(days) > 14:
    satellites = load.tle_file(tle_data_url, reload=True)



#calcular posicion geocentrica
t = ts.utc(2014, 1, 23, 11, 18, 7)
geocentric = satellite1.at(t)
print('Posicion Geocentrica del Objeto: ', geocentric.position.km,'\n')


t = ts.utc(2014, 1, 23, 11, 18, 7)
geocentric2 = satellite2.at(t)
print('Posicion Geocentrica del Objeto: ', geocentric2.position.km,'\n')

#calcularlongitud, altitud, altura del Satelite
subpoint = wgs84.subpoint(geocentric)
subpoint2 = wgs84.subpoint(geocentric2)

lat = (subpoint.latitude)
lon = (subpoint.longitude)

lat2 = (subpoint2.latitude)
lon2 = (subpoint2.longitude)


print('Latitud:', lat)
print('Longitud:', lon) 
print('Altura: {:.1f} km'.format(subpoint.elevation.km),'\n')

print('Latitud:', lat2)
print('Longitud:', lon2) 
print('Altura: {:.1f} km'.format(subpoint2.elevation.km),'\n')


fig, ax = plt.subplots()

ax.set_title('Puntos de Basura espacial')

ax.scatter (x = [-50.243722, 42.633111  ] , y = [-86.389806, -75.532833 ])

ax.set_ylabel('Longitud')
ax.set_xlabel('Latitud')

plt.savefig('diagrama-dispersion.png')

plt.show()
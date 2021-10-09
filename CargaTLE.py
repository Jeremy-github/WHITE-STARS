
from os import utime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import utm 

#Carga de un archivo TLE en tiempo Real de la Pagina Oficial Celestrak.
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
l1 = '1 25544U 98067A   14020.93268519  .00009878  00000-0  18200-3 0  5082'
l2 = '2 25544  51.6498 109.4756 0003572  55.9686 274.8005 15.49815350868473'
satellite1 = EarthSatellite(l1, l2, 'ISS (ZARYA)', ts)

l3 = '1 43556U 18046C   21276.80862477  .00006900  00000-0  22746-3 0  9991'
l4 = '2 43556  51.6411 346.9936 0007209 190.3860 169.6973 15.32572317179899'
satellite2 = EarthSatellite(l3, l4, 'AEROCUBE 12A', ts)

            
l5 = '1 43558U 18046E   21281.81150634  .00007339  00000-0  22166-3 0  9998'
l6 = '2 43558  51.6404 313.1410 0005778 218.5632 141.4938 15.35284684180784'
satellite3 = EarthSatellite(l5, l6, 'LEMUR-2-VU', ts)

                 
l7 = '1 44031U 98067PX  21281.74676736  .00416901  90543-4  60964-3 0  9996'
l8 = '2 44031  51.6335  32.2752 0008463 338.2659  21.7993 16.04480648153668'
satellite4 = EarthSatellite(l7, l8, 'UNITE', ts)


              

l9 =  '1 46923U 98067RT  21281.87044195  .00018285  00000-0  25389-3 0  9990'
l10 = '2 46923  51.6392 129.7220 0002507 161.6902 198.4180 15.57076256 52545'
satellite5 = EarthSatellite(l9, l10, 'NEUTRON-1 ', ts)


print('Obejeto espacial encontrado: ', satellite1,'\n')
print('Obejeto espacial encontrado: ', satellite2,'\n')
print('Obejeto espacial encontrado: ', satellite3,'\n')
print('Obejeto espacial encontrado: ', satellite4,'\n')
print('Obejeto espacial encontrado: ', satellite5,'\n')


#comprobación de la epoca de un TLE metodo #1
#print(satellite1.epoch.utc_jpl(),'\n')
#comprobación de la epoca de un TLE metodo #2
#t = ts.utc(2014, 1, 23, 11, 18, 7)
#days = t - satellite1.epoch
#if abs(days) > 14:
#    satellites = load.tle_file(tle_data_url, reload=True)


#t = ts.utc(2014, 1, 23, 11, 18, 7)
#days = t - satellite2.epoch
#print('{:.3f} days away from epoch\n'.format(days))
#if abs(days) > 14:
 #   satellites = load.tle_file(tle_data_url, reload=True)



#calcular posicion geocentrica
t = ts.utc(2014, 1, 23, 11, 18, 7)
geocentric = satellite1.at(t)
print(satellite1,'Posicion Geocentrica del Objeto: ', geocentric.position.km,'\n')


t = ts.utc(2014, 1, 23, 11, 18, 7)
geocentric2 = satellite2.at(t)
print(satellite2, 'Posicion Geocentrica del Objeto: ', geocentric2.position.km,'\n')

t = ts.utc(2014, 1, 23, 11, 18, 7)
geocentric3 = satellite3.at(t)
print(satellite3, 'Posicion Geocentrica del Objeto: ', geocentric3.position.km,'\n')


t = ts.utc(2014, 1, 23, 11, 18, 7)
geocentric4 = satellite4.at(t)
print(satellite4, 'Posicion Geocentrica del Objeto: ', geocentric4.position.km,'\n')


t = ts.utc(2014, 1, 23, 11, 18, 7)
geocentric5 = satellite5.at(t)
print(satellite5, 'Posicion Geocentrica del Objeto: ', geocentric5.position.km,'\n')

#calcularlongitud, altitud, altura del Satelite
subpoint = wgs84.subpoint(geocentric)
subpoint2 = wgs84.subpoint(geocentric2)
subpoint3 = wgs84.subpoint(geocentric3)
subpoint4 = wgs84.subpoint(geocentric4)
subpoint5 = wgs84.subpoint(geocentric5)

lat = (subpoint.latitude)
lon = (subpoint.longitude)

lat2 = (subpoint2.latitude)
lon2 = (subpoint2.longitude)

lat3 = (subpoint3.latitude)
lon3 = (subpoint3.longitude)

lat4 = (subpoint4.latitude)
lon4 = (subpoint4.longitude)

lat5 = (subpoint5.latitude)
lon5 = (subpoint5.longitude)


print(satellite1)
print('Latitud:', lat)
print('Longitud:', lon) 
print('Altura: {:.1f} km'.format(subpoint.elevation.km),'\n')

print(satellite2)
print('Latitud:', lat2)
print('Longitud:', lon2) 
print('Altura: {:.1f} km'.format(subpoint2.elevation.km),'\n')

print(satellite3)
print('Latitud:', lat3)
print('Longitud:', lon3) 
print('Altura: {:.1f} km'.format(subpoint3.elevation.km),'\n')

print(satellite4)
print('Latitud:', lat4)
print('Longitud:', lon4) 
print('Altura: {:.1f} km'.format(subpoint4.elevation.km),'\n')

print(satellite5)
print('Latitud:', lat5)
print('Longitud:', lon5) 
print('Altura: {:.1f} km'.format(subpoint5.elevation.km),'\n')



fig, ax = plt.subplots()

ax.set_title('Puntos de Satelites Principal fuente Basura espacial')

ax.scatter (x = [-50.243722, 42.633111, -22.841139, 4.786778, 45.456472] ,
            y = [-86.389806, -75.532833, 95.358528, 80.505056, -83.292056])

ax.set_ylabel('Longitud')
ax.set_xlabel('Latitud')

plt.savefig('Grafica_lonLat_Satelites.png')

plt.show()
import folium
from pymongo import MongoClient

mongo = MongoClient('localhost')

baseDatos = mongo['fusa']

archivos = baseDatos['archivos']

mapa = folium.Map(location =[-39.823641, -73.226158], zoom_start = 14)


for i in archivos.find():
    latitud = i['Latitud']
    longitud = i['Longitud']
    fecha = i['Fecha_grabacion']

    for j in i['Segmentos']:
        for x in j['Etiquetas']:
            fuente = x['Nombre_fuente']
            print(fuente)
                
    folium.Marker([latitud,longitud],popup = fecha,tooltip = fuente).add_to(mapa)
    

mapa.save('C:\\Users\\nicol\\Desktop\\mapa.html')



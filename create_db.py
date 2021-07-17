#Permite crear la base de datos en Mongo e insertar unos datos.
import pymongo, gridfs
import folium
from pymongo import MongoClient

mongo = MongoClient('localhost')

baseDatos = mongo['fusa']

archivos = baseDatos['archivos']

archivos.insert_many([
    {"ID_archivo" : 0,
            "Fecha_grabacion" : "28/06/2021",
            "Ciudad" : "Valdivia",
            "Duracion_archivo" : 60 ,
            "Formato_archivo" : ".wav" ,
            "Latitud" : -39.830040 ,
            "Longitud" : -73.238854 ,
            "Exterior" : "exterior" ,
            "Usuario" : { "RUT" : "19.941.933-1" ,
                          "Nombre" : "Nicol" ,
                          "Apellido" : "Huaiquil"
                          },
            "Segmentos" : [{ "ID_segmento" : 1,
                             "Formato_segmento" : ".wav" ,
                             "Duracion_segmento" : 10 ,
                             "Inicio" : 10,
                             "Fin" : 20,
                             "Etiquetas" : [ {
                                 "Nombre_fuente" : "camión" ,
                                 "Descripcion" : "pip-pip",
                                 "ID_analizador" : 2}]
                             }
                           ]
            },
    {"ID_archivo" : 1,
            "Fecha_grabacion" : "29/06/2021",
            "Ciudad" : "Valdivia",
            "Duracion_archivo" : 60 ,
            "Formato_archivo" : ".wav" ,
            "Latitud" : -39.833451 ,
            "Longitud" : -73.245225 ,
            "Exterior" : "exterior" ,
            "Usuario" : { "RUT" : "19.941.933-1" ,
                          "Nombre" : "Nicol" ,
                          "Apellido" : "Huaiquil"
                          },
            "Segmentos" : [{ "ID_segmento" : 1,
                             "Formato_segmento" : ".wav" ,
                             "Duracion_segmento" : 10 ,
                             "Inicio" : 10,
                             "Fin" : 20,
                             "Etiquetas" : [ {
                                 "Nombre_fuente" : "auto" ,
                                 "Descripcion" : "pip-pip",
                                 "ID_analizador" : 3}]
                             }
                           ]
            },
    {"ID_archivo" : 2,
            "Fecha_grabacion" : "30/06/2021",
            "Ciudad" : "Valdivia",
            "Duracion_archivo" : 60 ,
            "Formato_archivo" : ".wav" ,
            "Latitud" : -39.807097 ,
            "Longitud" : -73.264620 ,
            "Exterior" : "exterior" ,
            "Usuario" : { "RUT" : "19.941.933-1" ,
                          "Nombre" : "Daniel" ,
                          "Apellido" : "Díaz"
                          },
            "Segmentos" : [{ "ID_segmento" : 1,
                             "Formato_segmento" : ".wav" ,
                             "Duracion_segmento" : 10 ,
                             "Inicio" : 10,
                             "Fin" : 20,
                             "Etiquetas" : [ {
                                 "Nombre_fuente" : "camión" ,
                                 "Descripcion" : "pip-pip",
                                 "ID_analizador" : 4}]
                             }
                           ]
            }
    ])


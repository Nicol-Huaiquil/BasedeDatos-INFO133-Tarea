#que permite tambien almacenar archivos audios .wav (maximo 1 minuto) en su base de datos Mongo.
from bson.binary import Binary
from bson import ObjectId
import pymongo, gridfs
from gridfs import GridFS
from pymongo import MongoClient

mongo = MongoClient('localhost')

baseDatos = mongo['fusa']

audios = baseDatos['audios']

audioS = 'ost.wav'
with open(audioS, "rb") as f:
    encoded = Binary(f.read())
audios.insert_one({"nombre_archivo": audioS, "file": encoded, "descripcion": "ost de sailor moon", "fecha_archivo": "28/06/2021"})

audioS1 = 'ost1.wav'
with open(audioS1, "rb") as f:
    encoded = Binary(f.read())
audios.insert_one({"nombre_archivo": audioS1, "file": encoded, "descripcion": "ost de miraculous ladybug", "fecha_archivo": "29/06/2021"})

audioS2 = 'ost2.wav'
with open(audioS2, "rb") as f:
    encoded = Binary(f.read())
audios.insert_one({"nombre_archivo": audioS2, "file": encoded, "descripcion": "ost intro de miraculous ladybug", "fecha_archivo": "30/06/2021"})


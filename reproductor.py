import playsound
from pymongo import MongoClient

mongo = MongoClient('localhost')

baseDatos = mongo['fusa']

audios = baseDatos['audios']

print("Para buscar su archivo de audio ingrese la fecha")
print("ejemplo: '30/06/2021'")
fecha = input(": ")
for i in audios.find():
    if(i['fecha_archivo'] == fecha):
        plus = i["nombre_archivo"]

plus = "audio" + plus
data = audios.find_one({'fecha_archivo': fecha})
        
with open(plus, "wb") as f:
    f.write(data['file'])

print("Reproduciendo audio...")
   
playsound.playsound(plus)

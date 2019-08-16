import requests
import json
from threading import Thread
url = "http://api.openweathermap.org/data/2.5/forecast?lang=es&lat={}&lon={}&APPID=cbe372f2015158b50591b2f1a8f49f13"#liga con la cual se pedira el clima a Open Weather Map
respuestas = {}#diccionario que almacenará todos los climas de las ciudades con el nombre de estas como su llave

def pide_clima(ciudad):
    """Este método sera el ejecutará el hilo de cada peticion y recibe como parámetro el objeto ciudad para con las latitudes pedir el clima y una vez obtenido pueda guardar la información en un diciionario con el nombre de la ciudad como llave """
    peticion = url.format(ciudad.latitud,ciudad.longitud)
    respuesta = requests.get(peticion)#respuesta de Open Weather Map
    json = respuesta.json()#respuesta transformada a formato json para extraer de ella la información deseada de una manera mas sencilla
    if (json["cod"]!=404):
        lista_datos = json.get("list")
        datos_principales = lista_datos[1].get("main") 
        datos_clima = lista_datos[1].get("weather")
        temperatura = str(datos_principales.get("temp")-273.15)
        temperatura = temperatura[0:5]
        clima = datos_clima[0].get("description")
        mensaje = "tiene clima {} con temperatura {}ºC".format(clima,temperatura)
        respuestas[ciudad.nombre] = mensaje 
    else:
        mensaje = "No se encontro la ciudad :{}".format(ciudad.nombre)
        print(mensaje)
        quit()

def obtener_clima(ciudades):
    """Este método recibe todas las ciudades de las cuales se quiere obtener el clima y abre un hilo que pida el clima de cada ciudad"""
    lista_de_hilos = []
    for ciudad in ciudades.values():
        peticion_hilo = Thread(target = pide_clima,args = (ciudad,))
        peticion_hilo.start()
        lista_de_hilos.append(peticion_hilo)
    for hilo in lista_de_hilos:
        hilo.join()
    return respuestas
import requests
import json
url = "http://api.openweathermap.org/data/2.5/forecast?lang=es&lat={}&lon={}&APPID=cbe372f2015158b50591b2f1a8f49f13"#liga con la cual se pedira el clima a Open Weather Map
def obtener_clima(ciudades):
    """Este metodo recibe todas las ciudades de las cuales se quiere obtener el clima y hace la peticion a Open Weather Map con las latitudes y longitudes, regresara todos los climas en un diccionario y la llave de cada clima sera el nombre de su ciudad """
    respuestas = {}
    for ciudad in ciudades.values():
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
    return respuestas
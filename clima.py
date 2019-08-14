import requests
import json
url = "http://api.openweathermap.org/data/2.5/forecast?lang=es&lat={}&lon={}&APPID=cbe372f2015158b50591b2f1a8f49f13"#liga con la cual se pedira el clima a Open Weather Map
def obtener_clima(ciudad):
    """Este metodo recibe la ciudad de la cual se quiere obtener el clima y hace la peticion a Open Weather Map con la latitud y longitud, regresara los datos deseados en caso de encontrarlos"""
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
        return(clima,temperatura)
       
    else:
        mensaje = "No se encontro la ciudad :{}".format(ciudad.nombre)
        print(mensaje)
        quit()
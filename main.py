import sys
import threading
from viaje import Viaje,Ciudad
from clima import obtener_clima
archivo = "Uriel García Luna Bobadilla - dataset.csv"#nombre del archivo que contiene los vuelos
def ejecutar_programa():
    """Este método abre el  archivo(el cual se espera esté en la carpeta principal del programa) que contiene los viajes e imprime el clima de las ciudades de cada uno al momento de correr el algoritmo"""
    try:
        archivo_de_vuelos = open(archivo,"r")
    except IOError as fallo_al_abrir:
        print(fallo_al_abrir)
        print("No se pudo encontrar el archivo")
        quit()
    lista_de_datos = alamcena_vuelos(archivo_de_vuelos)
    vuelos = lista_de_datos[0]
    ciudades = lista_de_datos[1]
    climas = obtener_clima(ciudades)
    for vuelo in vuelos.values():
        mensaje = "El viaje {}, {} en {} y {} en {}".format(vuelo,climas.get(vuelo.ciudad_salida.nombre),vuelo.ciudad_salida,climas.get(vuelo.ciudad_llegada.nombre),vuelo.ciudad_llegada)   
        print(mensaje)
def alamcena_vuelos(archivo_de_vuelos):
    """Este método recibe como parámetro el archivo donde se encuentran los vuelos y regresa una lista con dos diccionarios, el primero de todos los vuelos y el segundo de todas las ciudades sin que se repita alguna, pues usa como llave de estas su nombre """
    numero_de_linea = 0
    cache_de_ciudades  = {} #diccionario que guardara todas las ciudades solo una vez
    vuelos = {}#diccionario que guardara todos los vuelos si importar que estos se repitan
    linea = archivo_de_vuelos.readline()
    while(linea!=""):
       if(numero_de_linea==0):
            linea = archivo_de_vuelos.readline()
            numero_de_linea += 1
            continue
       datos = linea.split(",")
       salida = Ciudad(datos[0],float(datos[2]),float(datos[3]))
       llegada = Ciudad(datos[1],float(datos[4]),float(datos[5]))
       viaje = Viaje(salida,llegada)
       vuelos[numero_de_linea] = viaje
       numero_de_linea += 1
       if(not datos[0] in cache_de_ciudades):
            cache_de_ciudades[datos[0]] = salida
       if(not datos[1] in cache_de_ciudades):
            cache_de_ciudades[datos[1]] = llegada
       linea = archivo_de_vuelos.readline()
    archivo_de_vuelos.close()
    return vuelos,cache_de_ciudades

if __name__ == "__main__":
    """Si se corre esta clase se mandará llamar al método ejecutar_programa() """
    ejecutar_programa()

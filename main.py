import sys
from viaje import Viaje,Ciudad
from clima import obtener_clima
def ejecutar_programa(nombre_de_archivo):
    """Este metodo recibe la dirección del archivo que contiene los viajes y regresa el clima de las ciudades de cada uno al momento de correr el algoritmo"""

    try:
        archivo_de_vuelos = open(nombre_de_archivo,"r")
    except IOError as fallo_al_abrir:
        print(fallo_al_abrir)
        print("No pude abrir el documento que me brindaste")
        quit()
    cache = alamcena_vuelos(archivo_de_vuelos)
    for viaje_actual in cache.values():
        clima_salida = obtener_clima(viaje_actual.ciudad_salida)
        clima_llegada = obtener_clima(viaje_actual.ciudad_salida)
        mensaje = "El viaje {}, tiene clima {} con temperatura {}ºC en {} y clima {} con temperatura {}ºC en {}".format(viaje_actual,clima_salida[0],clima_salida[1],viaje_actual.ciudad_salida,clima_llegada[0],clima_llegada[1],viaje_actual.ciudad_llegada)   
        print(mensaje)
def alamcena_vuelos(archivo_de_vuelos):
    """Este metodo recibe el archivo donde se encuentran los vuelos y los almacena en un cache donde no guardara un vuelo mas de dos veces al final regresa este cache"""
    numero_de_linea = 0
    cache = {} #diccionario que guardara todos los vuelos solo una vez
    linea = archivo_de_vuelos.readline()
    while(linea!=""):
       if(numero_de_linea==0):
            linea = archivo_de_vuelos.readline()
            numero_de_linea += 1
            continue
       datos = linea.split(",")
       clabe = linea[0:3]+linea[4:7] #es la llave con la que guardara cada viaje que es la union de los nombres de las ciudades
       if (clabe in cache):#se pregunta si la llave existe de ser asi se pasa al siguiente linea para de esta manera no repetir ningun vuelo
           linea = archivo_de_vuelos.readline()
       else:
            salida = Ciudad(datos[0],datos[2],datos[3])
            llegada = Ciudad(datos[1],datos[4],datos[5])
            viaje = Viaje(salida,llegada)
            cache.update({clabe:viaje})
            linea = archivo_de_vuelos.readline()
    archivo_de_vuelos.close()
    return cache
if __name__ == "__main__":
    """Si se corre esta clase se recibira la direccion del archivo que se desea leer y se llamara al metodo ejecutar_programa() de lo contrario terminara explicando el problema"""
    try:
        ejecutar_programa(sys.argv[1])
    except IndexError as sin_argumento:
          print(sin_argumento)
          print("Debes darme el archivo con los datos de los vuelos")
          quit()

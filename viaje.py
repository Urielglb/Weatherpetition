class Ciudad:
    """La clase esta conformada por el nombre de la ciudad que servira para que el usuario la reconozca de forma sencilla, la latitud y longitud nos serviran para pedir el clima """
    def __init__(self,nombre=" ",latitud=" ",longitud=" "):
        """Metodo init con el cual se inicilizaran los atributos de la clase"""
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
    def __str__(self):
        """Método str el cual define la representacioón en cadena de la ciudad como el nombre de esta"""
        return self.nombre
class Viaje:    
    """La clase esta conformada por dos ciudades: la de salida y la de llegada.
       La clase esta pensada para que el almacenamiento de los vuelos solo guarde un objeto con 6 atributos y así mejorar la lectura del programa
    """
    def __init__(self,ciudad_salida=" ",ciudad_llegada=" "):
        """Metodo init con el cual se inicializaran los atributos de la clasa"""
        self.ciudad_salida = ciudad_salida
        self.ciudad_llegada = ciudad_llegada
    def __str__(self):
        """Metodo str el cual define la representación en cadena del viaje como la ciudad de salida-ciudad de llegada del mismo"""
        return "%s-%s" %(self.ciudad_salida,self.ciudad_llegada)

#creacion de clase padre y atributos
class medios_de_transporte:
    def __init__(self,marca,color,modelo):
        self.marca=marca
        self.color=color
        self.modelo=modelo
    #clase hija y sus atributos, creacion de funcion super para poder utilisar el contrutor y atributos de la clase padre
class barco(medios_de_transporte):
    def __init__(self,motor,helipuerto,ancla,marca,color,modelo):
        super().__init__(marca,color,modelo)
        self.motor=motor 
        self.helipuerto=helipuerto
        self.ancla=ancla
        self.estado=None
        self.movimiento=None
    #creacion de metodo del ojeto
    def encendido(self):
       self.estado=True
       print("barco encendido, listo para salir")
    def apagado(self):
        self.estado=False
        print(f"el barco { self.marca} esta apagdo")
    def aceleracion(self):
        self.movimiento=True
        print("barco esta en moviento")
    def freno(self):
        self.movimiento=True
        print("barco esta frenando")
#ejecucion del programa
vehiculo=barco("motor YAMAHA","helipuerto elicototero","ancla grande negra","marca CAS","COLOR BLANCO CON AZUL Y ROJO","crucero CAS")
vehiculo.encendido()
vehiculo.aceleracion()
vehiculo.freno()
vehiculo.apagado()

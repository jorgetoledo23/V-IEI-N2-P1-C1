class Botella:
    alto = None
    ancho = None
    capacidadMaxima = None
    color = None
    tipo = None
    capacidadActual = 0

    def rellenarBotella(this, ml):
        if ((this.capacidadActual + ml) > this.capacidadMaxima):
            return False
        else:
            this.capacidadActual = this.capacidadActual + ml 
            return True

class Matematicas:
    PI = 3.1416

    def Sumar(self, n1, n2):
        pass

class Gato:
    especie = "Mamifero"

class Persona:
    rut = None
    nombres = None
    apellidos = None

    #Constructor
    def __init__(self, rut):
        self.rut = rut
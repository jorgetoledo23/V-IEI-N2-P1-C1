class Botella:
    capacidadMaxima = None
    color = None
    marca = None
    alto = None
    ancho = None
    materialConstruccion = None
    capacidadActual = 0

    def rellenarBotella(self, ml):
        if ((self.capacidadActual + ml) > self.capacidadMaxima):
            return "No se puede llenar la botella, SUPERA LA CAPACIDAD MAXIMA!"
        else:
            #self.capacidadActual += ml
            self.capacidadActual = self.capacidadActual + ml
            return "Botella Rellenada!"


class Animal:
    pass

class Gato:
    #Atributo de Clase
    especie = "Mamifero"
    subEspecie = "Felino"


class Auto:
    #Atributos de Clase
    cantidadRuedas = 4

    #Constructor
    def __init__(self, pat, nchas, marca, modelo, color, tipoCombustible, tipoAuto, km):
        #Atributos de Instancia

        #Encapsular
        self.__patente = str(pat).upper()
        self.nchasis = str(nchas).lower()
        self.marca = marca
        self.modelo = modelo
        self.__color = color
        self.tipoCombustible = tipoCombustible
        self.tipoAuto = tipoAuto
        self.kilometraje = km

    def verPatente(self):
        return self.__patente

    def verColor(self):
        return self.__color

    def cambiarColor(self, color):
        self.__color = color


class Persona:

    def __init__(self, rut, nom, ape, edad):
        self.nombres = nom
        self.apellidos = ape,
        self.edad = edad

        if(edad >=18):
            self.mayorEdad = True
        else:
            self.mayorEdad = False

        #Logica para validar/formatear el rut 17.172.876-K

class Mecanico:
    def __init__(self, rut, nom, ape, edad):
        self.nombres = nom
        self.apellidos = ape,
        self.edad = edad
        self.rut = rut

        if(edad >=18):
            self.mayorEdad = True
        else:
            self.mayorEdad = False

    def getNombreCompleto(self):
        return str(self.nombres) + " " + str(self.apellidos)

class Reparacion:

    def __init__(self, auto, mecanico, costo, repuestos):
        self.autoReparado = auto
        self.mecanicoAsignado = mecanico
        self.valor = costo
        self.repuestosUtilizados = repuestos

    def getInfoReparacion(self):
        return f"INFO REPARACION: AUTO PATENTE: {self.autoReparado.verPatente()} COLOR: {self.autoReparado.verColor() }, MECANICO ASIGNADO: {self.mecanicoAsignado.getNombreCompleto()} PRECIO REPARACION: {self.valor}"

    def cambiarColor(self, color):
        self.autoReparado.cambiarColor(color)
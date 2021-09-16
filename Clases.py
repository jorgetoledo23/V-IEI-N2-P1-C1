import os


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
        self.__nchasis = str(nchas).lower()
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__tipoCombustible = tipoCombustible
        self.__tipoAuto = tipoAuto
        self.__kilometraje = km

    def verPatente(self):
        return self.__patente

    def verColor(self):
        return self.__color

    def cambiarColor(self, color):
        self.__color = color

    def GetInfo(self):
        return f"Auto Patente: {self.__patente}, Marca: {self.__marca}, Modelo: {self.__modelo}, Color: {self.__color}, Tipo Auto: {self.__tipoAuto}"


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
        self.edad = int(edad)
        self.rut = rut

        if(edad >= 18):
            self.mayorEdad = True
        else:
            self.mayorEdad = False

    def getNombreCompleto(self):
        return str(self.nombres) + " " + str(self.apellidos)

    def GetInfo(self):
        return f"Mecanico Rut: {self.rut}, Nombres: {self.nombres}, Apellidos: {self.apellidos}, Edad {self.edad}"

class Reparacion:

    def __init__(self, auto, mecanico, costo, repuestos):
        self.autoReparado = auto
        self.mecanicoAsignado = mecanico
        self.valor = costo
        self.repuestosUtilizados = repuestos

    def getInfo(self):
        return f"INFO REPARACION: AUTO PATENTE: {self.autoReparado.verPatente()} COLOR: {self.autoReparado.verColor() }, MECANICO ASIGNADO: {self.mecanicoAsignado.getNombreCompleto()} PRECIO REPARACION: {self.valor}"

    def cambiarColor(self, color):
        self.autoReparado.cambiarColor(color)


class Menu:

    def MostrarMenu():

        print("-------------------------------SISTEMA DE REPARACIONES-----------------------")

        print("Presione 1 para Agregar Automoviles")
        print("Presione 2 para Agregar Mecanicos")
        print("Presione 3 para Agregar Reparaciones")

        print("Presione 4 para Ver los Vehiculos Ingresados")
        print("Presione 5 para Ver los Mecanicos Ingresados")
        print("Presione 6 para Ver las Reparaciones Ingresados")

        print("Escriba Salir para Finalizar!")

    def LimpiarConsola():
        os.system("cls" if os.name =="nt" else "clear")

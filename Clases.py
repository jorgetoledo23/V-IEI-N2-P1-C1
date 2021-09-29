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
    def __init__(self, pat, nchas, color, marca, modelo, year):
        #Atributos de Instancia

        #Encapsular
        self.__patente = str(pat).upper()
        self.__nchasis = str(nchas).lower()
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__year = year


    def verPatente(self):
        return self.__patente

    def setPatente(self, patNueva):
        self.__patente = patNueva

    def verColor(self):
        return self.__color

    def setColor(self, nuevoColor):
        self.__color = nuevoColor

    def setNChasis(self, chasNuevo):
        self.__nchasis = chasNuevo

    def setMarca(self, marca):
        self.__marca = marca

    def setModelo(self, modelo):
        self.__modelo = modelo

    def setYear(self, year):
        self.__year = year

    def GetInfo(self):
        return f"Auto Patente: {self.__patente}, Marca: {self.__marca}, Modelo: {self.__modelo}, Color: {self.__color}, Año: {self.__year}"

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
    def __init__(self, rut, nom, ape, edad,dir):
        self.__Nombres = nom
        self.__Apellidos = ape
        self.__Edad = int(edad)
        self.__Rut = rut
        self.__Direccion = dir

    def getNombreCompleto(self):
        return str(self.__Nombres) + " " + str(self.__Apellidos)

    def GetInfo(self):
        return f"Mecanico Rut: {self.__Rut}, Nombres: {self.__Nombres}, Apellidos: {self.__Apellidos}, Edad {self.__Edad}, Direccion: {self.__Direccion}"

class Reparacion:

    def __init__(self, auto, mecanico, costo, repuestos):
        self.__Auto = auto
        self.__Mecanico = mecanico
        self.__Valor = costo
        self.__Repuesto = repuestos

    def GetInfo(self):
        return f"INFO REPARACION: AUTO: {self.__Auto.GetInfo()}, MECANICO ASIGNADO: {self.__Mecanico.GetInfo()}, PRECIO REPARACION: ${self.__Valor}"

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

        print("Presione 7 para Editar informacion de un Automovil")
        print("Presione 8 para Eliminar un Automovil")

        print("Escriba Salir para Finalizar!")

    def LimpiarConsola():
        os.system("cls" if os.name =="nt" else "clear")

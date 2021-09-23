from Clases import *

#Tabla para Autos
listaAutos = []

#Tabla para Mecanicos
listaMecs = []

#Tabla para Reparaciones
listaReps = []

while True:

    Menu.LimpiarConsola()
    Menu.MostrarMenu()

    opcionSeleccionada = input(" : ")

    if opcionSeleccionada == "1":
        #Logica para Insertar Vehiculos   
        Menu.LimpiarConsola()
        print("----------------------Opcion Seleccionada Agregar Vehiculo!--------------------")
        print(" ")
        pat = input("Ingrese Patente: ")
        nchas = input("Ingrese Numero de Chasis: ")
        marca = input("Ingrese Marca: ")
        modelo = input("Ingrese Modelo: ")
        color = input("Ingrese Color: ")
        year = input("Ingrese Año: ")
        tAuto = input("Ingrese Tipo de Auto: ")
        tComb = input("Ingrese Tipo Combustible: ")
        km = input("Ingrese Kilometraje: ")

        #Crear Objeto / Instacia
        A = Auto(pat,nchas,marca,modelo,color,tComb,tAuto,km)
        
        #Insertar en la Base de Datos
        listaAutos.append(A)
        print(" ")
        input("Auto Ingresado Correctamente! Presiona Enter para Continuar...")

    if opcionSeleccionada == "2":
        Menu.LimpiarConsola()
        print("----------------------Opcion Seleccionada Agregar Mecanico!--------------------")
        print(" ")
        rut = input("Ingrese Rut: ")
        nom = input("Ingrese Nombres: ")
        ape = input("Ingrese Apellidos: ")
        edad = int(input("Ingrese Edad: "))

        #Crear el Objeto / Instancia
        Mec = Mecanico(rut, nom, ape, edad)

        #Insertar en la Base de Datos / Lista
        listaMecs.append(Mec)
        print(" ")
        input("Mecanico Ingresado Correctamente! Presiona Enter para Continuar...")

    if opcionSeleccionada == "3":
        Menu.LimpiarConsola()
        print("----------------------Opcion Seleccionada Agregar Reparacion!--------------------")
        print(" ")

        if ((len(listaAutos) > 0) & (len(listaMecs) > 0)):
            #OKEy. Se pueden agregar reparaciones
            #Objeto de tipo Auto
            i = 1
            for A in listaAutos:
                print(f"Opcion {i}: {A.GetInfo()}")
                i += 1

            opcion = int(input("Seleccine el Numero del Auto a Reparar: "))
            auto = listaAutos[opcion - 1]

            i = 1
            for M in listaMecs:
                print(f"Opcion {i}: {M.GetInfo()}")
                i += 1

            opcion = int(input("Seleccine el Numero del Mecanico para la Reparacion: "))
            mec = listaMecs[opcion - 1]

            valorReparacion = int(input("Ingresa Valor de la Reparacion: "))

            repuesto = input("Ingresa Repuesto Utilizado en la Reparacion: ")

            Rep = Reparacion(auto, mec, valorReparacion, repuesto)
            
            listaReps.append(Rep)

            print(" ")
            input("Reparacion Ingresada Correctamente! Presiona Enter para Continuar...")

        else:
            print("No puedes agregar Reparaciones sin Autos/Mecanicos Ingresados!")
            print(" ")
            input("Presiona Enter para Continuar...")


    if opcionSeleccionada == "4":
        Menu.LimpiarConsola()
        #Mostrar Vehiculos
        for A in listaAutos:
            print(A.GetInfo())
        print(" ")
        input("Mostrando listado de Vehiculos! Presiona Enter para Continuar...")

    if opcionSeleccionada == "5":
        Menu.LimpiarConsola()
        #Mostrar Vehiculos
        for M in listaMecs:
            print(M.GetInfo())
        print(" ")
        input("Mostrando listado de Mecanicos! Presiona Enter para Continuar...")

    if opcionSeleccionada == "6":
        Menu.LimpiarConsola()
        #Mostrar Vehiculos
        for R in listaReps:
            print(R.GetInfo())
        print(" ")
        input("Mostrando listado de Mecanicos! Presiona Enter para Continuar...")

    if opcionSeleccionada == "Salir": 
        print("Saliendo del Sistema. Gracias!")
        break
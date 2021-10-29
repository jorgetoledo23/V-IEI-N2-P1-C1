from Clases import *

def insertarDatosTesting():
    A = Auto('GHFG23','GTSFDRSF343434','ROJO', 'KIA','RIO 5', 2013)
    A2 = Auto('WESD17','HSTDGDRSF34332','BLANCO', 'NISSAN','TERRANO', 2010)
    A3 = Auto('HTDG22','IKYUHHFTDG2323','GRIS', 'MAZDA','CX 5', 2020)
    listaAutos.append(A)
    listaAutos.append(A2)
    listaAutos.append(A3)

    M = Mecanico('1.123.123-1','ALEXIS', 'SANCHEZ', 35, 'CURICO')
    M2 = Mecanico('2.123.123-1','ARTURO', 'VIDAL', 30, 'MOLINA')
    M3 = Mecanico('3.123.123-1','GARY', 'MEDEL', 40, 'TENO')
    listaMecs.append(M)
    listaMecs.append(M2)
    listaMecs.append(M3)

#Tabla para Autos
listaAutos = []

#Tabla para Mecanicos
listaMecs = []

#Tabla para Reparaciones
listaReps = []

insertarDatosTesting()

while True:

    Menu.LimpiarConsola()
    Menu.MostrarMenu()

    opcionSeleccionada = input(" : ")


    if opcionSeleccionada == "7":
        #Editar Auto
        Menu.LimpiarConsola()

        i = 1
        for A in listaAutos:
            print(f"Opcion {i}: {A.GetInfo()}")
            i += 1

        opcion = int(input("Seleccine el Numero del Auto a Editar: "))

        listaAutos[opcion - 1].setPatente(input('Ingrese Nueva Patente: '))
        listaAutos[opcion - 1].setNChasis(input('Ingrese Nuevo Numero de Chasis: '))
        #Casting
        listaAutos[opcion-1].setColor(input('Ingrese Nuevo Color: '))
        listaAutos[opcion-1].setMarca(input('Ingrese Nueva Marca: '))
        listaAutos[opcion-1].setModelo(input('Ingrese Nuevo Modelo: '))
        listaAutos[opcion-1].setYear(input('Ingrese Nuevo Año: '))
        
        print(" ")
        print("Auto Editado Exitosamente. Presione Enter para Continuar...")

    if opcionSeleccionada == "8":
        Menu.LimpiarConsola()

        #VALIDAR QUE EL AUTO A ELIMINAR NO ESTE EN UNA REPARACION

        i = 1
        for A in listaAutos:
            print(f"Opcion {i}: {A.GetInfo()}")
            i += 1

        opcion = int(input("Seleccine el Numero del Auto a Eliminar: "))

        listaAutos.remove(listaAutos[opcion -1])

        print(" ")
        print("Auto Eliminado Exitosamente. Presione Enter para Continuar...")


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

        #Crear Objeto / Instacia
        A = Auto(pat,nchas,color,marca,modelo,year)
        
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
        dir = input('Ingrese Direccion:')

        #Crear el Objeto / Instancia
        Mec = Mecanico(rut, nom, ape, edad, dir)

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
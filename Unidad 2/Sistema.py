from Model.Clases import *
from ConexionMySql import DAO

dao = DAO()
mP = MenuPrincipal()

while True:
    mP.LimpiarConsola()
    mP.MostrarMenu()

    oP = str(input(" : "))

    if oP == "1":
        mP.LimpiarConsola()
        mP.MenuSecundario("Cliente")
        oP = str(input(" : "))

        if oP == "1":
            #Insertar data Cliente a la Base de Datos
            mP.LimpiarConsola()
            print("======= Agregando Cliente =======")
            print("Complete la Informacion Solicitada:")
            print("")

            Rut = str(input("Rut: "))
            Nombres = str(input("Nombres: "))
            Apellidos = str(input("Apellidos: "))
            Telefono = str(input("Telefono: "))
            Correo = str(input("Correo: "))
            Direccion = str(input("Direccion: "))
            Comuna = str(input("Comuna: "))

            C = Cliente(Rut,Nombres,Apellidos,Correo,Telefono,Direccion,Comuna)

            dao.InsertarCliente(C)

            mP.ConfirmacionIngreso("Cliente")

        if oP == "2":
            #Listar TODOS los clientes que esten almacenados en la base de datos
            mP.LimpiarConsola()
            print("======= Listando Clientes =======")
            print("=================================")
            print("")

            for C in dao.ListarClientes():
                print(C.getInfo())

            print("")
            input("Presione Enter para Continuar...")

        if oP == "3":
            #Actualizar Cliente
            mP.LimpiarConsola()
            print("======= Editando Cliente =======")
            print("=================================")
            print("======= Seleccione el Cliente que desea Actualizar =======")
            print("")

            for C in dao.ListarClientes():
                print(C.getInfoDetallada())

            RutAntiguo = input("Digite Rut del Cliente: ")

            mP.LimpiarConsola()
            print(f"======= Editando Cliente: {RutAntiguo} =======")
            print("============== Complete la Informacion ===================")
            print("")

            Rut = str(input("Rut: "))
            Nombres = str(input("Nombres: "))
            Apellidos = str(input("Apellidos: "))
            Telefono = str(input("Telefono: "))
            Correo = str(input("Correo: "))
            Direccion = str(input("Direccion: "))
            Comuna = str(input("Comuna: "))
            C = Cliente(Rut,Nombres,Apellidos,Correo,Telefono,Direccion,Comuna)

            dao.ActualizarCliente(C, RutAntiguo)
            mP.ConfirmacionEdit('Cliente')

        if oP == "4":
            #Eliminar Cliente
            mP.LimpiarConsola()
            print("======= Eliminando Cliente =======")
            print("=================================")
            print("======= Seleccione el Cliente que desea Eliminar =======")
            print("Cuidado, la data eliminada no se puede Recuperar!")
            print("")

            for C in dao.ListarClientes():
                print(C.getInfoDetallada())

            Rut = input("Digite Rut del Cliente: ")

            confirmacion = input(f"Estas seguro de eliminar al Cliente Rut: {Rut} (Y/N): ")

            if confirmacion == "Y":
                dao.EliminarCliente(Rut)
                mP.ConfirmacionDelete("Cliente")
            
            if confirmacion == "N":
                print("Operacion Cancelada")
                input("Presione Enter para Continuar...")


        if oP == "0":
            pass

        oP == None

    if oP == "2":
        #Gestionamos Mecanicos
        mP.LimpiarConsola()
        mP.MenuSecundario("Mecanico")
        oP = str(input(" : "))

        if oP == "1":
            #Insertar data Mecanico a la Base de Datos
            mP.LimpiarConsola()
            print("======= Agregando Mecanico =======")
            print("Complete la Informacion Solicitada:")
            print("")

            Rut = str(input("Rut: "))
            Nombres = str(input("Nombres: "))
            Apellidos = str(input("Apellidos: "))
            Telefono = str(input("Telefono: "))
            Correo = str(input("Correo: "))
            Direccion = str(input("Direccion: "))
            Comuna = str(input("Comuna: "))

            M = Mecanico(Rut,Nombres,Apellidos,Correo,Telefono,Direccion,Comuna)

            dao.InsertarMecanico(M)

            mP.ConfirmacionIngreso("Mecanico")

        if oP == "2":
            #Listar TODOS los Mecacnicos que esten almacenados en la base de datos
            mP.LimpiarConsola()
            print("======= Listando Mecanicos =======")
            print("=================================")
            print("")

            for M in dao.ListarMecanicos():
                print(M.getInfo())

            print("")
            input("Presione Enter para Continuar...")

        if oP == "3":
            #Actualizar Mecanico
            mP.LimpiarConsola()
            print("======= Editando Mecanico =======")
            print("=================================")
            print("======= Seleccione el Mecanico que desea Actualizar =======")
            print("")

            for C in dao.ListarMecanicos():
                print(C.getInfoDetallada())

            RutAntiguo = input("Digite Rut del Mecanico: ")

            mP.LimpiarConsola()
            print(f"======= Editando Mecanico: {RutAntiguo} =======")
            print("============== Complete la Informacion ===================")
            print("")

            Rut = str(input("Rut: "))
            Nombres = str(input("Nombres: "))
            Apellidos = str(input("Apellidos: "))
            Telefono = str(input("Telefono: "))
            Correo = str(input("Correo: "))
            Direccion = str(input("Direccion: "))
            Comuna = str(input("Comuna: "))
            M = Mecanico(Rut,Nombres,Apellidos,Correo,Telefono,Direccion,Comuna)

            dao.ActualizarMecanico(M, RutAntiguo)
            mP.ConfirmacionEdit('Mecanico')


        if oP == "4":
            #Eliminar Mecanico
            mP.LimpiarConsola()
            print("======= Eliminando Mecanico =======")
            print("=================================")
            print("======= Seleccione el Mecanico que desea Eliminar =======")
            print("Cuidado, la data eliminada no se puede Recuperar!")
            print("")

            for C in dao.ListarMecanicos():
                print(C.getInfoDetallada())

            Rut = input("Digite Rut del Mecanico: ")

            confirmacion = input(f"Estas seguro de eliminar al Mecanico Rut: {Rut} (Y/N): ")

            if confirmacion == "Y":
                dao.EliminarMecanico(Rut)
                mP.ConfirmacionDelete("Mecanico")
            
            if confirmacion == "N":
                print("Operacion Cancelada")
                input("Presione Enter para Continuar...")


        if oP == "0":
            pass

        oP = None

    if oP == "3":
        #Gestionamos Vehiculos
        mP.LimpiarConsola()
        mP.MenuSecundario("Vehiculo")
        oP = str(input(" : "))

        if oP == "1":
            #Ingresar nuevo Vehiculo
            mP.LimpiarConsola()
            print("======= Agregando Vehiculo =======")
            print("Complete la Informacion Solicitada:")
            print("")

            Patente = input("Ingrese Patente: ")
            Marca = input("Ingrese Marca: ")
            Modelo = input("Ingrese Modelo: ")
            Year = input("Ingrese Year: ")
            NChasis =  input("Ingrese Numero de Chasis: ")
            Color = input("Ingrese Color: ")

            mP.LimpiarConsola()
            print("======= Seleccion Cliente =======")
            print("")

            for C in dao.ListarClientes():
                print(C.getInfo())

            print("")
        
            rutCliente = input("Ahora Ingrese Rut del Cliente de la Lista Anterior: ")

            A = Auto(Patente, NChasis, Color, Marca, Year, Modelo, rutCliente)

            dao.InsertarVehiculo(A)

            mP.ConfirmacionIngreso("Vehiculo")

        if oP == "2":
            #listar Vehiculos
            mP.LimpiarConsola()
            print("======= Listando Vehiculos =======")
            print("=================================")
            print("")

            for A in dao.ListarVehiculos():
                print(A.getInfo())

            print("")
            input("Presione Enter para Continuar...")


        if oP == "4":
            #Eliminar Vehiculo
            mP.LimpiarConsola()
            print("======= Eliminando Vehiculo =======")
            print("=================================")
            print("======= Seleccione el Vehiculo que desea Eliminar =======")
            print("Cuidado, la data eliminada no se puede Recuperar!")
            print("")

            for C in dao.ListarVehiculos():
                print(C.getInfo())

            Patente = input("Digite Patente del Vehiculo: ")

            confirmacion = input(f"Estas seguro de eliminar al Vehiculo Rut: {Rut} (Y/N): ")

            if confirmacion == "Y":
                dao.EliminarVehiculo(Patente)
                mP.ConfirmacionDelete("Vehiculo")
            
            if confirmacion == "N":
                print("Operacion Cancelada")
                input("Presione Enter para Continuar...")
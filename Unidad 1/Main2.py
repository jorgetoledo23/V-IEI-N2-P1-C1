from Clases import Auto, Gato, Mecanico, Reparacion

autoUno = Auto( #Aca se ejecuta el metodo Constructor
    pat="fsHg18",
    nchas="GFTBCVDF34",
    modelo="RIO",
    marca="KIA",
    km=100000,
    tipoAuto="Sedan",
    tipoCombustible="Diesel",
    color="Rojo")
autoDos = Auto("jGHx23", 
    "HJSHDKAJSHXCTYY4544", 
    "nIssAn", 
    "350Z",
    "Gris", 
    "Bencina", 
    "Hashback", 
    20000)

mecanicoUno = Mecanico("9.123.456-9", "Juan", "Moya", 35)
mecanicoDos = Mecanico("13.456.678-K", "Felipe", "Gonzalez", 28)

listaRepuestosUno = ["Empaquetadura Culata", "Sellante", "Aceite de Motor"]
listaRepuestosDos = ["Masilla", "Pintura", "Lija"]

reparacionUno = Reparacion(autoUno, mecanicoUno, 285000, listaRepuestosUno)
reparacionDos = Reparacion(autoDos, mecanicoDos, 540000, listaRepuestosDos)

reparacionDos.cambiarColor("Blanco")

print(reparacionDos.autoReparado.verPatente()) #JGHX23



#reparacionTres = Reparacion("asdasdasd", "hjajajja", True, False)

print(reparacionUno.getInfoReparacion())
print(reparacionDos.getInfoReparacion())

#INFO REPARACION: AUTO PATENTE: JAJAJAJAJAJA MECANICO ASIGNADO: Felipe ('Gonzalez',) PRECIO REPARACION: 540000


#INFO REPARACION: AUTO PATENTE: FSHG18 MECANICO ASIGNADO: Juan ('Moya',) PRECIO REPARACION: 285000
#INFO REPARACION: AUTO PATENTE: JGHX23 MECANICO ASIGNADO: Felipe ('Gonzalez',) PRECIO REPARACION: 540000






#autoUno.marca = "KIA" #Setear / Dar Valor
#autoDos.marca = "NISSAN"

#print(autoUno.patente) #Get / Obtener
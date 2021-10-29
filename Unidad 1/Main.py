from Clases import Botella, Matematicas, Gato, Persona

#Objeto a traves de la Intanciacion
miBotella = Botella()

botellaNatalia = Botella()

miBotella.capacidadMaxima = 1000
botellaNatalia.capacidadMaxima = 500

miBotella.color = "Plateado"
botellaNatalia.color = "Rosado"

miBotella.rellenarBotella(500)

botellaNatalia.rellenarBotella(1000)

print("Mi Botella actualmente tiene: ", miBotella.capacidadActual)
print("La Botella de Natalia actualmente tiene: ",botellaNatalia.capacidadActual)

print(miBotella)
print(botellaNatalia)


objetoMath = Matematicas()
print(Matematicas.PI)

print(Gato.especie)

yo = Persona("17.172.333-K")


print(yo.rut)



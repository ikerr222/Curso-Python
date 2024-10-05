#!/usr/bin/env python3

#Estructura de pares nombre-valor, sin índices, se pude modificar

diccionario = {"nombre": "iker", "edad": 22, "ciudad": "Tres Cantos"}

diccionario["nombre"] = "Mbappe"
diccionario["profesion"] = "Hacker"
#del diccionario["ciudad"]

if "ciudad" in diccionario:
    print("Esta clave existe")

#for key, value in diccionario.items():
    #print(f"Para la clave {key} tendríamos el valor {value}")

#print(diccionario["nombre"])
#print(type(diccionario))
print(f"La longitud del diccionario es {len(diccionario)}")
#diccionario.clear()
#print(diccionario.get("nombr", "No encontrado") #Si no lo encuentra te escribe lo segundo
diccionario2 = {"mascota": "Prenda"}
diccionario.update(diccionario2)
print(diccionario)

#cuadrados = {x: x**2 for x in range(6)}
#print(cuadrados)
#print(cuadrados.keys())
#print(cuadrados.values())

my_dict = {
    "nombre": "Iker",
    "hobbies": {"primero": "musica", "segundo": "fútbol"},
    "edad": 22
}

print(my_dict)

#!/usr/bin/env python3

class Persona:

    def __init__(self,nombre,edad): #constructor __init__(iker, nombre, edad)

        self.nombre = nombre
        self.edad = edad

    def saludo(self): # Persona.saludo(iker)

        return f"Hola soy {self.nombre} y tengo {self.edad} años"


iker = Persona("Iker", 22)
juan = Persona("Juan", 23)

print(juan.saludo())
print(iker.saludo())


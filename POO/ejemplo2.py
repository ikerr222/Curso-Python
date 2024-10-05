#!/usr/bin/env python3

class Animal:

    def __init__(self, nombre, animal):

        self.nombre = nombre
        self.animal = animal

    def descripcion(self):

        print(f"{self.nombre} es un {self.animal}")

gato = Animal("Furgo", "Gato")
perro = Animal("Prenda", "Perro")

gato.descripcion()
perro.descripcion()

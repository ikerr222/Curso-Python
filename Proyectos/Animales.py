#!/usr/bin/env python3

class Animal:

    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.alimentado = False

    def alimentar(self):
        self.alimentado = True

    def vender(self):
        self.alimentado = False

    def __str__(self):
        return f"{self.nombre} ({self.especie}) - {'Alimentado' if self.alimentado else 'Hambriento'}"

class TiendaAnimales:

    def __init__(self, nombre):
        self.nombre = nombre
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def mostrar_animales(self):
        for animal in self.animales:
            print(animal)

    def alimentar_animales(self):
        for animal in self.animales:
            animal.alimentar()

    def vender_animal(self, nombre):
        for animal in self.animales:
            if animal.nombre == nombre:
                animal.vender()
                self.animales.remove(animal)
                return #Por si la lista es muy grande, cuando lo encuentra se acaba, podria ser break
        print(f"\nNo se ha encontrado ningún animal con nombre {nombre}")



if __name__ == '__main__':

    tienda = TiendaAnimales("Mi tienda de animales")

    gato = Animal("Furgo", "Gato")
    perro = Animal("Prenda", "Perro")

    tienda.agregar_animal(gato)
    tienda.agregar_animal(perro)

    tienda.mostrar_animales()
    tienda.alimentar_animales()

    print("\nMostrando los animales una vez han sido alimentados\n")

    tienda.mostrar_animales()
    tienda.vender_animal("Furgo")

    print(f"\nMostrando los animales una vez Furgo ha sido vendido:\n")

    tienda.mostrar_animales()

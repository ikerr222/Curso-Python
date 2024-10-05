#!/usr/bin/env python3

class Libro:

    
    def __init__(self, titulo, autor, precio):

        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    @staticmethod #Decoradores
    def es_bestseller(total_ventas): #mi_libro, total_ventas

        return total_ventas > 5000

    @staticmethod
    def precio_con_iva(self):

        return precio + precio * Libro.IVA

mi_libro = Libro("Cant hurt me", "David Goggins", 18)
#print(Libro.es_bestseller(mi_libro, 7000))
print("\nEl precio con IVA es {mi_libro.precio_con_iva()}")

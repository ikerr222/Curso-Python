#!/usr/bin/env python3

class Rectangulo:

    def __init__(self, ancho, alto):

        self.ancho = ancho
        self.alto = alto

      
    def area(self): #Le paso un rectangulo
        
        return self.ancho * self.alto


    def __str__(self):

        return f"\n Propiedades del rectángulo: [Ancho: {self.ancho}][Alto: {self.alto}]"

    def __eq__(self, otro):
        return self.ancho == otro.ancho and selt.alto == otro.alto

rect2 = Rectangulo(10,60)
rect1 = Rectangulo(20,80)
print(f"\n El area es {rect1.area()}")
print(rect1)
print(f"\n Son iguales? -> {rect1 == rect2}")


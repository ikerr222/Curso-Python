#!/usr/bin/env python3

import pickle
from notas import Nota

class GestorNotas:

    def __init__(self, archivo_notas='notas.pkl'):
        self.archivo_notas = archivo_notas

        try:

            with open(self.archivo_notas, 'rb') as f:
                self.notas = pickle.load(f)

        except FileNotFoundError:
            self.notas = []

    def guardar_nota(self):
        with open(self.archivo_notas, 'wb') as f:
            pickle.dump(self.notas, f)

    def agregar_nota(self, contenido):
        self.notas.append(Nota(contenido))
        self.guardar_nota()

    def leer_notas(self):
        return self.notas

    def buscar_nota(self, texto_busqueda):
        return [nota for nota in self.notas if nota.coincide(texto_busqueda)]

    def eliminar_nota(self, index):
        if index < len(self.notas):
            del self.notas[index]
            self.guardar_nota() #Vuelve a abrir el archivo y mete la lista de notas con la nota que acabamos de borrar
        else:
            print(f"\nEl indice proporcionado es incorrecto\n")



   

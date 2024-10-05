#!/usr/bin/env python3

class Libro:

    def __init__(self, id_libro, autor, nombre_libro):

        self.id_libro = id_libro
        self.autor = autor
        self.nombre_libro = nombre_libro
        self.esta_prestado = False

    def __str__(self):
        return f"Libro({self.id_libro}, {self.autor}, {self.nombre_libro})"

    def __repr__(self):
        return self.__str__() #Representa la misma información de forma más adecuada(Sin comillas)


class Biblioteca:

    def __init__(self):
        self.libros = {} # Diccionario con los libros que hay en la biblioteca.
        # {1: Libro(1, ...), 2: Libro(2,...)

    def agregar_libro(self, libro):
        if libro.id_libro not in self.libros:# Comprobamos si el libro está ya o no
            self.libros[libro.id_libro] = libro
        else:
            print(f"\nNo es posible agregar el libro con ID {libro.id_libro}")

    def prestar_libro(self, id_libro):
        if id_libro in self.libros and not self.libros[id_libro].esta_prestado:
            self.libros[id_libro].esta_prestado = True
        else:
            print(f"\n No es posible prestar el libro con ID: {id_libro}")

    @property
    def mostrar_libros(self):
        return [libro for libro in self.libros.values() if not libro.esta_prestado] 
        #.values: valor de cada elemento del diccionario

    @property
    def mostrar_libros_prestados(self):
        return [libro for libro in self.libros.values() if libro.esta_prestado]

class BibliotecaInfantil(Biblioteca):

    def __init__(self):
        super().__init__()
        self.libros_para_ninos = {} # -> {1: False, 2. True}

    def agregar_libro(self, libro, es_para_ninos):
        super().agregar_libro(libro)
        self.libros_para_ninos[libro.id_libro] = es_para_ninos

    def prestar_libro(self, id_libro, es_nino):
        if id_libro in self.libros and self.libros_para_ninos[id_libro] == es_nino and not self.libros[id_libro].esta_prestado:
            self.libros[id_libro].esta_prestado = True
        else:
            print(f"\n No es posible prestar el libro con ID: {id_libro}")
    @property
    def mostrar_estado_libros_para_ninos(self):
        return self.libros_para_ninos


if __name__ == '__main__':

    biblioteca = BibliotecaInfantil()

    libro1 = Libro(1, "David Goggins", "Cant Hurt Me")
    libro2 = Libro(2, "Centrate", "Cal Newport")

    biblioteca.agregar_libro(libro1, es_para_ninos=False)
    biblioteca.agregar_libro(libro2, es_para_ninos=True)

    print(f"\n Todos los Libros en la Biblioteca: {biblioteca.mostrar_libros}") 

    biblioteca.prestar_libro(1, es_nino=False)

    print(f"\n Libros en la Biblioteca: {biblioteca.mostrar_libros}") 
    print(f"\n Libros prestados: {biblioteca.mostrar_libros_prestados}")
    print(f"\n Libros para niños: {biblioteca.mostrar_estado_libros_para_ninos}")


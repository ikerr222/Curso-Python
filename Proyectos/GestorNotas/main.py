#!/usr/bin/env python3

import os
from gestor import GestorNotas

def main():

    gestor = GestorNotas()

    while True:  # Bucle infinito

        print(f"\n--------------\nMENÚ\n---------------")
        print("1. Agregar una nota")
        print("2. Leer todas las notas")
        print("3. Buscar por una nota")
        print("4. Eliminar una nota")
        print("5. Salir")

        opcion = input("\nEscoge una opción: ")

        if opcion == "1": # Doble comillas porque es un string, agregar int(input... para que no haga falta ponerlas
            contenido = input("\nContenido de la nota: ")
            gestor.agregar_nota(contenido)

        elif opcion == "2":
            notas = gestor.leer_notas()

            print("\nMostrando todas las notas almacenadas:\n")
            for i, nota in enumerate(notas):
                print(f"{i}: {nota}")

        elif opcion == "3":
            texto_busqueda = input("\nIngresa el texto a buscar como criterio en las notas: ")
            notas = gestor.buscar_nota(texto_busqueda)

            print(f"\nMostrando las notas que coinciden con el criterio de búsqueda:\n ")
            for i, nota in enumerate(notas):
                print(f"{i}: {nota}")

        elif opcion == "4":
            index = int(input("\nIntroduce el índice de la nota que quieres borrar: "))
            gestor.eliminar_nota(index)

        elif opcion == "5":
            break
        else:
            print("\nLa opción indicada es incorrecta\n")

        input(f"\nPresiona <Enter> para continuar")

        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    main()

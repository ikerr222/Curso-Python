#!/usr/bin/env python3

class Vehiculo:
    
    def __init__(self, matricula, modelo):
        self.matricula = matricula
        self.modelo = modelo
        self.disponible = True

    def alquilar(self):
        if self.disponible:
            self.disponible = False
        else:
            print(f"\nEl vehículo con matrícula {self.matricula} no se puede alquilar")
    
    def devolver(self):
        if not self.disponible:
            self.disponible = True
        else:
            print(f"\nEl vehículo con matrícula {self.matricula} no está alquilado")
    
    def __str__(self):
        return f"Vehículo(matricula={self.matricula}, modelo={self.modelo}, disponible={self.disponible})"

class Flota:

    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self,vehiculo):
        self.vehiculos.append(vehiculo)

    def alquilar_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.alquilar()
    def devolver_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.devolver()

    def __str__(self):
        return "\n".join(str(vehiculo) for vehiculo in self.vehiculos)
#Saltos de linea entre vehiculos mostrados

if __name__ == '__main__':

    flota = Flota()

    flota.agregar_vehiculo(Vehiculo("BASKD5", "Toyota Corolla"))
    flota.agregar_vehiculo(Vehiculo("DJKDJ8", "Honda Civic"))

    print("\nFlota inicial:\n")
    print(flota)

    flota.alquilar_vehiculo("BASKD5")

    print("\nMostrando la flota después de haber alquilado el Toyota:\n")
    print(flota)

    flota.devolver_vehiculo("BASKD5")

    print("\nMostrando la flota después de haber devuelto el Toyota:\n")
    print(flota)



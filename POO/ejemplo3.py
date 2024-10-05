#!/usr/bin/env python3

class CuentaBancaria:

    def __init__(self, cuenta, nombre, dinero=0):#0 será por defecto, si no le pasas ese valor
        self.cuenta = cuenta
        self.nombre = nombre
        self.dinero = dinero

    def depositar_dinero(self, dinero):

        self.dinero += dinero
        return f"\n Se han depositado {dinero} euros, actualmente tiene {self.dinero} euros"

    def retirar_dinero(self, dinero):

        if dinero > self.dinero:
            return f"No tienes suficiente dinero"
        
        self.dinero -= dinero
        return f"\n Se han retirado {dinero} euros, actualmente tiene {self.dinero} euros" 

iker = CuentaBancaria("1234567", " Iker Bermejo", 1000)
print(iker.depositar_dinero(500))
print(iker.depositar_dinero(700))
print(iker.retirar_dinero(1000))

#!/usr/bin/env python3

example = (1,[1, 2, 3],3,{'manzanas' : 1, 'peras' : 5},5) #Paréntesis=Tupla, Corchetes=listas
a, b, c, d, e = example

print(b) 

print(type(example))
#print(example[1:4]) #Ultimo numero siempre -1: de 1 al 3
#print(example[2:])

# En las tuplas no podemos realizar ningún cambio
# Si pudeo realizar operaciones con ellas almacenándolas en otras variables
#example.remove("1") #No se puede porque no se puede realizar ningún cambio
for element in example:
    print(element)


#Caso práctico base de datos con duplas, no se pudeen manipular los elementos de la tupla
db1_credential = ("Iker", "Iker123")
db2_credential = ("s4vitar", "s4vitar123")

try: 
    db1_credential[0] = "manolo"
except TypeError:
        print("No es posible cambiar el nombre de usuario (Tupla)")



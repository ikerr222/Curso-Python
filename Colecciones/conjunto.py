#!/usr/bin/env python3

#Conjuntos se definen con llaves {}

#No puede haber elementos repetidos

conjunto = {1, 2, 3}
conjunto2 = {2, 3, 4, 5, 6, 7} 

lista = [1, 5, 4, 2, 2, 2, 1, 12, 14, 14, 15]

no_repeat = list(set(lista)) #Set=conjunto, como no se puede repetir, los elimina y luego los pasa a lista otra vez
print(no_repeat)

conjunto_inter = conjunto.intersection(conjunto2) #Elementos repetidos son los que se printean
conjunto_union = conjunto.union(conjunto2) 
#difference: printea las diferencias de 2 conjuntos

print(conjunto.issubset(conjunto2)) #Es subconjunto de 2? Da igual el orden


print(conjunto_inter)
print(conjunto_union)

#conjunto.add(4)
#conjunto.add(9)

#No hay orden al añadirlos
#conjunto.update({5,7,8})
#conjunto.remove(3)
#conjunto.discard(6) #Si el elemento está lo remueve, si no lo está no arroja error

#print(conjunto)

mi_conjunto = set(range(10)) #Muy eficiente para listas/conjuntos muy grandes

print(mi_conjunto)
print(4 in mi_conjunto)
for element in mi_conjunto:
    print(element)

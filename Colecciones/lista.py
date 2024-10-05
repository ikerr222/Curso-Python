#!/usr/bin/env python3

puertos_tcp = [21, 22, 25, 80, 443, 8080, 445, 69]
nombres_tcp = ["ftp", "ssh", "smtp", "http", "https", "tcp", "tcp2", "udp"]

for puerto, nombre in zip(puertos_tcp, nombres_tcp):
          print(f"{nombre} corresponde al puerto: {puerto}")

#nombes_tcp.insert(2, "smtp") inserta en la 2 smtp, no elimina ninguno
#nombres_tcp.pop() #quitar último elemento
#nombres_tcp.clear() #Limpiar lista
#nombres_tcp.remove("smtp")

#puertos_tcp.append(1337)

#print(len(puertos_tcp))

#puertos_tcp.sort()
#puertos_tcp.reverse()

#for puerto in puertos_tcp:
#    print(f"{puerto}")

#ssh = puertos_tcp[7]

#print(ssh)

#i = 0 #Contador

#while i < len(puertos_tcp):
#    print(puertos_tcp[i])
#   i += 1

#for i, puertos in enumerate(puertos_tcp):
#    print(f"Para la posición {i+1} tenemos el puerto {puertos}")


#!/usr/bin/env python3

my_ports = []
my_ports.append(22)
my_ports.append(80)
my_ports.append(443)

my_ports.extend([84,85])
my_ports += [86,87]
my_ports = sorted(my_ports)

for port in my_ports:
    print(port)


print(f"\nLa lista tiene un total de {len(my_ports)} elementos")

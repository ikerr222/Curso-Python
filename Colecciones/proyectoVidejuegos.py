#!/usr/bin/env python3

juegos = ["Super Mario Bros", "Zelda: Breath of the wild", "Cyberpunk 2077", "Final Fantasy VII"]
tope = 500

# Géneros
generos = {
    "Super Mario Bros": "Aventura",
    "Zelda: Breath of the wild": "Aventura",
    "Cyberpunk 2077": "Rol",
    "Final Fantasy VII": "Rol"
}


#Ventas y Stock
ventas_y_stock = {
        "Super Mario Bros": (400,  200),
        "Zelda: Breath of the wild": (600,20),
        "Cyberpunk 2077": (60,120),
        "Final Fantasy VII": (924, 3)
}

#Clientes
clientes = {
    "Super Mario Bros": {"Marcelo", "Iker", "Hacker"},
    "Zelda: Breath of the wild": {"Lucia", "Iker", "Luis"},
    "Cyberpunk 2077": {"Patricia", "Lucia", "Iker", "Marcelo"},
    "Final Fantasy VII": {"Iker", "Hacker", "Luis", "Marcelo"}

}

#Sumario
def sumario(juego):
  print(f"\n[i] Resumen del juego {juego}\n")
  print(f"\t[+] Género del juego: {generos[juego]}")
  print(f"\t[+] Total de ventas para este juego: {ventas_y_stock[juego][0]}")
  print(f"\t[+] Total de stock para este juego: {ventas_y_stock[juego][1]}")
  print(f"\t[+] Clientes que han adquirido este juego: {', '.join(clientes[juego])}")

for juego in juegos:
    if ventas_y_stock[juego][0] > tope:
        sumario(juego)

ventas_totales = lambda: sum(ventas for juego, (ventas, _) in ventas_y_stock.items() if ventas_y_stock[juego][0] > tope)

print(f"\n[+] El total de ventas de todos los productos ha sido de {ventas_totales()} productos")

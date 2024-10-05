#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

root = tk.Tk()
root.title("Menu() Widget")

def abrir_archivo():
     ruta_archivo = filedialog.askopenfilename()
     print(f"\nRuta del archivo: {ruta_archivo}")
# También se podria con botones

barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

menu1 = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Menú", menu=menu1)

menu1.add_command(label="Opción 1")
menu1.add_command(label="Opción 2")

menu2 = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Extras", menu=menu2)

menu2.add_command(label="Se tensa", command=abrir_archivo)

root.mainloop()

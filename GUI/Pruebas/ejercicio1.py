#!/usr/bin/env python3

import tkinter as tk

# def accion_de_boton():
#    print(f"\nSe ha presionado el boton")

root = tk.Tk()
root.geometry('700x550')#Abrirlo en una proporcion
root.title("Text() Widget")

def get_data():
    data = text_widget.get("1.0", tk.END)
    print(f"\nDatos introducidos por el usuario: {data}\n\n")

text_widget = tk.Text(root) #Entry es para introducir texto, Text para mas texto
text_widget.pack(pady=5, padx=5, fill=tk.X) # Separacion respecto al margen

buton = tk.Button(root, text='Recoger datos de entrada', command=get_data)
buton.pack()

text_widget.pack()

#label1 = tk.Label(root, text="Mi primer label",bg="red")
#label2 = tk.Label(root, text="Mi primer label",bg="green")
#label3 = tk.Label(root, text="Mi primer label",bg="blue")

#label1.place(x=20, y=20) #Cada numero es cada pixel, relx=0.8, rely=0.2, anchor=tx.CENTER fijo
#label2.pack(fill=tk.Y, side=tk.LEFT)
#label3.grid(row=0, column=0, columnspan=2)

#button = tk.Button(root, text="Presioname", command=accion_de_boton)
#button.pack()

#label = tk.Label(root, text="Hola Mundo")
#label.pack() # Representarlo, grid() place()
root.mainloop() #Clicar, teclado etc.

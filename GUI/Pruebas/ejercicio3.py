#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("Canvas() Widget")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack(pady=15)

oval = canvas.create_oval(50, 50, 150, 150, fill="red")
rect = canvas.create_rectangle(170, 50, 330, 100, fill="green")
line = canvas.create_line(50, 250, 200, 320, width=5, fill="blue")


root.mainloop()

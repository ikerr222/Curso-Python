#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()i
root.geometry("300x200")
root.title("Frame() Widget")

frame = tk.Frame(root, bg="blue", bd=5) #Marco
frame.place(relx=0.5,rely=0.5, anchor=tk.CENTER)

label1 = tk.Label(frame, text="Label1", bg="green")
label2 = tk.Label(frame, text="Label2", bg="red")
label1.pack(fill=tk.X)
label2.pack(fill=tk.X)
root.mainloop()

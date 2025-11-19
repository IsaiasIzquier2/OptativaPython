# Eejmplo de app DNI

import tkinter as tk

ventana = tk.Tk()
ventana.title("Consulta DNI")
ventana.geometry("600x600")

imagen = tk.PhotoImage(file="T8\Ejemplos\tkinter\descargaDNI1.png")

lblImage = tk.Label(ventana, image=imagen)

lblImage.grid(column=0, row=0)

ventana.mainloop()
#Mi primer tkintr

from tkinter import*

window = Tk()
window.title("Bienvenido")
window.geometry("777x777")

contador = 0 

def renombrar():
    global contador

    contador+=1
    lbl.configure(text=contador)

lbl = Label(window, text="Mi primer label", font=("Arial",400))
lbl.grid(column=0, row= 0)

botoncico = Button(window, text="pulsame", command=renombrar)
botoncico.grid(column=0, row=1)


window.mainloop()


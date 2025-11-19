from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Bienvenido al sistema")
window.geometry("800x500")

def checkear():

    nombre = "Bienvenido"+textName.get()
    
    lista_letra = ("T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E")
    dni = textDNI.get()
    lenth = len(dni)
    numDni = int(dni[0:lenth-1])
    indice = numDni % 23

    if dni == str(numDni)+lista_letra[indice]:
        messagebox

    else:

lbBienvenido = Label(window, text="Bienveido")
lbBienvenido.grid(row=0, column=1)

lbName = Label(window, text="Nombre:")
lbName.grid(row=1, column=0)

textName = Entry(window, width=10)
textName.grid(row=1, column=1)

lbDNI = Label(window, text="DNI:")
lbDNI.grid(row=2, column=0)

textDNI = Entry(window, width=10)
textDNI.grid(row=2, column=1)

send = Button(window, text="enviar", command= checkear)
send.grid(row=3, column=1)


lbimg= PhotoImage( file="img/descargaDNI1.png")


window.mainloop()


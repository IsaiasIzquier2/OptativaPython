from tkinter import*



window = Tk()
window.title("yoquese primo estoy rayaiyo")
window.geometry("777x888")

def renombrar():

    resultado = int(txt.get()) *2


lb = Label(window, text="introduce un valor")
lb.grid(column=0,row=0)

txt = Entry(window, width=10)
txt.grid(column=2,row=0)

bt = Button(window, text="Púlsame", command=renombrar)
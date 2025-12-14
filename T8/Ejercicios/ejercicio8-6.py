# JUEGO DADOS EN TK
import random
from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title("Jueguillo del dado")
window.geometry("777x777")





firstmessage = tk.Label(window, text="¿Desea jugar al juego?")
firstmessage.grid(column=0, row=0)

gameresult = tk.Label(window, text="")
gameresult.grid(column=0, row=2)

playertext = tk.Label(window, text="Número jugador:")
playertext.grid(column=0, row=3)

machinetext = tk.Label(window, text="Número maquina:" )
machinetext.grid(column=0, row=4)

playernum = tk.Label(window, )
playernum.grid(column=1, row=3)

machinenum = tk.Label(window, )
machinenum.grid(column=1, row=4)



def game():
    
    
    numP = random.randint(1, 6)
    numM = random.randint(1, 6)

    if numP > numM:

        gameresult.configure(text="Has ganado")
        playernum.configure(text=numP)
        machinenum.configure(text=numM)

    

    elif numM > numP :

        gameresult.configure(text="Has perdido")
        playernum.configure(text=numP)
        machinenum.configure(text=numM)
    
    
    else:

        gameresult.configure(text="Empate")
        playernum.configure(text=numP)
        machinenum.configure(text=numM)
        
    
    

play = tk.Button(window, text="jugar", command=game)
play.grid(column=0, row=1)


window.mainloop()
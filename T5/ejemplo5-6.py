
# Adivina un número aleatorio del 1 al 100 en 10 intentos

import random

rnum = random.randint(1,100)

count = 0
while (count < 10):

    inum = int(input(f"Adivina un número aleatorio del 1 al 100, intento {count} de 10:"))
    count == count+1
    if (inum == rnum):

        print("FELICIDADES!!!! has adivinado el número")
        break

    elif (inum > rnum):

        print("Te has quedado corto")

    else:

        print("Te has pasado")

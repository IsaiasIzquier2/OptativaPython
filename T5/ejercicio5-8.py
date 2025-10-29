
import random
import time

rnum = random.randint(1, 10)

for i in range(3):
    
    inum = int(input(f"Adivina el número del uno al diez, intento {i+1}/3:"))

    time.sleep(1)

    if inum == rnum: 
        print("FELICIDADES!!!!!!!!!! LO HAS ADIVINADO")
        break

    else:
        print("No lo has adivinado")

else:
    print("Te has quedado sin intentos")
    
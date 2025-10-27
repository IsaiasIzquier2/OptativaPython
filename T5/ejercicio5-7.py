# Mejora el programa anterior, de forma que el usuario pueda introducir tantos números como quiera.
# El programa solicitará números al usuario hasta que introduzca la palabra “fin”. Entonces mostrará
# el mayor de todos por pantalla.

topnum = 0

while(True):
    value = input("Introduce un número:")

    if(value == "fin"):

        print(F"{topnum} es el número mayor")
        break
    
    else:
        num = int(value)
        
        if(num > topnum):
            
            topnum = num

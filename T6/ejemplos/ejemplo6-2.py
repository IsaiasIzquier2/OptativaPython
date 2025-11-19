
lista_letra = ("T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E")
dni = input("Introduzca su DNI:")
lenth = len(dni)
numDni = int(dni[0:lenth-1])
indice = numDni % 23

if dni == str(numDni)+lista_letra[indice]:
    print ("El DNI es correcto")

else:
    print ("El DNI es incorrecto")






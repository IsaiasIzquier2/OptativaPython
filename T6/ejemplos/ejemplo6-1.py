
# Ejemplo de lista

list = ["Pepe", "Luis", "Carlos", "Capo"]

list.append("Raul")
list.insert(0,"Juan")
list[0] = "Elias"

# list.remove("Luis")
# list.pop(2)

indice = list.index("Luis")

print(f"La posición del elemento")
print(f"Valores de la lista: {list}")

cont = 0

for i in list:


    print(f"El valor de indice {cont} es: {i}")

    cont = cont +1
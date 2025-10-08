
age = int(input("Indique su edad:"))
money = int(input("Indique su nomina:"))

if age >= 18 :
    if money < 1000:
        print("Le corresponde la ayuda")
    else:
        print("No cumple el requisito de la nomina")

elif money <1000:

    print("No cumple el requisito de la edad")

else:
    print("No cumple ninguno de los dos requisitos")

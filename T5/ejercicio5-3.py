num1 = int(input("Introduce un número entero"))
num2 = int(input("Introduce otro número entero"))
suma1 = 0
suma2 = 0

for n in range(num1, num2 +1 ):
    if(n % 2 == 0):
        suma1 = suma1 + n
    else:
        suma2 = suma2 + n

print(f"""
    
    Suma pares: {suma1}
    Suma impares: {suma2}

""")


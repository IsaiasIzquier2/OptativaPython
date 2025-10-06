num1 = int(input("Introduce un número entero"))
num2 = int(input("Introduce otro número entero"))
repeticiones = num2 - num1 + 1
suma = num1

for n in range(repeticiones):
    suma = suma + n
    
    
print(suma)



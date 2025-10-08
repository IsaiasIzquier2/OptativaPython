
num = int(input("Indica un número"))

if num >= 0:

    if (num % 2 == 0):

        if num < 10:

            print("Es par menor de 10")

        else:
            
            print("Es par mayor de 10")

    else:
        if num < 10:
            
            print("Es inmpar menor de 10")

        else:

            print("Es inmpar mayor de 10")



else:

    print("Es negativo")
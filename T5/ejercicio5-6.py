# Crea un programa que reciba 5 números del usuario y muestre el mayor de todos por pantalla.


# CON WHILE
# count = 0
# topnum = 0

# while (count < 5):
#     num = int(input("Introduce un número:"))

#     count == count+1

#     if (num >= num):
#         topnum = topnum + num

# else:
#     print(f"El númro más grande es el {topnum} ")

# CON FOR

nums = [2,4,78,9,5,4356,7648,34,4567,651,132]
topnum = 0

for num in nums:
    if num > topnum:
        topnum = num
else:
    print(topnum)


count = 0
list1 = []
list2 = []
list3 = []
repNum= []


while count<=9:

    if(count<5):
        
        list1.append(int(input(f"Introduce el {count+1}º número de la 1º lista:")))

        count += 1

    else:

        list2.append(int(input(f"Introduce el {count-4}º número de la 2º lista:")))

        count += 1

else:

        list3 = list1 + list2

        for i in list1:

            x = list3.count(i)

            if x >= 2:

                repNum.append(i)

                


        

print(f"Números en comun en la lista 1 y 2: {repNum}")



# 1ºINTENTO
#     list3 = list1.extend(list2)

#     for i in list1:

#         x = list3.count(i)

#         if x >= 2:

#             repNum.append(i)

# print(f"Números en comun en la lista 1 y 2:")

    

        
        
# COMPROBACIÓN LISTAS
# else: 
#     print(f"""
#             Lista 1:{list1}
#             Lista 2:{list2}
#           """)
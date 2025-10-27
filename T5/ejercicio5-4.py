

# user = "root"
# key = "toor"

# while(True):

#     imputUser = input("Usuario:")
#     imputKey = input("Clave:")

#     if((imputUser == user) and ( imputKey == key)):
#         print("Acceso permitido.")
#         break

#     else:
#         print("Acceso denegado, intetelo de nuevo.")


user = "root"
key = "toor"
count = 3

while( count >0 ):

    imputUser = input("Usuario:")
    imputKey = input("Clave:")
    

    if((imputUser == user) and ( imputKey == key)):
        print("Acceso permitido.")
        break

    else:
        count = count-1
        print(f"Acceso denegado, le quedan {count} intentos.")



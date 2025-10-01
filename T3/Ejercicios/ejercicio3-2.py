
nombre = input("Introduzca su nombre:")
numDNI = input("Introduzca su número de DNI sin letra:")
letrDNI = str.upper(input("Introduzca su letra de DNI:"))

print(f"""
      Nombre:{nombre}
      DNI:{numDNI + letrDNI}
      """)


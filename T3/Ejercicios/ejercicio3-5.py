
frase = input("Introduce frase:")
letra1 = input("Letra que quieres remplazar:")
letra2 = input("Por la que quieres remplazar:")

fraseNueva = frase.replace(letra1, letra2)
veces = frase.count(letra1)

print(f"""

Veces de remplazos: {veces}
Frase con reemplazos: {fraseNueva}

""" ) 
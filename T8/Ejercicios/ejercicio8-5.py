# JUEGO DADOS
import random


partidasGanadas = 0
partidasPerdidas = 0
partidasEmpatadas = 0
partidasJugadas = 0

def juego(a,b):
    global partidasGanadas, partidasPerdidas, partidasEmpatadas, partidasJugadas

    partidasJugadas += 1

    if a > b:

        print(f"""
                Has ganado!!
                Mi dado:{b} 
                Tu dado:{a}
        """)
        partidasGanadas += 1

    elif b > a:

        print(f"""
                Has perdido :(
                Mi dado:{b} 
                Tu dado:{a}
        """)
        partidasPerdidas += 1
    
    else:
        print(f"""
                Hemos empatado
                Los dos hemos sacado {a}
        """)
        partidasEmpatadas += 1  

juegoIntencion = input("Deseas jugar al juego? s/n:")

while True:
    dadoU = random.randint(1, 6)
    dadoM = random.randint(1, 6)
    
    if juegoIntencion == "s":
        juego(dadoU, dadoM)

        print(f"""
            {partidasJugadas}º Partida jugada
            Victorias: {partidasGanadas}
            Derrotas: {partidasPerdidas}
            Empates: {partidasEmpatadas}

            """)
        juegoIntencion = input("Deseas jugar al juego? s/n:")

    elif juegoIntencion == "n":
        print("bye")
    else:
        "Introduzca una opción valida"

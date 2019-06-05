import random
import sys
import os

#Definiendo la cantidad de jugadores y cuantas cartillas han comprado
a = int(input("Cantidad de jugadores: "))
print()
c = []
e = []
pozo = 0

for i in range (0,a):
    b = str(input("Inserte nombre jugador: "))
        
    while True:
        d = int(input("Cantidad de cartillas compradas: "))
        print()
        if d > 3:
            print("Solo puede comprar hasta 3 cartillas")
        elif 0 < d <= 3:
            d = d * 5
            break

    pozo = pozo + d

    c.append(b)
    e.append(d)

#Definiendo la eleccion de bolillas
z = int(input("Si desea una bolilla presione (1), si desea reiniciar el juego presione (2). si quiere terminar el juego presione (3): "))
bolillas_sin_jugar = []
bolillas_jugadas = []


for i in range(1,81):
    bolillas_sin_jugar.append(i)

x = 0

#Si elige un boton que no sea (1), (2), (3)
while z != 1 and z != 2 and z != 3:
        print("Debe de elegir (1), (2), (3)")
        print()
        z = int(input("Si desea otra bolilla presione (1), si desea reiniciar el juego presione (2), si quiere terminar el juego presione (3): "))

#Definiendo la accion del boton (1) elegir otra bolilla
while z == 1:
    x = x + 1
    juego = random.choice(bolillas_sin_jugar)
    bolillas_sin_jugar.remove(juego)
    bolillas_jugadas.append(juego)
    print("Cantidad de bolillas jugadas:",x)
    print("Bolilla:",juego)
    print("Bolillas que han salido: ",bolillas_jugadas)
    print()
    z = int(input("Si desea una bolilla presione (1), si desea reiniciar el juego presione (2), si quiere terminar el juego presione (3): "))
    
    #Definiendo la accion del boton (3) finalizar juego
    while z == 3:
        if x < 15:
            print("Se deben jugar al menos 15 bolillas para terminar el juego")
            print()
            z = int(input("Si desea una bolilla presione (1), si desea reiniciar el juego presione (2). si quiere terminar el juego presione (3): "))
            print()
        elif x >= 15:
            print("Pozo ganado:",pozo)
            print("Juego Finalizado")
            print()
            z = int(input("Si desea reiniciar el juego presione (2), si quiere terminar la aplicación presione(3): "))
            print()
            if z == 3:
                print("Programa finalizado")
                break

    while z != 1 and z != 2 and z != 3:
        print("Debe de elegir (1), (2), (3)")
        print()
        z = int(input("Si desea una bolilla presione (1), si desea reiniciar el juego presione (2), si quiere terminar el juego presione (3): "))

#Accion Boton (2) repeticion del programa
while z == 2:
    print()
    a = int(input("Cantidad de jugadores: "))
    print()
    c = []
    e = []
    pozo = 0

    for i in range (0,a):
        b = str(input("Inserte nombre jugador: "))
        print()
    
        while True:
            d = int(input("Cantidad de cartillas compradas: "))
            if d > 3:
                print("Solo puede comprar hasta 3 cartillas")
            elif 0 < d <= 3:
                d = d * 5
                break

    pozo = pozo + d

    c.append(b)
    e.append(d)

    z = int(input("Si desea una bolilla presione (1), si desea reiniciar el juego presione (2). si quiere terminar el juego presione (3): "))
    bolillas_sin_jugar = []
    bolillas_jugadas = []


    for i in range(1,81):
        bolillas_sin_jugar.append(i)

    x = 0

    while z != 1 and z != 2 and z != 3:
        print("Debe de elegir (1), (2), (3)")
        print()
        z = int(input("Si desea otra bolilla presione (1), si desea reiniciar el juego presione (2), si quiere terminar el juego presione (3): "))

    while z == 1:
        x = x + 1
        juego = random.choice(bolillas_sin_jugar)
        bolillas_sin_jugar.remove(juego)
        bolillas_jugadas.append(juego)
        print("Cantidad de bolillas jugadas:",x)
        print("Bolilla:",juego)
        print("Bolillas que han salido: ",bolillas_jugadas)
        print()
        z = int(input("Si desea una bolilla presione (1), si desea reiniciar el juego presione (2). si quiere terminar el juego presione (3): "))
    

        while z == 3:
            if x < 15:
                print("Se deben jugar al menos 15 bolillas para terminar el juego")
                print()
                z = int(input("Si desea una bolilla presione (1), si desea reiniciar el juego presione (2). si quiere terminar el juego presione (3): "))
                print()
            elif x >= 15:
                print("Pozo ganado:",pozo)
                print("Juego Finalizado")
                print()
                z = int(input("Si desea reiniciar el juego presione (2), si quiere terminar la aplicación presione(3): "))
                print()
            if z == 3:
                print("Programa finalizado")
                break
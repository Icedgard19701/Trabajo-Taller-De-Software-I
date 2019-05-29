import random
import sys
import os


#Definiendo la cantidad de jugadores y cuantas cartillas han comprado
a = int(input("Cantidad de jugadores: "))
c = []
e = []
pozo = 0

for i in range (0,a):
    b = str(input("Inserte nombre jugador: "))
    
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

#Definiendo la eleccion de bolillas
z = int(input("Si desea otra bolilla presione (1), si desea reiniciar el juego presione (2). si quiere terminar el juego presione (3): "))
bolillas_sin_jugar = []
bolillas_jugadas = []


for i in range(1,81):
    bolillas_sin_jugar.append(i)


while z == 1:
    juego = random.choice(bolillas_sin_jugar)
    bolillas_sin_jugar.remove(juego)
    bolillas_jugadas.append(juego)
    print("Bolilla:",juego)
    print("Bolillas que han salido: ",bolillas_jugadas)
    print()
    z = int(input("Si desea otra bolilla presione (1), si desea reiniciar el juego presione (2). si quiere terminar el juego presione (3): "))

if z == 3:
    print()

print(pozo)


#Bolillas a jugar
#for i in range(0,80):

print(c)
print(e)
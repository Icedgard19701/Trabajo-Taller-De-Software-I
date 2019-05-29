import random
import sys
import os
#import sys

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


    



    
    
    
    
    
    
#print(random.randint(0,80))

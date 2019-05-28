import random
import sys
z = input(input("Si desea otra bolilla presione (1), si desea reiniciar el juego presione (2). si quiere terminar el juego presione (3)"))

if z == 1:
    print(random.randint(0,80))
#elif z == 2:
   # restart-app
elif z == 3:
    sys.exit()
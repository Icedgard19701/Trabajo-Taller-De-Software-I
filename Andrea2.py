cant = int(input("Cantidad de jugadores: "))
c = []
e = []

for i in range (0,cant):
    b = str(input("Inserte nombre jugador: "))
    
    while True:
        car = int(input("Cantidad de cartillas compradas: "))
        if car > 3:
            print("Solo puede comprar hasta 3 cartillas")
        elif 0 < car <= 3:
            break
    c.append(b)
    e.append(car)

print("Jugadores:",c)
print("N° cartillas:",e)

import random
n = []
for i in range(0,80):
    x = print(random.choice(range(80)))
    n.append(x)  
print (n)



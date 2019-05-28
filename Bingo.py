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

print(pozo)


#Bolillas a jugar
#for i in range(0,80):

print(c)
print(e)
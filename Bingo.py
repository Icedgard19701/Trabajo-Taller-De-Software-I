a = int(input("Cantidad de jugadores: "))
c = []
e = []

for i in range (0,a):
    b = str(input("Inserte nombre jugador: "))
    
    while True:
        d = int(input("Cantidad de cartillas compradas: "))
        if d > 3:
            print("Solo puede comprar hasta 3 cartillas")
        elif 0 < d <= 3:
            break
    c.append(b)
    e.append(d)

print(c)
print(e)
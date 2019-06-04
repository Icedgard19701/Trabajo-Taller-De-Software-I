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
import sys
import os


n = []
for i in range(1, 81):
    n.append(i)

random.shuffle(n)
print ("Arrelo de 80 # desordenados",n)

print ("Codigo 1 = Mostrar nueva bolilla")
print ("Codigo 2 = Finalizar del juego")
print ("Codigo 3 = Reiniciar juego")

codigo = int (input("Ingrese codigo:"))


m=[]

while codigo == 1:
    bol = random.choice(n)
    n.remove(bol)
    m.append(bol)
    print ("Bolilla", bol)
    print ("Bolillas que ya salieron:", m)
  
    codigo = int (input("Ingrese codigo:"))


while codigo == 2: 
     print ("Has seleccionado salir")
     break






while codigo == 3:
    restart = input("\nDo you want to restart the program? [y/n] > ")
if restart == "y":
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 
else:
    print("\nThe programm will me closed...")
    sys.exit(0)

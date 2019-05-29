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
for i in range(1, 81):
    n.append(i)

random.shuffle(n)
print ("Arrelo de 80 # desordenados",n)

print ("Codigo 1 = Mostrar nueva bolilla")
print ("Codigo 2 = Finalizar del juego")
print ("Codigo 3 = Reiniciar juego")

codigo = int (input("Ingrese codigo:"))


m=[]
i = 1
while codigo == 1:
    print ("Bolilla", n[i])
    m.append (n[i])
    
    i = i+1
    codigo = int (input("Ingrese codigo:"))

















m = []
estado = False
i=1
while estado == False and i < 80:
    codigo = int (input ("Ingrese 1 para nuevo #:"))
    while codigo ==1:
        x = n[i]
        m.append(x)
        i = i +1
        print (m)

    


    m.append




m = []
for i in n:
    m.append(i)
    
print (m)




m = []
mensaje = input ("Mostrar número:")
mensaje = mensaje.lower()
estado = False 

for j in range(len(n)):
    
     if mensaje == "Si":
         estado = True
     if estado == True:
             m.append(n[j])
             print (m)
             n.remove(j)
             print (n)
             






    
 



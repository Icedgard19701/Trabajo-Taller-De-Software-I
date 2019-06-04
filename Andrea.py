n = input("Ingrese su nombre:")

while True:
    cart =int(input("¿Cuantas cartillas desea?:"))
    if cart <=3:
        print ("Puede continuar...")
        break
    else:
        print ("Ingrese nuevamente la cantidad de cartillas que desea.")
        print ("Recuerde que deben ser menor a 4 cartillas")

mensaje = input ("¿Desea saber el monto a pagar?:")

for i in mensaje:
    letra = i.lower()
    if letra == "si":
        pagar = cart * 5
        print ("El monto es:", pagar)
        break
    else:
        print ("Puede seguir")
        break








































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
             






    
 











 for i in mensaje:
         letra = i.lower()
         if letra == "Si":
             m.append(n[j])
             print (m)
             n.remove(j)
         else:
             print (n)

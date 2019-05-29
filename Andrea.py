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
















 for i in mensaje:
         letra = i.lower()
         if letra == "Si":
             m.append(n[j])
             print (m)
             n.remove(j)
         else:
             print (n)

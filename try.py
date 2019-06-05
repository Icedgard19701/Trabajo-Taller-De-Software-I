a = input("Cantidad de jugadores: ")
try:
   val = int(a)
   print("Yes input string is an Integer.")
   print("Input number value is: ", val)
except ValueError:
   print("That's not an int!")
   print("No.. input string is not an Integer. It's a string")




a = input ("Cantidad de jugadores: ")
estado = True
if (a.isdigit()):
  estado = True
  print ( "Se ingreso un numero ")
else:
  print ("Se ingreso una letra")
  while estado == False:
    a = input ("cantidad de jugadores:")
    estado = False
    if (a.isdigit()):
      estado = True
      print ( "Se ingreso un numero ")
    else:
      print ("Se ingreso una letra")  
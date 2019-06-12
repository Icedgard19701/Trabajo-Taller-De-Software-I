import random
from tkinter import*
from tkinter import ttk
from tkinter import messagebox

# Ventana principal de la aplicación
bingo = Tk()

# Dimensiones de la ventana
bingo.geometry('300x200') # anchura x altura

# fondo será gris
bingo.configure(bg = 'beige')

#Título a la ventana
raiz.title('BINGO')

# Define un botón en la parte inferior de la ventana
ttk.Button(bingo, text='Salir', command=quit).pack(side=BOTTOM)
boton1 = Button(bingo, text="Jugadores", COMMAND=#Funcion).place (x=250, y=410)

raiz.mainloop()


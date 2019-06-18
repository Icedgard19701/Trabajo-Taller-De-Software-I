import random
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage

#http://www.peremanelv.com/Pagina_Web_de_Pere_Manel/Tutoriales_files/Python%20Tkinter%20Introducci¢n%20%28Interface%20grafica%29.pdf

ventana=Tk()


#DEFINIR VARIABLES
#Bolas
z=[]
for i in range(1,81):
        z.append(i)
x=[]#bolillas sacadas

#nombre de jugadores
u=[]
c=[]
nombre= StringVar()
cartilla=StringVar()


#FUNCIONES
#VENTANA 2
def ventana2():
        ventana.withdraw() #Nos permite cerrar la ventana anterior
        segundaventana=Tk.Toplevel()
        segundaventana.geometri('350x450')
        if int(len(u))>1:
                etiqueta3 = Label(ventana, Text="Mostrar resumen:",fg="#181446",bg="#48C9B0",wraplength=300).place(x=80, y=190)
                boton6 = Button(ventana,Text="Mostrar resumen",COMMAND=resumen,activebackground="red").place(x=200, y=220)
                etiqueta4 = Label(ventana, Text="Reiniciar juego:",fg="#181446",bg="#48C9B0",wraplength=300).place(x=80, y=220)
                boton7 = Button(ventana,Text="Reiniciar juego",COMMAND=reiniciar,activebackground="red").place(x=200, y=255)
                etiqueta5 = Label(ventana,Text="Terminar juego",fg="#181446",bg="#48C9B0").place(x=80, y=290)
                boton8 = Button(ventana,Text="Terminar juego",COMMAND=finalizar,activebackground="red").place(x=200, y=290)
                etiqueta6 = Label(ventana,Text="Mostrar Pozo",fg="#181446",bg="#48C9B0").place(x=80, y=325)
                boton9 = Button(ventana,Text="Mostrar Pozo",COMMAND=mostrarpozo,activebackground="red").place(x=200, y=325)
                etiqueta7 = Label(ventana,Text="Sacar nueva bolilla" ,fg="#181446",bg="#48C9B0").place(x=80, y=360)
                boton10 = Button(ventana,Text="Sacar nueva bolilla",COMMAND=seleccionarbolilla,activebackground="red").place(x=200, y=360)
                boton11 = Button(ventana, Text="Bingo", COMMAND=ganar,activebackground="#BABC28").place(x=250, y=410)
        else:
                messagebox.showinfo("Mensaje" , "Como minimo se debe registrar 2 jugadores")


def ganar():
        if int(lent(x))>15:
                ventana3 = Tk()
                etiqueta8 = Label(ventana3, Text="FELICIDADES. Usted es el ganador del pozo",bg="#BABC28").place(x=50, y=20)
                ventana3.geometry('350x250')
                ventana3.title("Bingo")
                ventana3.config(bg="#BABC28")
                etiqueta9 = Label(ventana3, Text="Pozo Ganado",bg="#BABC28").place(x=50, y=50) 

                pozo = 0
                for i in c:
                        pozo = pozo + int(i)
                pozo = pozo*5
        else:
                messagebox.showinfo("Mensaje", "Aun no han salido las 15 bolillas")

        etiqueta10 = Label(ventana3, text=(str(pozo),"Nuevos Soles"),bg="#BABC28").place(x=180, y=50)


def resumen():
        messagebox.showinfo("Resumen", str(x))


def reiniciar():
        x.clear()
        u.clear()
        c.clear()
        z.clear()
        messagebox.showinfo("Reiniciar juego", "Juego reiniciado")


def finalizar():
        messagebox.showinfo("Finalizar juego", "Juego finalizado")
        ventana2.destroy()


def mostrarpozo():
        pozo = 0
        for i in c:
                pozo = pozo + int(i)
        pozo = pozo*5
        messagebox.showinfo("Mostrar Pozo", "El pozo es de "+ str(pozo)+" Nuevos Soles.")


def seleccionarbolilla():
        a = random.choice(z)
        x.append(a)
        z.append(a)
        messagebox.showinfo("Bolilla", "Nueva bolilla: "+str(a))

def añadirjugador():
        if int(cartilla.get())<4:
                u.append(nombre.get())
                c.append(cartilla.get())
                messagebox.showinfo("Mensaje", "Jugador agregado")
        else:
                messagebox.showinfo("Mensaje", "Solo se permite máximo 3 cartillas por jugador.")
#Borrar        
        nombre.set("")
        cartilla.set("")


def mostrarjugadores():
        messagebox.showinfo("Personas participando", str(u))


def eliminar():
        u.clear()
        c.clear()



#PRIMERA VENTANA
ventana.geometry('350x450')
ventana.title("BINGO")
etiqueta = Label(ventana, text="Bienvenidos al Bingo",bg="#48C9B0")
etiqueta.pack()
ttk.Button(ventana, text='Salir', command=ventana.destroy).pack(side=BOTTOM)


etiqueta1=Label(ventana, text="Nombre de usuario").place(x=42,y=30)
nombre_etiqueta=Entry = Entry(ventana, textvariable=nombre).place(x=180,y=30)

etiqueta2 = Label(ventana, text="Cantidad de cartillas").place(x=40,y=60)
cartilla_etiqueta = Entry(ventana, textvariable=cartilla).place(x=180,y=60)


boton2 = Button(ventana, text="Comenzar",COMMAND=ventana2, activebackground="#369A8E").place(x=70, y=130)
boton3 = Button(ventana, text="Agregar Jugador",COMMAND=añadirjugador, activebackground="#369A8E").place(x=60, y=90)
boton4 = Button(ventana, text="Mostrar Jugadores",COMMAND=mostrarjugadores, activebackground="#369A8E").place(x=180, y=90)
boton5 = Button(ventana, text="Eliminar Jugadores",COMMAND=eliminar, activebackground="#369A8E").place(x=185, y=130)


ventana.mainloop()
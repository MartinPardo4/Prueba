from tkinter import *

ventana = Tk()
ventana.title("Calculadora")

frame = Frame()
frame.pack(fill="both", expand = "True")
frame.config(bg="green")
ventana.resizable(0,0)

i = 0

def click_boton(valor):
    global i
    Texto.insert(i, valor)
    i = i + 1
def borrar():
    Texto.delete(0, END)
    i = 0
def calculo():
    operacion = Texto.get()
    resultado = eval(operacion)
    Texto.delete(0, END)
    Texto.insert(0, resultado)
    i = 0



Texto =Entry(frame, font = ("Calibri 20"))
Texto.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)


boton1 = Button(frame, text = "1", width = 5, height = 2, command = lambda: click_boton(1))
boton2 = Button(frame, text = "2", width = 5, height = 2, command = lambda: click_boton(2))
boton3 = Button(frame, text = "3", width = 5, height = 2, command = lambda: click_boton(3))
boton4 = Button(frame, text = "4", width = 5, height = 2, command = lambda: click_boton(4))
boton5 = Button(frame, text = "5", width = 5, height = 2, command = lambda: click_boton(5))
boton6 = Button(frame, text = "6", width = 5, height = 2, command = lambda: click_boton(6))
boton7 = Button(frame, text = "7", width = 5, height = 2, command = lambda: click_boton(7))
boton8 = Button(frame, text = "8", width = 5, height = 2, command = lambda: click_boton(8))
boton9 = Button(frame, text = "9", width = 5, height = 2, command = lambda: click_boton(9))
boton0 = Button(frame, text = "0", width = 13, height = 2, command = lambda: click_boton(0))

boton_borrar = Button(frame, text = "AC", width = 5, height = 2, command = lambda: borrar())
boton_parentesis1 = Button(frame, text = "(", width = 5, height = 2, command = lambda: click_boton("("))
boton_parentesis2 = Button(frame, text = ")", width = 5, height = 2, command = lambda: click_boton(")"))
boton_punto = Button(frame, text = ".", width = 5, height = 2, command = lambda: click_boton("."))

boton_div = Button(frame, text = "/", width = 5, height = 2, command = lambda: click_boton("/"))
boton_mult = Button(frame, text = "x", width = 5, height = 2, command = lambda: click_boton("*"))
boton_suma = Button(frame, text = "+", width = 5, height = 2, command = lambda: click_boton("+"))
boton_resta = Button(frame, text = "-", width = 5, height = 2, command = lambda: click_boton("-"))
boton_igual = Button(frame, text = "=", width = 5, height = 2, command = lambda: calculo())

boton1.grid(row = "2", column = "0", padx = "5", pady ="5")
boton2.grid(row = "2", column = "1", padx = "5", pady ="5")
boton3.grid(row = "2", column = "2", padx = "5", pady ="5")
boton4.grid(row = "3", column = "0", padx = "5", pady ="5")
boton5.grid(row = "3", column = "1", padx = "5", pady ="5")
boton6.grid(row = "3", column = "2", padx = "5", pady ="5")
boton7.grid(row = "4", column = "0", padx = "5", pady ="5")
boton8.grid(row = "4", column = "1", padx = "5", pady ="5")
boton9.grid(row = "4", column = "2", padx = "5", pady ="5")
boton0.grid(row = "5", column = "0", columnspan = 2, padx = "5", pady ="5")

boton_borrar.grid(row ="1", column = "3", padx = "5", pady = "5")
boton_parentesis1.grid(row = "1", column = "0", padx = "5", pady ="5")
boton_parentesis2.grid(row = "1", column = "1", padx = "5", pady ="5")
boton_punto.grid(row = "1", column = "2", padx = "5", pady ="5")

boton_div.grid(row = "2", column = "3", padx = "5", pady ="5")
boton_mult.grid(row = "3", column = "3", padx = "5", pady ="5")
boton_suma.grid(row = "4", column = "3", padx = "5", pady ="5")
boton_resta.grid(row = "5", column = "3", padx = "5", pady ="5")
boton_igual.grid(row = "5", column = "2", padx = "5", pady ="5")



ventana.mainloop()





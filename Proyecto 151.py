# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 21:24:55 2023

@author: anyta
"""

from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Ganancias del año")

Meses = Label(root)
Ganancias = Label(root)
Mes_max = Label(root)
Mes_min = Label(root)

tupla = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

tup = (1200, 2300, 3400, 4500, 5600, 6700, 7800, 8900, 9000, 10100, 11200, 12300)

Numero_max = max(tup)

Valor_indice = tup.index(Numero_max)

print(Valor_indice)

meses_max = tupla[Valor_indice]

Meses_M = "El mes en el que mas se vendió fue..." + meses_max + ". Esto fue el total de ventas " + str(Numero_max)

#----------------------------------------------------------------------------------------------------------------

Numero_min = min(tup)

Indice = tup.index(Numero_min)

print(Indice)

meses_min = tupla[Indice]

Meses_m = "El mes en el que menos se vendió fue... " + meses_min + ". Esto fue lo que se vendió en el mes " + str(Numero_min)

Meses["text"] = tupla
Ganancias["text"] = str(tup)


def Max():
    Mes_max["text"] = str(Meses_M)
    
def Min():
    Mes_min["text"] = str(Meses_m)
    
Btn = Button(root, text= "Muestra el mes con mas ganancia", command= Max)
Btn2 = Button(root, text= "Muestra el mes con menos ganancia", command= Min)

Meses.place(relx=0.5, rely=0.2, anchor=CENTER)
Ganancias.place(relx=0.5, rely=0.3, anchor=CENTER)
Btn.place(relx=0.5, rely=0.4, anchor=CENTER)
Mes_max.place(relx=0.5, rely=0.5, anchor=CENTER)
Btn2.place(relx=0.5, rely=0.6, anchor=CENTER)
Mes_min.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()
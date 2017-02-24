# -*- coding: utf-8 -*-
"""
Implementação do k-means
"""
from tkinter import *
import random as rnd
import kmeans_module as kmm
arq=open("../res/iris.2D.arff","r")
#inicialização do tkinter()
master = Tk()
master.title("Plotter em python")
cnv=Canvas(master,width=700,height=500)
cnv.pack()
esp=0
cores=['Red','Blue','Yellow','Green','Gray','#50f0da']
cnv.create_line(2,450,650,450)
cnv.create_line(2,450,2,2)
classes=[]
coords = kmm.gerar_centroides(3,4)
for i in coords:
    idx = rnd.randint(0,len(cores))
    cnv.create_rectangle(i[0],i[1],i[0]+10,i[1]+10,fill=cores[idx])

for linha in arq:
    values = linha.split(sep=',')
    x=abs(float(values[0]))*100
    y=abs(float(values[1]))*100
    cnv.create_oval(x+esp,y+esp,x+5+esp,y+5+esp)

mainloop()
    

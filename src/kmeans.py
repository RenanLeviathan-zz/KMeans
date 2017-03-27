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
btn=Button(master)
btn['text']='Recalcular'
#btn['command']=
btn.pack()
cnv.pack()
esp=0
cores=['Red','Blue','Yellow','Green','Gray','#50f0da']
cnv.create_line(2,450,650,450)
cnv.create_line(2,450,2,2)
#geraçao de centroides
coords = kmm.gerar_centroides(3,6)
points = []
#rnd.seed(7)
for i in coords:
    idx = rnd.randint(0,len(cores))
    cnv.create_rectangle(i[0],i[1],i[0]+10,i[1]+10,fill=cores[idx])

for linha in arq:
    values = linha.split(sep=',')
    x=abs(float(values[0]))*100
    y=abs(float(values[1]))*100
    points.append([x,y])
    cnv.create_oval(x+esp,y+esp,x+5+esp,y+5+esp)

for p in points:
    cd=None
    menor=1000
    for c in coords:
        d=kmm.dist_euc(p,c)
        if d < menor:
            menor=d
            cd=c
    cnv.create_line(p[0],p[1],cd[0],cd[1])
mainloop()
    

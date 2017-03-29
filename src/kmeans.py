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
btn['command']=replot
btn.pack()
cnv.pack()
esp=0
cores=['Red','Blue','Yellow','Green','Gray','#50f0da']
cr=[]
cnv.create_line(2,450,650,450)
cnv.create_line(2,450,2,2)
#geraçao de centroides
num_cent=3
coords = kmm.gerar_centroides(num_cent,4)
points = []
rnd.seed(7)
for i in coords:
    idx = rnd.randint(0,len(cores))
    cnv.create_rectangle(i[0],i[1],i[0]+10,i[1]+10,fill=cores[idx])
    cr.append(cores[idx])

for linha in arq:
    values = linha.split(sep=',')
    x=abs(float(values[0]))*100
    y=abs(float(values[1]))*100
    points.append([x,y])
    cnv.create_oval(x+esp,y+esp,x+5+esp,y+5+esp)

groups={}   
for i in range(num_cent):
    groups[i]=[]

def replot():
    i=0
    for i in range(num_cent):
        p=kmm.recalcular(groups[i])
        print(p)
        cnv.create_rectangle(p[0],p[1],p[0]+10,p[1]+10,fill=cr[i])
        i+=1
for p in points:
    cd=None
    menor=1000
    idx=0
    for c in enumerate(coords):
        d=kmm.dist_euc(p,c[1])
        if d < menor:
            menor=d
            cd=c[1]
            idx=c[0]
    groups[idx].append(p)
    cnv.create_line(p[0],p[1],cd[0],cd[1])
print(groups)
mainloop()
    

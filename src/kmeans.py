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
#geraçao de centroides
coords = kmm.gerar_centroides(3,4)
points = []
def set_centroids():
    rnd.seed(7)
    for i in coords:
        idx = rnd.randint(0,len(cores))
        cnv.create_rectangle(i[0],i[1],i[0]+10,i[1]+10,fill=cores[idx])
set_centroids()
for i in coords:
    idx = rnd.randint(0,len(cores))
    cnv.create_rectangle(i[0],i[1],i[0]+10,i[1]+10,fill=cores[idx])

for linha in arq:
    values = linha.split(sep=',')
    x=abs(float(values[0]))*100
    y=abs(float(values[1]))*100
    points.append([x,y])
    cnv.create_oval(x+esp,y+esp,x+5+esp,y+5+esp)

dists=[]
for c in coords:
    ds=sorted(kmm.dist_eucl(c,points))
    dists.append(ds)

medias = []
for d in dists:
    medias.append(kmm.media(d))

i=0
for c in coords:
    for p in points:
        if kmm.dist_euc1(c,p) <= medias[i]:
            cnv.create_oval(p[0]+esp,p[1]+esp,p[0]+5+esp,p[1]+5+esp,fill=cores[i])
            cnv.create_line(c[0],c[1],p[0],p[1])
    i+=1
b = Button(master,text="Reposicionar centroides",command=set_centroids)
b.pack()
mainloop()
    

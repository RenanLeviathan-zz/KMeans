# -*- coding: utf-8 -*-
"""
ola
"""
from tkinter import *
from random import *
arq=open("../res/iris.2D.arff","r")
#inicialização do tkinter()
master = Tk()
master.title("Plotter em python")
cnv=Canvas(master,width=700,height=500)
cnv.pack()
esp=0
cores=['Red','Blue','Yellow']
cnv.create_line(2,450,650,450)
cnv.create_line(2,450,2,2)
classes=[]
for linha in arq:
    values = linha.split(sep=',')
    x=abs(float(values[0]))*100
    y=abs(float(values[1]))*100
    classe=values[2]
    idx=0;
    if not classe in classes:
        classes.append(classe)
    if classe.find('Iris-setosa')!=-1:
        idx=0
    elif classe.find('Iris-virginica')!=-1:
        idx=1
    elif classe.find('Iris-versicolor')!=-1:
        idx=2
    cnv.create_oval(x+esp,y+esp,x+5+esp,y+5+esp,fill=cores[idx])
#gerar centroides

mainloop()
    

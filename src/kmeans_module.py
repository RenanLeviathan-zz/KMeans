# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 15:09:53 2017

@author: FACOMP
"""
import random as rnd
import math as mt
def gerar_centroides(qtd,length):
    coords=[]
    while qtd > 0:
        x=abs(rnd.randint(0,length))*100
        y=abs(rnd.randint(0,length))*100
        coord=[x,y]
        coords.append(coord)
        qtd-=1
    return coords
    
def media(lista):
    s=0
    m=0
    for l in lista:
        s+=l
    m=s/len(lista)
    return m

def dist_eucl(c,ps):
    dists=[]
    for p in ps:
        d = mt.sqrt(mt.pow(c[0]-p[0],2)+mt.pow(c[1]-p[1],2))
        dists.append(d)
    return dists

def dist_euc1(c,p):
    return mt.sqrt(mt.pow(c[0]-p[0],2)+mt.pow(c[1]-p[1],2))
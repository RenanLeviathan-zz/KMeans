# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 15:09:53 2017

@author: FACOMP
"""
import random as rnd
def gerar_centroides(qtd,length):
    coords=[]
    for i in range(0,qtd):
        x=abs(rnd.randint(0,length))*100
        y=abs(rnd.randint(0,length))*100
        coord=[x,y]
        coords.append(coord)
    return coords
    

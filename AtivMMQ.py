#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 14:07:53 2021

@author: lyliana

Dados fornecidos pelo professor
Q0
xi: (1.09,1.22,1.34,1.52,2.56,2.77)
yi: (1.62,1.99,2.56,2.11,6.17,5.9)
beta = 2.13
Q1
Equacao para ser linearizada, mencionada no enunciado:
x^2 = ( a y^2 + b y^1 ) / ( 2 + c y^1 )
Q2
x = (-4,-3,-2,0,2)
y = (-3,2,2,2,-2)
Q3
A funcao para fazer a analise harmonica estah definida no intervalo [-4.0,3.0]
Ela vale 1.0 para x em [-4.0,1.0)
e vale -1.0 para x em [1.0,3.0)
"""
xi = [1.09,1.22,1.34,1.52,2.56,2.77]
yi = [1.62,1.99,2.56,2.11,6.17,5.9]
beta = 2.13
i = 0
residuo2 = 0
for i in range(len(xi)):
    residuo2 += yi[i] - (a + b*xi[i])
    i += 1
    
print(residuo2)
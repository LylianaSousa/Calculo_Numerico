#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 17:54:18 2021

@author: lyliana
"""

import numpy as np
import random
import matplotlib.pyplot as plt

def f(x):
  np.random.seed(22447480)
  A = np.random.rand()*10 - 5
  B = np.random.rand()*3 + 3
  omega = np.random.rand()*0.4 + 0.8
  m = np.random.rand() + 0.5
  w = 0
  dif = 1
  i = 0
  while (dif > 5e-15) and (i < 20):
    w_ant = w
    w = w - (A+B*np.sin(omega*x)+(m+1)*w+0.9*np.sin(w))/(m+1+0.9*np.cos(w))
    dif = np.abs(w - w_ant)
    i = i + 1
  return w

def est_4a_derivada(funcao,x,h):
  c0 = funcao(x+2*h)
  c1 = funcao(x+h)
  c2 = funcao(x)
  c3 = funcao(x-h)
  c4 = funcao(x-2*h)
  est = (c0 - 4*c1 + 6*c2 - 4*c3 + c4)/(h**4)
  return est
"""
# Exemplo de uso:
y = f(1.3)
d = est_4a_derivada(f,1.3,0.005)
print(y)
print(d)"""

#Definindo o meu intervalo
intervalo = np.arange(-3.5, 2.301, 0.725)
fxvec = np.zeros(len(intervalo))

#Parte 0
print("\nParte 0\n")
c = 0
for i in  intervalo:
    fx = f(i)
    fxvec[c] = fx 
    c += 1
    print(f' x = {i:.6f} --- f(x) = {fx:.6f}')

#Parte 1
print("\nParte 1\n")
scont = 0
intervaloisimpson = 1.45
integralsimpson = 0
while scont < 8:
    integralsimpson += (intervaloisimpson*(fxvec[scont] + (4*fxvec[1 + scont]) + fxvec[2 + scont]))/6
    scont = scont + 2
print(f'Integral por 4-Simpson = {integralsimpson:.6f}')

#Parte 2
print("\nParte 2\n")
ntrap = 8
print('n = ', ntrap)
tcont = 0
intervaloitrapezio = 0.725
integraltrapezio = 0
while tcont < 8:
    integraltrapezio += (intervaloitrapezio*(fxvec[tcont] + fxvec[1 + tcont]))/2
    tcont = tcont + 1
print(f'Integral por n-Trapézios = {integraltrapezio:.6f}')

#Parte 3
print("\nParte 3\n")
intervaloderiv = np.arange(-3.5, 2.301, 0.01)
fxvecdev = np.zeros(len(intervaloderiv))
cdev = 0
for i in  intervaloderiv:
    fx = f(i)
    fxvecdev[cdev] = fx 
    cdev += 1
mod4dev = np.zeros(len(intervaloderiv))
for i in range(len(intervaloderiv)):
    mod4dev[i] = np.abs(est_4a_derivada(f,intervaloderiv[i],0.005))
max4dev = max(mod4dev)
print(f' máximo da quarta derivada = {max4dev:.6f}')

#Parte 4
print("\nParte 4\n")
C = (max4dev*(5.8**5))/2880
print(f'C = {C:.6f}')
    
#Parte 5
print("\nParte 5\n")
n1 = (C/(10**(-3)))**(1/4)
print(f'n1 = {n1:.0f}')
n2 = (C/(3*(10**(-5))))**(1/4)
print(f'n2 = {n2:.0f}')
 
#Parte 6
print("\nParte 6\n")
intervaloexato = np.arange(-3.5, 2.30, 2.9e-4)
fxvecexato = np.zeros(len(intervaloexato))
cexato  = 0
for i in  intervaloexato:
    fx = f(i)
    fxvecexato[cexato] = fx 
    cexato += 1

scontexato = 0
intervaloisimpsonexato = 5.8e-4
integralsimpsonexato = 0

while scontexato < 10000:
    integralsimpsonexato += (intervaloisimpsonexato*(fxvecexato[scontexato] + (4*fxvecexato[1 + scontexato]) + fxvecexato[2 + scontexato]))/6
    scontexato = scontexato + 2
print(f'Integral exata = {integralsimpsonexato:.6f}')

y = 10000
vetorerro = np.zeros(y)
n = np.array( range(y))

for i in range(y):
    k = 0
    ie = 5.8/(i+1)
    cf  = 0
    ise = 0 #que é o valor da integral
    fe = np.zeros(len(intervaloexato))
    for j in  np.arange(-3.5, 2.301, 5.8/(i+1)):
        fx = f(j)
        fe[cf] = fx 
        cf += 1
    while k < i:
        ise += (ie*(fe[i] + fe[1 + i]))/2
        k = k + 1
    vetorerro[i] = np.log(integralsimpsonexato - ise)
m = np.log(n + 1)
plt.scatter(m, vetorerro)
print(vetorerro[-1])


max4devexata = np.zeros(len(intervaloexato))
intervaloderivexata = np.zeros(len(intervaloexato))
for i in range(len(intervaloderivexata)):
    max4devexata[i] = np.abs(est_4a_derivada(f,intervaloexato[i],0.005))

maxexata = max(max4devexata)
print(f' máximo da quarta derivada exata = {maxexata:.6f}')

#plt.scatter(intervalo,fxvec)
#plt.scatter(intervaloexato, fxvecexato)

#C_T
deltaIt = np.abs(integraltrapezio - integralsimpsonexato )
CT = (((maxexata)*(5.8**3))/12)
print('CT = ', CT)

#C_S
deltaIs = np.abs(integralsimpson - integralsimpsonexato )
CS = (((maxexata)*(5.8**5))/2880)
print('CS = ', CS) 

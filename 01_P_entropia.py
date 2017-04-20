# -*- coding: utf-8 -*-
"""

"""
import math
import numpy as np
import matplotlib.pyplot as plt


'''
Dada una lista p, decidir si es una distribución de probabilidad (ddp)
0<=p[i]<=1, sum(p[i])=1.
'''
def es_ddp(p,tolerancia=10**(-5)):
	s=0
	for i in p:
		if i<0 or i>1: return False
		s=s+i
	if(round(s,5)!=1): return False
	return True

'''
Dado un código C y una ddp p, hallar la longitud media del código.
'''

def LongitudMedia(C,p):
	l=0
	for ci,pi in zip(C,p):
		l=l+(len(ci)*pi)
	return l

    
'''
Dada una ddp p, hallar su entropía.
'''
def H1(p):
	H=0
	for pi in p:
		if(pi!=0): H=H+(pi*math.log(1.0/pi,2))
	return H
'''
Dada una lista de frecuencias n, hallar su entropía.
'''
def H2(n):
	tot=sum(n)
	p=[]
	i=0
	while i < len(n):
		p.append(n[i]/tot)
		i=i+1
	H=0
	for pi in p:
		if(pi!=0): H=H+(pi*math.log(1.0/pi,2))
	return H



'''
Ejemplos
'''
C=['001','101','11','0001','000000001','0001','0000000000']
p=[0.5,0.1,0.1,0.1,0.1,0.1,0]
n=[5,2,1,1,1]

print(H1(p))
print(H2(n))
print(LongitudMedia(C,p))



'''
Dibujar H(p,1-p)
'''
x=[]
y=[]
for p in np.arange(0,1.0,0.01):
	x.append(p)
	y.append(H1([p,1-p]))
fig=plt.figure()
plt.plot(x,y,'r-',lw=2)
plt.show()
		



'''
Hallar aproximadamente el máximo de  H(p,q,1-p-q)
'''
Hmax=0
for p in np.arange(0,1.0,0.01):
	for q in np.arange(0,1.0-p,0.01):
		hh=H1([p,q,1-p-q])
		if Hmax<hh:
			Hmax=hh
print(Hmax)


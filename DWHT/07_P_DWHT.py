# -*- coding: utf-8 -*-


########################################################

import numpy as np
import matplotlib.pyplot as plt

"""
Implementar la DWHT Discrete Walsh-Hadamard Transform y su inversa
para bloques NxN 

dwht_bloque(p,HWH,N) 
idwht_bloque(p,HWH,N) 

p bloque NxN
HWH matriz de la transformación
"""

HWH8=getHWH(8);
bloque = np.array([[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1]])

#Calculo de HWH8
def reordenar(base):
	m,n = base.shape
	aux = np.zeros((m,n))
	positive = True
	cont = 0
	for i in range(m):
		for j  in range(n):
			if j==0: 
				if base[i,j]>0: positive=True
				else: positive=False 
			else:
				if positive==True and base[i,j]<0:
					cont+=1
					positive=False
				elif positive==False and base[i,j]>0:
					cont+=1
					positive=True
		aux[cont]=base[i]
		cont=0
	return aux
	
def getHWH(N):
	base = np.array([1])
	i=2
	f=N*2
	while(i<f):
		aux = np.zeros((i,i))
		n_bloque=int(i/2)
		for n1 in range(int(i/n_bloque)):
			for n2 in range (int(i/n_bloque)):
				bx1=n2*n_bloque
				bx2=bx1+n_bloque
				bz1=n1*n_bloque
				bz2=bz1+n_bloque
				if (n1==(i/n_bloque)-1) and (n2==n1): aux[bx1:bx2,bz1:bz2]=-base
				else: aux[bx1:bx2,bz1:bz2]=base
		base=aux;
		i*=2
	n_bloque=int(i/2)
	base =reordenar(base)
	HWH8=base/np.sqrt(n_bloque)
	return HWH8
"""
La matriz ya está creada adecuadamente
dado el bloque p calculamos:
HWH*p*HWH
y el resultado se multiplica por 1/sqrt(n_bloque)
se devuelve la mtrix transformada o se hace print de ella
"""
def dwht_bloque(p,HWH=HWH8,n_bloque=8):
	n = np.tensordot(np.tensordot(HWH,p,axes=([1][0])),HWH,axes=([1][0]))
	return n

"""
tenemos el bloque transformado y la matriz de transformación, obtenemos el bloque base?
"""
def idwht_bloque(p,HWH=HWH8,n_bloque=8):
	n = np.tensordot(np.tensordot(HWH,p,axes=([1][0])),HWH,axes=([1][0]))
	return n

#main: dado un blque 


print(dwht_bloque(bloque))
print(idwht_bloque(dwht_bloque(bloque)))

"""
Reproducir los bloques base de la transformación para los casos N=4,8 (Ver imágenes adjuntas)

"""
base = np.array([[1,1,1,1],
[1,1,-1,-1],
[1,-1,-1,1],
[1,-1,1,-1]])
base = base*(1/2)
N=4
i=1
#getHWH(N*i)*np.sqrt(N*i)
while i<2:
	H = base
	for row in range(i*N):
		for col in range(i*N):
			baseImage = np.tensordot(H[row], np.transpose(H[col]), 0)
			print(baseImage)
			plt.imshow(baseImage) 
			plt.xticks([])
			plt.yticks([])
			plt.show() 
	i+=1
		




# -*- coding: utf-8 -*-
"""

"""
import itertools
'''
Dada la lista L de longitudes de las palabras de un código 
r-ario, decidir si pueden definir un código.

'''
#Desigualdad de Kraft
def  kraft1(L, r=2):
	res=0.0
	for i in L:
		res=res+(1.0/r**i)
	if res>1: return False
	else: return True

'''
Dada la lista L de longitudes de las palabras de un código 
r-ario, calcular el máximo número de palabras de longitud 
máxima, max(L), que se pueden añadir y seguir siendo un código.

'''

def  kraft2(L, r=2):
	sum=0
	cont=0
	for i in L:
		if(i!=max(L)):
			aux=max(L)-i
			sum=sum+(2**aux)
		else: cont=cont+1
	res= (2**max(L))-sum
	return res-cont

'''
Dada la lista L de longitudes de las palabras de un  
código r-ario, calcular el máximo número de palabras 
de longitud Ln, que se pueden añadir y seguir siendo 
un código.
'''
#Cont es solo para descontar las palabras de esas longitudes que ya están, del total de palabras de esa longitud que puede tener el código
def  kraft3(L, Ln, r=2):
	sum=0
	cont=0
	for i in L:
		if(i!=Ln):
			aux=Ln-i
			sum=sum+(2**aux)
		else: cont=cont+1
	res=(2**Ln)-sum
	return res-cont

'''
Dada la lista L de longitudes de las palabras de un  
código r-ario, hallar un código prefijo con palabras 
con dichas longiutudes
'''
def Code(L,r=2):
	L=sorted(L)
	i_ant=0
	j=0
	res=[]
	for i in L:
		if(i!=i_ant):
			C=list(itertools.product(range(r),repeat=i))
			j=0
			for m in res:
				b=False
				while b==False:
					aux=''.join(str(z) for z in C[j])
					if aux.startswith(m): j=j+1
					else: b=True
		res.append(''.join(str(z) for z in C[j]))
		j=j+1
		i_ant=i
	return res

'''
Ejemplo
'''
L=[1,3,5,5,10,3,5,7,8,9,9,2,2,2]
print(sorted(L),' codigo final:',Code(L,3))
print(kraft1(L))

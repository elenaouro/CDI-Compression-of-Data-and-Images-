# -*- coding: utf-8 -*-


import random
import numpy.random
'''
0. Dada una codificación R, construir un diccionario para codificar m2c y otro para decodificar c2m
'''
R = [('a','0'), ('b','11'), ('c','100'), ('d','1010'), ('e','1011')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])


'''
1. Definir una función Encode(M, m2c) que, dado un mensaje M y un diccionario 
de codificación m2c, devuelva el mensaje codificado C.
'''

def Encode(M, m2c):
	C="";
	l = list(M)
	for i in l:
		C=C+m2c[i]
	return C;
''' 
2. Definir una función Decode(C, m2c) que, dado un mensaje codificado C y un diccionario 
de decodificación c2m, devuelva el mensaje original M.
'''

def isPrefix(dic):
	keys =dic.keys()
	i=0
	found=True
	while i<len(keys) and found==True:
		j=i+1
		while j<len(keys) and found==True:
			if keys[j].startswith(keys[i]):
				found=False
			j=j+1
		i=i+1
	return found

def Decode(C,c2m):
	M=""
	l = list(C)
	#Ejemplos 1 y 2
	if(isPrefix(c2m)):
		w=""
		for i in l:
			w=w+i
			x=c2m.get(w)
			if x is not None:
				M=M+x
				w=""
	#Ejemplo 3
	else:
		w=""
		for i in l:
			if i==0:
				if w!="":
					if len(w)>4:
						aux = int(len(w)/4)
						aux2 = len(w)-(aux*4)
						x=c2m.get(w[0:aux2])
						M = M+x
						j=0
						while j<aux:
							x=c2m.get(w[aux2:aux2+4])
							M=M+x
							j=j+1	
					else:
						M=M+c2m.get(w)
				w="0"
			else:
				w=w+i
		if len(w)>4:
			aux = int(len(w)/4)
			aux2 = len(w)-(aux*4)
			x=c2m.get(w[0:aux2])
			M = M+x
			j=0
			while j<aux:
				x=c2m.get(w[aux2:aux2+4])
				M=M+x
				j=j+1	
	return M

  

#------------------------------------------------------------------------
# Ejemplo 1
#------------------------------------------------------------------------

R = [('a','0'), ('b','11'), ('c','100'), ('d','1010'), ('e','1011')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])

'''
3. Generar un mensaje aleatorio M de longitud 50 con las frecuencias 
esperadas 50, 20, 15, 10 y 5 para los caracteres
'a', 'b', 'c', 'd', 'e' y codificarlo.
'''
arr=['a','b','c','d','e']
M= numpy.random.choice(arr,50,p=[0.5,0.2,0.15,0.1,0.05])
print(M)
C = Encode(M,m2c)


''' 
4. Si 'a', 'b', 'c', 'd', 'e' se codifican inicialmente con un código de bloque de 3 bits, hallar la ratio de compresión al utilizar el nuevo código.  
'''

r = (len(M)*3)/len(C)


#------------------------------------------------------------------------
# Ejemplo 2
#------------------------------------------------------------------------
R = [('a','0'), ('b','10'), ('c','110'), ('d','1110'), ('e','1111')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])

i=0
while i<20:
	l = ['a','b','c','d','e']
	le = random.randint(1,1000)
	m=''.join(random.choice(l) for i in range(le))
	c=Encode(m,m2c)
	m2=Decode(c,c2m)
	if m==m2: print("OK")
	else: print("Fail")
	i=i+1
''' 
5.
Codificar y decodificar 20 mensajes aleatorios de longitudes también aleatorios.  
Comprobar si los mensajes decodificados coinciden con los originales.

'''
#------------------------------------------------------------------------
# Ejemplo 3 
#------------------------------------------------------------------------
R = [('a','0'), ('b','01'), ('c','011'), ('d','0111'), ('e','1111')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])

ae = Encode('ae',m2c)
ae2 = Decode(ae,c2m)
if('ae'==ae2): print("OK")
else: print("Fail")

be = Encode('be',m2c)
be2 = Decode(be,c2m)
if('be'==be2): print("OK")
else: print("Fail")
''' 
6. Codificar y decodificar los mensajes  'ae' y 'be'. 
Comprobar si los mensajes decodificados coinciden con los originales.
'''







  





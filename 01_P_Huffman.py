# -*- coding: utf-8 -*-
"""

"""

#from cdi20152016Q1 import *

import heapq
import collections
import math
'''
Dada una distribucion de probabilidad, hallar un código de Huffman asociado
'''


def DFS(n,c):
	if(n[1]==[]):
		return c;
	else:
		c1=c+"0"
		codigosL= DFS(n[2],c1)
		c2=c+"1"
		codigosR=DFS(n[1],c2)
		codigos=codigosL+codigosR
		return codigos

def Huffman(p):
	q=[]
	for pr in p:
		heapq.heappush(q,(pr,[],[]))
	while len(q)>1:
		e1= heapq.heappop(q)
		e2=heapq.heappop(q)
		e=(e1[0]+e2[0],e1,e2)
		heapq.heappush(q,e)
	return DFS(q[0],"")



'''
Dada la ddp p=[0.80,0.1,0.05,0.05], hallar un código de Huffman asociado,
la entropía de p y la longitud media de código de Huffman hallado.
'''
def LongitudMedia(C,p):
	l=0
	for ci,pi in zip(C,p):
		l=l+(len(ci)*pi)
	return l

def H1(p):
	H=0
	for pi in p:
		if(pi!=0): H=H+(pi*math.log(1.0/pi,2))
	return H

p=[0.80,0.1,0.05,0.05]
Cod=Huffman(p)
print(Cod)
print(H1(p))
print(LongitudMedia(Cod,p))



'''
Dada la ddp p=[1/n,..../1/n] con n=2**8, hallar un código de Huffman asociado,
la entropía de p y la longitud media de código de Huffman hallado.
'''

n=2**8
p=[1/n for _ in range(n)]
Cod=Huffman(p)
print(Cod)
print(H1(p))
print(LongitudMedia(Cod,p))






'''
Dado un mensaje hallar la tabla de frecuencia de los caracteres que lo componen
'''
def tablaFrecuencias(mensaje):
	total = len(mensaje)
	count = collections.Counter(mensaje)
	freq={}
	for ch,cnt in count.items():
		freq[ch] = float(cnt)/float(total)
	return freq

'''
Definir una función que codifique un mensaje utilizando un código de Huffman 
obtenido a partir de las frecuencias de los caracteres del mensaje.

Definir otra función que decodifique los mensajes codificados con la función 
anterior.
'''
def DFSC(n,c):
	if(n[1]==[]): 
		d = {}
		d[n[3]]=c
		return d
	else:
		c1=c+"0"
		codigosL= DFSC(n[2],c1)
		c2=c+"1"
		codigosR=DFSC(n[1],c2)
		codigos=codigosL.copy()
		codigos.update(codigosR)
		return codigos

def HuffmanC(p):
	q=[]
	for pr in p.items():
		heapq.heappush(q,(pr[1],[],[],pr[0]))
	while len(q)>1:
		e1= heapq.heappop(q)
		e2=heapq.heappop(q)
		e=(e1[0]+e2[0],e1,e2,e1[3]+e2[3])
		heapq.heappush(q,e)
	codigo = DFSC(q[0],"")
	return codigo

def EncodeHuffman(mensaje_a_codificar):
	m2c = HuffmanC(tablaFrecuencias(mensaje))
	mensaje_codificado="";
	for c in mensaje_a_codificar:
		mensaje_codificado=mensaje_codificado+m2c[c]
	return mensaje_codificado,m2c
    

def DecodeHuffman(mensaje_codificado,m2c):
	mensaje_decodificado=""
	c2m={v: k for k, v in m2c.items()}
	w=""
	for c in mensaje_codificado:
		w=w+c
		x=c2m.get(w)
		if x is not None:
			mensaje_decodificado=mensaje_decodificado+x
			w=""
	return mensaje_decodificado


'''
Ejemplo
'''
mensaje='La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos.'
mensaje_codificado, m2c=EncodeHuffman(mensaje)
print(m2c)
mensaje_recuperado=DecodeHuffman(mensaje_codificado,m2c)
print(mensaje_recuperado)
ratio_compresion=8*float(len(mensaje))/float(len(mensaje_codificado))
print(ratio_compresion)


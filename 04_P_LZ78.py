# -*- coding: utf-8 -*-


"""
Dado un mensaje dar su codificación  usando el
algoritmo LZ78


mensaje='wabba wabba wabba wabba woo woo woo'
LZ78Code(mensaje)=[[0, 'w'], [0, 'a'], [0, 'b'], [3, 'a'], 
                   [0, ' '], [1, 'a'], [3, 'b'], [2, ' '], 
                   [6, 'b'], [4, ' '], [9, 'b'], [8, 'w'], 
                   [0, 'o'], [13, ' '], [1, 'o'], [14, 'w'], 
                   [13, 'o'], [0, 'EOF']]
  
"""

def getPos(men,dic):
	for entry in dic:
		if(men==entry[1]): return entry[0]
	return -1
	
def LZ78Code(mensaje):
	mensaje=mensaje
	dic=[]
	stepD=[1,mensaje[0]]
	dic.append(stepD)
	res=[]
	stepR =[0,mensaje[0]]
	res.append(stepR)
	i=1
	cont=2
	while i<len(mensaje):
		j=i;
		pos=0
		while(getPos(mensaje[i:j+1],dic)!=-1 and j<len(mensaje)):
			pos=getPos(mensaje[i:j+1],dic)
			j=j+1;
		stepD=[cont,mensaje[i:j+1]]
		dic.append(stepD)
		if(j<len(mensaje)):
			if(pos==0):stepR=[pos,mensaje[i]]
			else: stepR=[pos,mensaje[j]]
		else: stepR=[pos,'EOF']
		res.append(stepR)
		i=j+1
		cont=cont+1
	if res[-1][1]!='EOF': res.append([0,'EOF'])
	print(len(dic))
	print(dic)
	return res
"""
Dado un mensaje codificado con el algoritmo LZ78 hallar el mensaje 
correspondiente 

code=[[0, 'm'], [0, 'i'], [0, 's'], [3, 'i'], [3, 's'], 
      [2, 'p'], [0, 'p'], [2, ' '], [1, 'i'], [5, 'i'], 
      [10, 'p'], [7, 'i'], [0, ' '], [0, 'r'], [2, 'v'], 
      [0, 'e'], [14, 'EOF']]

LZ78Decode(mensaje)='mississippi mississippi river'
"""    
def LZ78Decode(codigo):
	dic=[]
	mensaje=''
	cont=1
	for c in codigo:
		if c[1]!='EOF':
			if c[0]==0: 
				mensaje=mensaje+c[1]
				dic.append([cont,c[1]])
				cont=cont+1
			else: 
				mensaje=mensaje+dic[c[0]-1][1]+c[1]
				dic.append([cont,dic[c[0]-1][1]+c[1]])
				cont=cont+1
		else:
			if c[0]>0:
				mensaje=mensaje+dic[c[0]-1][1]
	print(len(dic))
	return mensaje
    
i=1000000000
mensaje='a'
while(i>0):
	mensaje=mensaje+'a'
	i=i-1;

print(LZ78Code(mensaje))
'''mensaje='wabba wabba wabba wabba woo woo woo' 
mensaje_codificado=LZ78Code(mensaje)
print('Código: ',mensaje_codificado)   
mensaje_recuperado=LZ78Decode(mensaje_codificado)
print('Código: ',mensaje_codificado)   
print(mensaje)
print(mensaje_recuperado)
if (mensaje!=mensaje_recuperado):
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

mensaje='mississipi mississipi' 
mensaje_codificado=LZ78Code(mensaje)
print('Código: ',mensaje_codificado)   
mensaje_recuperado=LZ78Decode(mensaje_codificado)
print('Código: ',mensaje_codificado)   
print(mensaje)
print(mensaje_recuperado)
if (mensaje!=mensaje_recuperado):
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


mensaje='La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos.'

import time
bits_indice=12
start_time = time.clock()
mensaje_codificado=LZ78Code(mensaje)
print (time.clock() - start_time, "seconds CODE")
start_time = time.clock()
mensaje_recuperado=LZ78Decode(mensaje_codificado)
print (time.clock() - start_time, "seconds DECODE")
ratio_compresion=8*len(mensaje)/((bits_indice+8)*len(mensaje_codificado))
print(len(mensaje_codificado),ratio_compresion)
if (mensaje!=mensaje_recuperado):
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print(len(mensaje),len(mensaje_recuperado))
        print(mensaje[-5:],mensaje_recuperado[-5:])'''




    

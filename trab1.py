#!/usr/bin/python
# -*- coding: UTF-8 -*-


from random import randint
from random import choice



def main():
	
	numlinhas= 9
	numcolunas = 9


	matriz = geraMatriz(numlinhas, numcolunas)

	for i in range(numlinhas):
		print(matriz[i])	
	
	# print(len(matriz[1])

	# Média

	media(matriz, numlinhas)
	
	# Média ponderada

	print("")
	print("Média Ponderada")
	print("")
	

	for i in range(numlinhas):
		somadividendo = 0
		somadivisor= 0
		qtdelemenetoatual = 0
		elementosjasomados = []
		for j in range(len(matriz[i])):
			if matriz[i][j] in elementosjasomados:
				continue
			else:	
				for k in range(len(matriz[i])):
					if(matriz[i][j] == matriz[i][k]):
						qtdelemenetoatual += 1
				somadividendo += matriz[i][j] * qtdelemenetoatual
				somadivisor  += qtdelemenetoatual
				elementosjasomados.append(matriz[i][j])
		mediaponderadaatual = somadividendo/somadivisor
		print("A média ponderada do alternativa {} é igual a {}".format(i, mediaponderadaatual))	

	# Técnica Nominal de  Grupo

	print("")
	print("Técnica Nominal de Grupo")
	print("")

	for i in range(numlinhas):
		somaatual = 0
		for j in range(len(matriz[i])):
			somaatual += matriz[i][j]
		print("A pontuação do alternativa {} é igual a {}".format(i, somaatual))	
		if i == 0:
			maioresultado = somaatual
			maioralternativa = i 
		else:
			if somaatual > maioresultado:
				maioresultado = somaatual
				maioralternativa = i 
		
	print("")	
	print("A maior pontuação é da alternativa {} .".format(maioralternativa))	

	# Média de Windsor

	print("")
	print("Média de Windsor")
	print("")
	

	for i in range(numlinhas):
		qtddecadaelemento = []
		somadecadaelemento = []
		elementosjasomados = []
		for j in range(len(matriz[i])):
			if matriz[i][j] in elementosjasomados:
				continue
			else:	
				somadecadaelemento.append(matriz[i][j]) 
				qtddecadaelemento.append(1)
				for k in range(j + 1, len(matriz[i])):
					if(matriz[i][j] == matriz[i][k]):
						somadecadaelemento[len(somadecadaelemento) - 1] += matriz[i][k] 
						qtddecadaelemento[len(somadecadaelemento) - 1] += 1
				#somadividendo += matriz[i][j] * qtdelemenetoatual
				#somadivisor  += qtdelemenetoatual
				elementosjasomados.append(matriz[i][j])
		

		#print(sum(somadecadaelemento))
		#print(sum(qtddecadaelemento))

		#removendo menor elemento
		indexmenorelemento = qtddecadaelemento.index(min(qtddecadaelemento))
		somadecadaelemento.pop(indexmenorelemento)
		qtddecadaelemento.pop(indexmenorelemento)

		#removendo maior elemento
		indexmaiorelemento = qtddecadaelemento.index(max(qtddecadaelemento))
		somadecadaelemento.pop(indexmaiorelemento)
		qtddecadaelemento.pop(indexmaiorelemento)

		#print(somadecadaelemento)
		#print(qtddecadaelemento)

		somatotal = sum(somadecadaelemento)

		mediadewindsoratual = somatotal/len(matriz[i])
		print("A média de Windsor do alternativa {} é igual a {}".format(i, mediadewindsoratual))	


	

def geraMatriz(numlinhas, numcolunas):
	matriz = []
	for i in range(numlinhas):
		linha = []
		for j in range(numcolunas):
			achounumero = 0
			colunaatual = []
			for k in range(i):
				colunaatual.append(matriz[k][j])
			while (achounumero == 0):
				num = choice([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
				if num in colunaatual:
					continue
				else:
					achounumero = 1
			linha.append(num)
		matriz.append(linha)
	return matriz

def media(matriz, numlinhas)
	print("Média")
	print("")

	for i in range(numlinhas):
		somaatual = 0
		for j in range(len(matriz[i])):
			somaatual += matriz[i][j]
		mediaatual = somaatual/len(matriz[i])
		print("A média do alternativa {} é igual a {}".format(i, mediaatual))	



main()
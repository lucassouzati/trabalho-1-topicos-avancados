#!/usr/bin/python
# -*- coding: UTF-8 -*-


from random import randint
from random import choice



def main():
	
	numlinhas= 9
	numcolunas = 10


	matriz = geraMatriz(numlinhas, numcolunas)

	for i in range(numlinhas):
		print(matriz[i])	
	
	# print(len(matriz[1])

	# Média

	print("Média")
	print("")

	for i in range(numlinhas):
		somaatual = 0
		for j in range(len(matriz[i])):
			somaatual += matriz[i][j]
		mediaatual = somaatual/len(matriz[i])
		print("A média do criterio {} é igual a {}".format(i, mediaatual))	

	# Média ponderada

	print("")
	print("Média Ponderada")
	print("")
	

	for i in range(numlinhas):
		somaatual = 0
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
		print("A média ponderada do criterio {} é igual a {}".format(i, mediaponderadaatual))	

	# Técnica Nominal de  Grupo

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

main()
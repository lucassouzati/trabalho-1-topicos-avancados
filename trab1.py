#!/usr/bin/python
# -*- coding: UTF-8 -*-


from random import randint
from random import choice

def main():
	matriz = []
	numlinhas= 10


	for i in range(numlinhas):
		linha = []
		for j in range(10):
			linha.append(choice([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 0.0]))
		matriz.append(linha)

	print(matriz)
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
				print("")
			else:	
				for k in range(len(matriz[i])):
					if(matriz[i][j] == matriz[i][k]):
						qtdelemenetoatual += 1
				somadividendo += matriz[i][j] * qtdelemenetoatual
				somadivisor  += qtdelemenetoatual
				elementosjasomados.append(matriz[j])
		mediaponderadaatual = somadividendo/somadivisor
		print("A média ponderada do criterio {} é igual a {}".format(i, mediaponderadaatual))	

main()
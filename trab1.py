#!/usr/bin/python
#encoding: utf-8


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

	# Media

	for i in range(numlinhas):
		somaatual = 0
		for j in range(len(matriz[i])):
			somaatual += matriz[i][j]
		mediaatual = somaatual/len(matriz[i])
		print("A media do criterio {} e igual a {}".format(i, mediaatual))	

main()
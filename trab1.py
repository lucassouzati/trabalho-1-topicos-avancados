#!/usr/bin/python
# -*- coding: UTF-8 -*-


from random import randint
from random import choice



def main():
	
	numlinhas= 9
	numcolunas = 9
	vetorPesos = [1, 3, 5, 1, 3, 5, 1, 3, 5]

	matriz = geraMatriz(numlinhas, numcolunas)

	for i in range(numlinhas):
		print(matriz[i])	
	
	# print(len(matriz[1])

	# Média

	media(matriz, numlinhas)
	
	# Média ponderada

	mediaponderada(matriz, numlinhas, vetorPesos)

	# Técnica Nominal de  Grupo

	tecnicanominaldegrupo(matriz, numlinhas)

	# Média de Windsor

	mediawindsorordenando(matriz, numlinhas)

	

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

def media(matriz, numlinhas):
	print("Média")
	print("")

	for i in range(numlinhas):
		somaatual = 0
		for j in range(len(matriz[i])):
			somaatual += matriz[i][j]
		mediaatual = somaatual/len(matriz[i])
		print("A média do alternativa {} é igual a {}".format(i, mediaatual))	

def mediaponderada(matriz, numlinhas, vetorPesos):
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

def tecnicanominaldegrupo(matriz, numlinhas):
	print("")
	print("Técnica Nominal de Grupo")
	print("")

	maioresresultados = []
	maioresalternativas = []

	for i in range(numlinhas):
		somaatual = 0
		for j in range(len(matriz[i])):
			somaatual += matriz[i][j]
		print("A pontuação do alternativa {} é igual a {}".format(i, somaatual))	
		if i == 0:
			maioresultado = somaatual
			maioralternativa = i 
			maioresresultados.append(somaatual)
			maioresalternativas.append(i)
		else:
			if somaatual > maioresultado:
				maioresultado = somaatual
				maioralternativa = i 
				maioresresultados.append(somaatual)
				maioresalternativas.append(i)
			elif somaatual == maioresultado:
				maioresresultados.append(somaatual)
				maioresalternativas.append(i)
	achou = 0
	for i in range(len(maioresresultados)):
		if maioresultado == maioresresultados[i]:
			achou += 1
	if achou == 1:
		print("")	
		print("A maior pontuação é da alternativa {} .".format(maioralternativa))	
	
	else:
		#print(maioresresultados)
		#print(max(maioresresultados))
		resultado = ""
		for i in range(len(maioresresultados)):
			if(maioresresultados[i] >= maioresultado):
				resultado += "alternativa {}, ".format(maioresalternativas[i])
		print("")	
		print("As maiores pontuações são {} .".format(resultado))	



def mediadewindsor(matriz, numlinhas):
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


def mediawindsorordenando(matriz, numlinhas):
	print("")
	print("Média de Windsor")
	print("")

	for i in range(numlinhas):
		somaatual = 0.0
		matriz[i].sort()
		#print(matriz[i])
		for j in range(1, len(matriz[i]) - 1):
			#print(matriz[i][j])
			somaatual += matriz[i][j]
		mediadewindsoratual = somaatual / len(matriz[i])
		print("A média de Windsor da alternativa {} é igual a {}.".format(i, mediadewindsoratual))


def matrizConcordancia(tabela, nLinhas, nColunas, vetorPesos):
	print("")
	print("nMatriz de Concordância")
	print("")

	somaPesos = 0
	mConcordancia = []

	for x in range(len(vetorPesos)):
		somaPesos += vetorPesos[x]

	#Laço para alternativa a ser comparada
	for i in range(nLinhas):
		linha = []
		
		#Laço para o criterio a ser comparado
		for j in range(len(tabela[i])):
			#Laço para percorrer matriz
			somatorioW = 0
			for y in range(nColunas):
				if tabela[i][y] >= tabela[j][y]:
					somatorioW += vetorPesos[y]
			result = 1.0/somaPesos * somatorioW
			linha.append(round(result, 2))
			#print result
		mConcordancia.append(linha)
		print mConcordancia[i], cidades[i]

def matrizDiscordancia(tabela, nLinhas, nColunas):
	print "\nMatriz de Discordância\n"

	#Calculando a diferença entre o maior e menor valor de cada criterio
	vetorDiferencas = []

	for i in range(nLinhas):
		valoresCriterio = []
		for j in range(len(tabela[i])):
			valoresCriterio.append(tabela[j][i])
		valorMin = min(valoresCriterio)
		valorMax = max(valoresCriterio)
		result = valorMax - valorMin
		vetorDiferencas.append(result)
	#print vetorDiferencas

	#Calculando Matriz de Discordancia
	mDiscordancia = []

	#Laço para alternativa a ser comparada
	for i in range(nLinhas):
		linha = []
		#Laço para o criterio a ser comparado
		for j in range(len(tabela[i])):
			#Laço para percorrer matriz
			vetorIndices = []
			for y in range(nColunas):
				vResultante = (tabela[j][y] - tabela[i][y])/vetorDiferencas[y]
				#print vResultante
				vetorIndices.append(round(vResultante, 2))
			linha.append(max(vetorIndices))
		mDiscordancia.append(linha)
		print mDiscordancia[i], cidades[i]
	
main()
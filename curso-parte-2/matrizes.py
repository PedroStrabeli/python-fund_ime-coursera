def dimensoes(matriz):
	linhas = len(matriz)
	colunas = len(matriz[0])
	# print(str(linhas)+"X"+str(colunas))
	return linhas, colunas


def soma_matrizes(m1, m2):
	if (dimensoes(m1) == dimensoes(m2)):
		for i in range (len(m1)):
			for j in range (len(m1[i])):
				m1[i][j] = m1[i][j] + m2[i][j]
		return m1
	else:
		return False

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m3 = [[1, 2], [4, 5], [7, 8]]

# dimensoes(m1)
# dimensoes(m2)
# dimensoes(m3)
# print(soma_matrizes(m1, m2))
# print(soma_matrizes(m1, m3))


def imprime_matriz(matriz):
	for i in range(len(matriz)):
		linha = ''
		for j in range(len(matriz[i])):
			linha += str(matriz[i][j]) + " "
		print(linha.strip())

def sao_multiplicaveis(m1, m2):
	if len(m1[0]) == len(m2):
		return True
	else:
		return False

# imprime_matriz(m1)
# imprime_matriz(m2)
# imprime_matriz(m3)
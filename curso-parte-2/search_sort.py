def ordenada(lista):
	copy = lista[:]
	copy.sort()
	if lista == copy:
		return True
	return False

def busca(lista, elemento):
	for i in (range(len(lista))):
		if lista[i] == elemento:
			return i
	return False


# print(ordenada([1, 2, 3, 4]))
# print(ordenada([1, 4, 2, 3, 4]))

# print(busca([1, 2, 3], 1))
# print(busca([1, 2, 3], 4))

import random
def lista_grande(n):
	lista = []
	for i in range(n):
		lista.append(random.randint(-1000, 1000))
	return lista

def ordena(lista): #selection sort
	for i in range(len(lista)):
		menor = lista[i]
		for j in range(i, len(lista)):
			if lista[j] < menor:
				menor, lista[j] = lista[j], menor
		lista[i] = menor
	return lista


# print(lista_grande(3))
# print(lista_grande(10))
# print(lista_grande(50))
# print(lista_grande(1))
# print(ordena([3, 1, 4, 1, 6]))
# print(ordena([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))

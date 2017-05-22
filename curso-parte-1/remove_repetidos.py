def remove_repetidos(lista):
	lista.sort()
	deleteIndexes = []
	for i in range(len(lista)-1):
		if lista[i] == lista[i-1]:
			deleteIndexes.append(i) # finds out whick numbers should be erased

	fatorCorrecao = 0 # each number deleted makes the other indexes shift by 1, so we need this correction incremented over time
	for i in deleteIndexes:
		del(lista[i-fatorCorrecao])
		fatorCorrecao+=1
	return lista


# print(remove_repetidos([1, 4, 2, 3, 5, 6, 6, 64, 3, 1]))
# print(remove_repetidos([2,2,2,2,2,2,2,1,100,1,69, 69, 69, 69, 69, 69, 69, 666]))
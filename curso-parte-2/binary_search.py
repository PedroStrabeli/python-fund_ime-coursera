class Search:
	def binary_search(self, lista, x):
		primeiro = 0
		ultimo = len(lista)-1
		while primeiro <= ultimo:
			meio = (primeiro+ultimo)//2
			print(meio)
			if lista[meio]==x:
				return meio
			else:
				if lista[meio] > x:
					ultimo = meio-1
				else:
					primeiro = meio+1
		return False#-1

	def binary_search_2(self, lista, x):
		meio = (len(lista)-1)//2
		if lista[meio] == x:
			return meio
		else:
			if lista[meio]>x:
				return binary_search_2(lista[:meio], x)
			else:
				return binary_search_2(lista[meio:], x)
		return False #-1

class Ordenador:
	def bubble_sort(self, lista):
		for i in range(len(lista)-1, 0, -1):
			switched = False
			for j in range(i):
				if lista[j] > lista[j+1]:
					lista[j], lista[j+1] = lista[j+1], lista[j]
					switched = True
			print(lista)
			if not switched:
				return lista
		return lista

def bubble_sort(lista):
	o = Ordenador()
	return o.bubble_sort(lista)

def busca(lista, elemento):
	s = Search()
	return s.binary_search(lista, elemento)

# print()
# print(bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
# print()
# print(bubble_sort([1, 9, 4, 7, 6, 15, 2, 1]))

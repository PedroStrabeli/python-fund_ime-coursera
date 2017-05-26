import random
import time
import pytest
class Timer:

	def lista_aleat(self, n):
		lista = []
		for i in range(n):
			lista.append(random.randrange(1000))
		return lista
	
	def lista_aleat2(self, n):
		lista = [0 for x in range(n)]
		for i in range(n):
			lista[i]= random.randrange(1000)
		return lista

	def lista_aleat3(self, n):
		lista = [random.randrange(1000) for x in range(n)]
		return lista

class TestaTimer:
	@pytest.fixture
	def l(self):
		return Timer()

	def teste1():
		assert True

	def teste2():
		assert False

if __name__ == "__main__":
	l = Timer()
	a1 = time.time()
	l.lista_aleat(500000)
	d1 = time.time()
	print(d1-a1)
	
	a2 = time.time()
	l.lista_aleat2(500000)
	d2 = time.time()
	print(d2-a2)

	a3 = time.time()
	l.lista_aleat3(500000)
	d3 = time.time()
	print(d3-a3)

class Triangulo:
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def perimetro(self):
		return self.a + self.b + self.c

	def tipo_lado(self):
		if self.a == self.b == self.c:
			return "equilátero"
		elif self.a == self.b or self.a == self.c or self.c == self.b:
			return "isósceles"
		else:
			return "escaleno"		
			
	def retangulo(self):
		if self.a**2 == (self.b**2 + self.c**2) or self.b**2 == (self.a**2 + self.c**2) or self.c**2 == (self.b**2 + self.a**2):
			return True
		return False

	def semelhantes(self, triangle):
		t1 = [self.a, self.b, self.c]
		t1.sort()
		t2 = [triangle.a, triangle.b, triangle.c]
		t2.sort()
		if t1[0]/t2[0] == t1[1]/t2[1] == t1[2]/t2[2]:
			return True
		return False

if __name__=="__main__":
	t1 = Triangulo(1, 2, 3)
	t2 = Triangulo(2, 4, 6)
	print(t1.semelhantes(t2))

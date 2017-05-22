import math

a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))

delta = b ** 2 -(4 * a * c)

if delta < 0:
	print("esta equação não possui raízes reais")
else:
	raiz1 = (-b + math.sqrt(delta))/(2*a)
	if delta  == 0:
		print("a raiz desta equação é", raiz1)
	else: 
		raiz2 = (-b - math.sqrt(delta))/(2*a)
		if raiz1 > raiz2:
			aux = raiz1
			raiz1 = raiz2
			raiz2 = aux
		print("as raízes da equação são", raiz1, "e", raiz2)
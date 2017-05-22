import math

def calculateDelta(a, b, c):
	return b**2 - 4*a*c

# a, b, c = [int(x) for x in input("Digite os parâmetros a, b e c: ").replace(","," ").split()]

a = int(input("Digite a: "))
b = int(input("Digite b: "))
c = int(input("Digite c: "))

delta = calculateDelta(a, b, c)

if delta > 0:
	raiz1 = (-b + math.sqrt(delta))/(2*a)
	raiz2 = (-b - math.sqrt(delta))/(2*a)

	if raiz1 > raiz2:
		aux = raiz1
		raiz1 = raiz2
		raiz2 = aux

	print("as raízes da equação são", raiz1, "e", raiz2)
elif delta == 0:
	raiz = -b/(2*a)
	print("a raiz desta equação é", raiz)
elif delta < 0:
	print("esta equação não possui raízes reais")



n = int(input("Insira número: "))

crivo = list(range(2, n+1))

for item in crivo:
	i = 0
	while i < len(crivo):
		if crivo[i] % item == 0 and crivo[i] != item:
			crivo.pop(i)
		i = i + 1
if crivo[len(crivo)-1] == n:
	print("primo")
else:
	print("não primo")
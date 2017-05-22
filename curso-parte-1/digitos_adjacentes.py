n = int(input("Insira número: "))

adjacente = "nao"

while n > 0:
	u = n % 10
	n = n // 10
	if u == n % 10:
		adjacente = "sim"


print(adjacente)
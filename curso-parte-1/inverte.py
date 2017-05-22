def inverter():
	num = 666
	lista = []
	while num != 0:
		num = int(input("Digite um número: "))
		if num != 0:
			lista.append(num)
	print()
	for i in range(len(lista)):
		print(lista[-1-i])

inverter()
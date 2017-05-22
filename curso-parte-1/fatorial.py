def fatorial(n):
	if n == 0:
		return 1
	else:
		return n * fatorial(n-1)

num = 1
while num >= 0:
	num = int(input("digita algum numero, seu bosta: "))
	print(fatorial(num))
	
width = int(input("digite a largura: "))
height = int(input("digite a altura: "))

for i in range(height):
	for j in range(width):
		if i == 0 or i == height-1:
			print("#", end="")
		elif j == 0 or j == width-1:
			print("#", end="")
		else:
			print(" ", end="")
	print()
	

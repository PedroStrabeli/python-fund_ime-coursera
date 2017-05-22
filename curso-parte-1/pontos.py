import math

# x1, y1, x2, y2 = input("Insira 4 números: ").replace(",", " ").split()

# x1, y1, x2, y2 = [int(x1), int(y1), int(x2), int(y2)]
x1 = int(input("Digite x1: "))
y1 = int(input("Digite y1: "))
x2 = int(input("Digite x2: "))
y2 = int(input("Digite y2: "))

dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)

if dist >=10:
	print("longe")
elif dist < 10:
	print("perto")
else:
	print("erro")
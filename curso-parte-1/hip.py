def soma_hipotenusas(n):
	soma = 0
	isHip = False
	for i in range(1, n+1):
		j=1
		while j < i and not isHip:
			k=1
			while k <= j and not isHip:
				hip = (j**2)+(k**2)
				if (hip == (i**2)):
					isHip = True
					soma += i
				k+=1
			j+=1
		isHip=False
	return soma

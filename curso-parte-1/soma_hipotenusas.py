def é_hipotenusa(n):
	soma = 0
	for i in range(2, n+1):
		isHip = False
		j=1
		while j < i and isHip == False:
			k=1
			while k < j and isHip == False: #n**2 = #a^2 = b^2 + c^2
				if k**2+j**2 == i**2:
					isHip = True
					soma += n
				k+=1
			j+=1

	return soma

print(é_hipotenusa(25))
def maior_primo(n):
	crivo = list(range(2, n+1))

	for item in crivo:
		i = 0
		while i < len(crivo):
			if crivo[i] % item == 0 and crivo[i] != item:
				crivo.pop(i)
			i = i + 1
	return(crivo[len(crivo)-1])

def n_primos(n):
	crivo = list(range(2, n+1))

	for item in crivo:
		i = 0
		while i < len(crivo):
			if crivo[i] % item == 0 and crivo[i] != item:
				crivo.pop(i)
			i = i + 1
	return(len(crivo))

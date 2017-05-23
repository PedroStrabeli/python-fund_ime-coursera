def maiusculas(string):
	maius = ""
	for i in string:
		if ord(i) <= 90 and ord(i) >= 65:
			maius += i

	return maius


def menor_nome(lista):
	menor = lista[0].strip().capitalize()
	for i in lista:
		newI = i.strip().capitalize()
		if len(newI) < len(menor):
			menor = newI

	return menor


def conta_letras(frase, contar="vogais"):
	qte = 0
	if contar == "vogais":
		for letra in frase:
			if letra in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
				qte += 1
	elif contar == "consoantes":
		for letra in frase:
			if ((ord(letra)>=65 and ord(letra)<=90) or (ord(letra)>=97 and ord(letra)<=122)) and letra not in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
				qte += 1
	else:		
		return "vai tomar no seu cu"
	return qte

def primeiro_lex(lista):
	first = lista[0]
	for word in lista:
		if word < first:
			first = word

	return first
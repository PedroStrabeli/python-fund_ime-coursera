def fizzbuzz(n):
	fizz_str = ''
	buzz_str = ''

	if int(n) % 3 == 0:
		fizz_str = 'Fizz'
	if int(n) % 5 == 0:
		buzz_str = 'Buzz'
	print(len(fizz_str+buzz_str))
	if len(fizz_str+buzz_str) == 0:
		return n
	else:
		return fizz_str + buzz_str

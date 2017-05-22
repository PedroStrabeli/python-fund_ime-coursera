def fizzbuzzToN(n):
	if n == 0:
		return 
	#for i in list(range(n)):
	#	fizzbuzz(i)

def fizzbuzz(num):
	if num % 10 == 0:
		print(num, "- Fizz Buzz")
	elif num % 2 == 0:
		print(num, "- Fizz")
	else:
		print(num, "- Buzz")

fizzbuzzToN(10)
fizzbuzzToN(100)


def palindrome(word):
	print("Identificador de palíndromos")
	#word = input("Insira uma palavra: ")
	word = word.upper()

	for i in list(range(getHalfWordIndex(word))):
		if word[i] != word[len(word)-(i+1)]:
			return False # stops the loop and claims it's not a palyndrome
	return True # claims it's a palyndrome

def getHalfWordIndex(word):
	center = len(word)//2
	if len(word) % 2 != 0:
		center+=1
	return center


def palindrome2(word):
	print("Identificador de palíndromos")
	#word = input("Insira uma palavra: ")
	invertedWord = ""

	for letter in word:
		invertedWord = letter+invertedWord

	return word == invertedWord


def mapLetters(word):
	mapper = {}
	for i in word:
		if i in mapper:
			mapper[i]+= 1 #increments value for this key
		else:
			mapper[i] = 1 #generates new key with value 1
	return mapper


#print(mapLetters('arara'))
#print(mapLetters('arararada'))
#print(mapLetters('penis grande'))

#def areAnagrams(word1, word2):
#	return mapLetters(word1) == mapLetters(word2)


def areAnagrams(word1, word2):
	mapper1= mapLetters(word1)
	mapper2= mapLetters(word2)
	print (mapper1,mapper2)
	for key in mapper1:
		if key in mapper2 and mapper1[key] == mapper2[key]:
			mapper1[key] = 0
			mapper2[key] = 0
		else:
			return False
	for key in mapper2:
		if mapper2[key] > 0:
			return False
	return True

#print(areAnagrams('rato','ators'))
#print(areAnagrams('rato','penis'))

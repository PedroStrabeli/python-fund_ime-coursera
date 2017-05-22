def computador_escolhe_jogada(n, m):
	play = checkIfMultipleMInRange(n, m)

	if play == 0:
		#play biggest number possible
		if n > m:
			play = m
		else:
			play = n

	return play

def usuario_escolhe_jogada(n, m):
	chosen = False
	while chosen == False:
		tirar = int(input('Quantas peças você vai tirar? '))
		if tirar > n or tirar > m or tirar < 1:
			print()
			print('Oops! Jogada inválida! Tente de novo.')
			print()
		else: 
			chosen = True
	if tirar == 1:
		print('Você tirou', tirar, 'peça.')
	else:
		print('Você tirou', tirar, 'peças.')
	return tirar

def partida():
	n = int(input('Quantas peças? '))
	m = int(input('Limite de peças por jogada? '))

	pecasEmJogo = n

	vezComputador = decideFirstPlayer(n, m)

	while pecasEmJogo != 0:
		if vezComputador:
			play = computador_escolhe_jogada(pecasEmJogo, m)
			if play == 1:
				print("O computador tirou uma peça")
			else:
				print("O computador tirou", play, "peças.")

			pecasEmJogo -= play
			vezComputador = False
		else:
			pecasEmJogo -= usuario_escolhe_jogada(pecasEmJogo, m)
			vezComputador = True

		if pecasEmJogo > 1:
			print('Agora restam', pecasEmJogo, 'peças no tabuleiro.')
		elif pecasEmJogo == 1:
			print('Agora resta apenas uma peça no tabuleiro.')
		print()

	#A cada jogada a vez é alternada, portanto aqui a lógica é invertid
	if vezComputador: 
		print('Você Ganhou!')
		winner = 'u'
	elif vezComputador == False: 
		print('O Computador Ganhou!')
		winner = 'c'

	return winner

def campeonato():
	print('Voce escolheu um campeonato!')
	print()
	comp = 0
	user = 0
	for i in range(1,3+1):
		print('**** Rodada', i, '****')

		if partida() == 'c':
			comp += 1
		else:
			user += 1
	print("**** Final do campeonato! ****")
	print()
	print("Placar: Você", user, "X", comp, "Computador")


def main():
	print('Bem-vindo ao jogo do NIM! Escolha:')
	print('1 - para jogar uma partida isolada')
	print('2 - para jogar um campeonato')

	gameMode = input()

	if gameMode == '1':
		partida()
	else:
		campeonato()

def decideFirstPlayer(n, m):
	if n % (m+1) == 0:
		vezComputador = False
		print('Você começa!')
		print()
	else:
		vezComputador = True
		print('Computador começa!')
		print()

	return vezComputador

def checkIfMultipleMInRange(n, m):
	for i in range(m, 0, -1): #decreasing sequence from m (max playable number) to 0.
		print(n-1, m+1, n-1%m+1)
		if (n-i) % (m+1) == 0: #check if there is multple of m+1 and can be played
			return i

	return 0

main()


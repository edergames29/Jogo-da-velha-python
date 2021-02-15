import os
import random
#for animation
import time
os.system('clear')


def jogo():
	#-----------------------INIT-----------------#
	tabuleiro = []
	formatoTabuleiro = "-"
	for number in range(9):
	    tabuleiro.append(formatoTabuleiro)
	"""
	tabuleiro = [0,0,0,
				 0,0,0,
				 0,0,0]
	"""
	jogador = ["X","O"]
	vez = jogador[random.randint(0, 1)] #passa entre 1 e 2 perguntando quem começa o jogo
	jogo = {
		'jogadores':["X","o"]
	}
	erros=False
	ganhador=""
	jogando = True

	jogadas=0

	def menu():

		while jogando:

			mostraTabuleiro()

			posicao = input('Selecione a posicao do tabuleiro: ')
			
			tratamento(posicao)

			verifica_vitoria()

			os.system('clear')

		resultados_do_jogo()


	#---------------------SCREEN-----------------#
	def mostraTabuleiro():
		print(erros_log())

		#printado exemplo de jogo
		print("Entradas:")
		print(1,2,3)
		print(4,5,6)
		print(7,8,9)
		print("------------")
		#printando tabela do jogo
		print("Jogo:")
		print(tabuleiro[0],tabuleiro[1],tabuleiro[2])
		print(tabuleiro[3],tabuleiro[4],tabuleiro[5])
		print(tabuleiro[6],tabuleiro[7],tabuleiro[8])

		print('Press "E" for exit.')


	#------------------INPUT GETTER ---------------#
	def tratamento(pos):
		try:
			pos = int(pos) -1 # o -1 é para ficar alinhado com 1-2-3-4-5...
		except:
			return False


		colocar_no_tabuleiro(pos)
	#------------------SET INDEX-------------------#

	def colocar_no_tabuleiro(pos):
		nonlocal tabuleiro
		nonlocal jogadas

		if tabuleiro[pos] != formatoTabuleiro:
			erros_log("posição sendo usada")
			return "Erro esta posicão está sendo usada."		
		tabuleiro[pos] = vez
		jogadas = jogadas+1
		verifica_vitoria()
		trocar_jogador()
		maquina()
		print("sucess")
	#-----------------ERROS------------------------#
	def erros_log(p=False):
		nonlocal erros
		if(erros):
			t= erros
			erros = 0
			return t

		if p:
			erros = p
			print('erros')
		return f"você é o: {vez}"

	def trocar_jogador():
		nonlocal vez
		if jogando:
			if vez == jogador[0]:
				vez=jogador[1]
			else:
				vez =jogador[0]
	#-----------------CPU-------------------------#
	def maquina():
		nonlocal tabuleiro
		tamanho=0
		array_disp=[]
		for i in tabuleiro:
			if i == formatoTabuleiro:
				array_disp.append(tamanho)
			tamanho=tamanho+1
		print(array_disp)
		
		#sorteando
		if array_disp:
			sort_position = random.randint(0, len(array_disp)-1)
			extract=array_disp[sort_position]
			#animation
			maquinaAnimation()
			
			
			#jogando
			tabuleiro[extract] = vez
			print(f'a vez do bot é{vez}')
			verifica_vitoria()
			print(f'a vez do bot é{vez}')
			trocar_jogador()
			print(f'a vez do bot é{vez}')

	def maquinaAnimation(a=True):
		if a:
			espera = 0.3
			os.system("clear")
			mostraTabuleiro()
			print("pensando.")
			time.sleep(espera)
			os.system("clear")
			mostraTabuleiro()
			print("pensando..")
			time.sleep(espera)
			os.system("clear")
			mostraTabuleiro()
			print("pensando...")

	#-----------------WIN ALGORITM----------------#
	def verifica_vitoria():
		players = jogador
		pos_coluna = 0
		pos_linha = 0
		sobrando = []
		#Verifica se for velha, ele conta se entrou 9 indices diferentes do formato do tabuleiro
		#se for verdadeiro ele encerra o jogo.
		for i in tabuleiro:
			if i != formatoTabuleiro:
				sobrando.append("formatoTabuleiro")

		if(len(sobrando) == 9):
			nonlocal vez
			vez = "velha"
			pararjogo()


		#Percorre entre as linhas e colunas com X e Bola.
		for xisbol in jogador:
			#coluna ---
			if tabuleiro[0] == xisbol and tabuleiro[1] == xisbol and tabuleiro[2] == xisbol:
				pararjogo()
			if tabuleiro[3] == xisbol and tabuleiro[4] == xisbol and tabuleiro[5] == xisbol:
				pararjogo()
			if tabuleiro[6] == xisbol and tabuleiro[7] == xisbol and tabuleiro[8] == xisbol:
				pararjogo()
			#linha ---
			if tabuleiro[0] == xisbol and tabuleiro[3] == xisbol and tabuleiro[6] == xisbol:
				pararjogo()
			if tabuleiro[1] == xisbol and tabuleiro[4] == xisbol and tabuleiro[7] == xisbol:
				pararjogo()
			if tabuleiro[2] == xisbol and tabuleiro[5] == xisbol and tabuleiro[8] == xisbol:
				pararjogo()
			#Se o resultador for entre diagonais
			if tabuleiro[0] == xisbol and tabuleiro[4] == xisbol and tabuleiro[8] == xisbol:
				pararjogo()
			if tabuleiro[6] == xisbol and tabuleiro[4] == xisbol and tabuleiro[2] == xisbol:
				pararjogo()


	def pararjogo():
		nonlocal jogando
		nonlocal ganhador
		ganhador = vez
		jogando=False

	#Mostrar os resultados do jogo 
	def resultados_do_jogo():
		print("Resultados do jogo de jogo")
		print(tabuleiro[0],tabuleiro[1],tabuleiro[2])
		print(tabuleiro[3],tabuleiro[4],tabuleiro[5])
		print(tabuleiro[6],tabuleiro[7],tabuleiro[8])
		print(f"Jogadas: {jogadas}")
		print(f"Ganhador: {ganhador}")

	

	menu()

	

jogo()

# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<
''', '''
+---+
|   |
    |
    |
    |
    |
=========
''', '''
+---+
|   |
O   |
    |
    |
    |
=========
''', '''
+---+
|   |
O   |
|   |
    |
    |
=========
''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========
''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========
''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========
''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, palavra):
		self.letras_corretas = []
		self.letras_erradas = []
		self.palavra = list(palavra)
		#print(palavra)
		
	# Método para adivinhar a letra
	def guess(self, letras):
		self.letras = letras
		l_e = []
		l_c = []

		dicionario_palavra = dict(enumerate(self.palavra))

		verify = True
		self.resposta = []
		verificador = True

		while verificador == True:
			for key, value in dicionario_palavra.items():
				if value in self.letras:
					verify = False
					for a in self.letras:
						if a in self.palavra:
							while verificador == True:
								for b in self.palavra:
									if b not in self.letras:
										self.resposta.extend('_')
									elif b in self.palavra:
										if b in self.letras:
											self.resposta.extend(b)
											self.letras_corretas.extend(b)
								verificador = False
			for c in self.letras:
				if c not in self.palavra:
					self.letras_erradas.extend(c)
			verificador = False

		#print(self.resposta)
		#print('Letras erradas: ' + ' '.join((set(self.letras_erradas))))  # o set() vai embaralhar as letras, não ficará na ordem que o usuário digitou
		#print('Letras corretas: ' + ' '.join((set(self.letras_corretas))))

		# pedaço do código para aparecer o '___...___' até a primeira letra correta ser chutada
		y = []
		if verify == True:
			for i in self.palavra:
				y.extend('_')
			#print(y)
		else:
			y.extend(self.resposta)

		return self.resposta, y

	# Método para verificar se o jogo terminou
	def hangman_over(self):
		if len(set(self.letras_erradas)) >= 6 or self.palavra == self.resposta: #vamos ver porque ele não está reconhecendo esse len = 6
			terminou = True
		else:
			terminou = False
		return(terminou)
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if self.palavra == self.resposta:
			venceu = True
		else:
			venceu = False
		return venceu

	# Método para não mostrar a letra no board
	def hide_word(self):

		print('Letras erradas: ' + ' '.join((set(self.letras_erradas))))  # o set() vai embaralhar as letras, não ficará na ordem que o usuário digitou
		print('Letras corretas: ' + ' '.join((set(self.letras_corretas))))
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		x = len(set(self.letras_erradas))
		# print(x)
		if x >= 0 and x <= 6:
			if x == 0:
				print(board[1])
			elif x == 1:
				print(board[2])
			elif x == 2:
				print(board[3])
			elif x == 3:
				print(board[4])
			elif x == 4:
				print(board[5])
			elif x == 5:
				print(board[6])
			elif x == 6:
				print(board[7])


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    jogo = Hangman(rand_word())
    lista = []
    # print(lista)
    answer = jogo.guess(lista)
    print(board[0])
    print('A palavra é: '+ ' '.join(answer[1]))
    jogo.print_game_status()
    terminou = False
    #venceu = False


    while terminou == False:
        entrada = list(str(input('Digite uma letra: ')))
        #print(entrada)
        lista.extend(entrada)
        # print('letras:' +' '.join(lista))
        answer = jogo.guess(lista)
        #print(answer[1])
        #print('A palavra é: ' + ''.join(answer[0]))
        terminou = jogo.hangman_over()
        #print(terminou)
        #venceu = jogo.hangman_won()
        #print(venceu)
        #print(answer[1])
        print('\n')
        print('A palavra é: ' + ' '.join(answer[1]))
        jogo.print_game_status()
        #escondida = jogo.hide_word()
        #print(escondida)
        #print('A palavra é: ' + ' '.join(answer[1]))
        jogo.hide_word()
        #print('\n')

    if jogo.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + ''.join(jogo.palavra))

    print('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()


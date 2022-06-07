# Função Main - Execução do Programa

def main():
    # Objeto
    jogo = Hangman(rand_word())
    jogo.print_game_status()
    terminou = False
    venceu = False
    lista_letras = []
    while terminou == False or venceu == False:
        entrada = input('Digite uma letra: ')
        lista_letras = lista_letras.extend(entrada)
        answer = jogo.guess(lista_letras)
        print(answer)
        terminou = jogo.hangman_over()
        venceu = jogo.hangman_won()
        jogo.print_game_status()

    if jogo.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + jogo.palavra)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')

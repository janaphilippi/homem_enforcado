terminou = False
letras_erradas = ['s', 1, 2, 3, 4, 5]
palavra = list('melancia')
resposta = list('melanci_')

if len(letras_erradas) == 6 or palavra == resposta:
    terminou = True
else:
    terminou = False

print(terminou)

palavra =list('melancia')
letra = str(input("Digite uma letra: "))

print(palavra)
print(letra)

if letra in palavra:
    resposta = letra
else:
    resposta = '_'

print(resposta)
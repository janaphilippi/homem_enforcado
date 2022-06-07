palavra = 'janaina'

letras = 'n'

'''if letras in palavra:
    print('yes')
else:
    print('no')'''

print(dict(enumerate(palavra)))
dicionario_palavra = dict(enumerate(palavra))
print(dicionario_palavra.keys())
print(dicionario_palavra.values())

x = []
verificador = True

while verificador == True:
    for key, value in dicionario_palavra.items():
        if value == letras:
            print(key, value)
            for letra in palavra:
                if letra == letras:
                    while verificador == True:
                        for i in palavra:
                            if i != letras:
                                x.extend('_')
                            elif i == letras:
                                x.extend(letras)
                        verificador = False
    verificador = False
print(x)



# if letras in dicionario_palavra.values():



# for letras in palavra:


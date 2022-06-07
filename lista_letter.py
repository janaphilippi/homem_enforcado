palavra =list('melancia')


def guess():
    letras = list(input("Digite uma letra: "))
    #letras = ['a', 'p', 'c', 'i', 'n','x']
    letras_erradas = []
    letras_corretas = []

    #print(dict(enumerate(palavra)))
    dicionario_palavra = dict(enumerate(palavra))
    #print(dicionario_palavra.keys())
    #print(dicionario_palavra.values())


    # Verificador se letra digitada existe ou não dentro da palavra escolhida aleatóriamente
    verify = True
    resposta = []
    verificador = True

    while verificador == True:
        for key, value in dicionario_palavra.items():
            #print(key, '->',  value)
            if value in letras:
                verify = False
               # print(key, '=',  value)
                for a in letras:
                    #print(a)
                    #if a not in palavra:
                            #letras_erradas.extend(a)
                    if a in palavra:
                        #print(palavra)
                        while verificador == True:
                            for b in palavra: # esse for que faz com que as letras certas fiquem nos lugares certos
                                #print(palavra)
                                if b not in letras:
                                    resposta.extend('_')
                                elif b in palavra:
                                    #print(i)
                                    if b in letras:
                                        #print(i)
                                        resposta.extend(b)
                                        letras_corretas.extend(b)
                            verificador = False
        for c in letras:
            if c not in palavra:
                letras_erradas.extend(c)
        verificador = False

    print(resposta)
    # print(palavra)
    print('Letras erradas: ', set(letras_erradas)) # o set() vai embaralhar as letras, não ficará na ordem que o usuário digitou
    print('Letras corretas: ', set(letras_corretas))

    # pedaço do código para aparecer o '___...___' até a primeira letra correta ser chutada
    y = []
    while verify == True:
        for i in palavra:
            y.extend('_')
        print(y)
        break
    #print(palavra)

guess()
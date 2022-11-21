key = True
while key:
    entrada = input('')
    valores = entrada.split()


    numero = valores[0]
    palavra = valores[1]
    nova_palavra = ''

    if numero == '0' and palavra == '0':
        key = False
    else:

        n = palavra.find(numero)
        if n == -1:
            comparacao = ''
        else:
            comparacao = str(palavra[n])

        for i in palavra:
            if i == comparacao:
                continue
            else:
                nova_palavra += i

        try:
            print('{}'.format(int(nova_palavra)))
        except:
            print('0')









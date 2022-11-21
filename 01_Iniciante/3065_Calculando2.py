contador = 0

while True:
    i = int(input())
    if i == 0: break
    else: contador = contador + 1
    entrada = input()

    comando = ''

    for x in range(len(entrada)):
        if entrada[x].isnumeric():
            try:
                if entrada[x+1].isnumeric():
                    number = entrada[x] + entrada[x+1]
                    comando = comando + '' + str(int(number))
                elif not entrada[x-1].isnumeric():
                    comando = comando + '' + str(int(entrada[x]))
            except:
                comando = comando + '' + str(int(entrada[x]))
        else:
            comando = comando + '' + entrada[x]
    
    resultado = eval(comando)

    print('Teste {}\n{}\n'.format(contador,int(resultado)))

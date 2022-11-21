#link da Questoes -> https://www.urionlinejudge.com.br/judge/pt/problems/view/3065

contador = 0

while True:
    i = int(input())
    if i == 0: break
    else: contador = contador + 1
    entrada = input()

    numeros = []
    operacoes = []

    numeros.append(int(entrada[0]))

    for x in range(1,len(entrada)-1):
        if entrada[x].isnumeric():
            try:
                if entrada[x+1].isnumeric():
                    number = entrada[x] + entrada[x+1]
                    numeros.append(int(number))
                elif not entrada[x-1].isnumeric():
                    number = entrada[x]
                    numeros.append(int(number))
            except:
                number = entrada[x]
                numeros.append(int(number))    
        else:
            operacoes.append(entrada[x])
    
    resultado = numeros[0]

    for k in range(1,(i-1)):
        if operacoes[k-1] == '+':
            resultado = resultado + numeros[k]
        if operacoes[k-1] == '-':
            resultado = resultado - numeros[k]
        
    print(f'Teste {contador}\n{resultado}\n')


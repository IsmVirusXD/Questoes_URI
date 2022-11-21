#link da Questão -> https://www.urionlinejudge.com.br/judge/pt/problems/view/2850

while True:
    try:
        pernas = input()

        if pernas == 'esquerda':
            print('ingles')
        elif pernas == 'direita':
            print('frances')
        elif pernas == 'nenhuma':
            print('portugues')
        elif pernas == 'as duas':
            print('caiu')

    except EOFError:
        break
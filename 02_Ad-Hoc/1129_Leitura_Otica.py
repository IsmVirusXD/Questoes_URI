# link da Questoes -> https://www.urionlinejudge.com.br/judge/pt/problems/view/1129
Dic = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
}


def conversao() -> list:
    resposta = list(map(int, input().split()))
    labraba = []
    for i in resposta:
        if i <= 127:
            labraba.append('Branco')
        else:
            labraba.append('Preto')

    return labraba


while 1:
    n = int(input())
    if n == 0:
        break
    else:
        for i in range(n):
            lista = conversao()
            l = lista.count('Branco')
            if l != 1:
                print('*')
            else:
                index = lista.index('Branco')
                print(Dic[index])

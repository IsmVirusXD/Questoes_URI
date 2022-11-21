#Link da Questão -> https://www.urionlinejudge.com.br/judge/pt/problems/view/1169

n = int(input())
i = 0

while i < n:
    i += 1
    grao = 1
    soma = 1
    teste = int(input())
    j = 1
    while j < teste:
        grao = grao * 2
        soma += grao
        j += 1

    peso = (soma/12)/1000

    print('{} kg'.format(int(peso)))

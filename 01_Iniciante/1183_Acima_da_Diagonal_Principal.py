#link da questao -> https://www.urionlinejudge.com.br/judge/pt/problems/view/1183
matriz = []
soma = 0
unidade = 0
operacao = input()

for l in range(0,12):
    lista = []
    for c in range(0,12):
        n = float(input())
        lista.append(n)
        if l < c:
            soma += n
            unidade += 1
    matriz.append(lista)


if operacao == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format((soma/unidade)))
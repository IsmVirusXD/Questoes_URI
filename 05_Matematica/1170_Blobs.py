#link da Questão -> https://www.urionlinejudge.com.br/judge/pt/problems/view/1170


casos = int(input())
i = 0

while i < casos:
    i += 1
    dias = 0
    comida = float(input())
    while comida > 1.0:
        comida = (comida)/2
        dias += 1

    print('{} dias'.format(dias))


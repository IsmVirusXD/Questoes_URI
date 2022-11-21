#link da Questoes -> https://www.urionlinejudge.com.br/judge/pt/problems/view/1708
from math import trunc

valores = input().split()
X, Y = int(valores[0]), int(valores[1])

volta = 0
tempo_total_X = 0
tempo_total_Y = 0
i = 1

while True:
    tempo_total_X = i * X
    tempo_total_Y = i * Y
    velocidade = tempo_total_Y - tempo_total_X
    if velocidade >= Y:
        break
    i += 1

print('{}'.format(i))
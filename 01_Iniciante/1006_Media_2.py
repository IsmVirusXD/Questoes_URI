# Link da Questão -> https://www.urionlinejudge.com.br/judge/pt/problems/view/1006

A = float(input())
B = float(input())
C = float(input())

Pa = 2
Pb = 3
Pc = 5

MEDIA = ((A * Pa) + (B * Pb) + (C * Pc))/(Pa + Pb + Pc)

print('MEDIA = {:.1f}'.format(MEDIA))
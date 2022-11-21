#Link da Questão -> https://www.urionlinejudge.com.br/judge/pt/problems/view/1047
from math import fabs

def convertor(hora, min):
    hora = int(hora)
    min = int(min)
    min_Total = (hora * 60) + min
    return min_Total

valor = input('')
tempo = valor.split()

min1 = convertor(tempo[0], tempo[1])
min2 = convertor(tempo[2], tempo[3])

duracao = min2 - min1

if duracao == 0:
    horas = 24
    minutos = 0

elif duracao < 0:
    horas = 23 + int(duracao / 60)
    minutos = -1 * int(duracao % 60)
    minutos = fabs(minutos)

else:
    horas = int(duracao / 60)
    minutos = int(duracao % 60)
    minutos = fabs(minutos)

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas, int(minutos)))
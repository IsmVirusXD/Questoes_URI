# Link da Questão -> https://www.urionlinejudge.com.br/judge/pt/problems/view/1061
from math import trunc


def dia():
    entrada = input()
    dia = entrada.split()
    return dia[1]


def hora():
    entrada = input()
    hora = entrada.split(" : ")
    return hora


def conversao(dia, horas, minutos, segundos):
    d = int(dia) * 86400
    h = int(horas) * 3600
    m = int(minutos) * 60
    s = int(segundos)
    seg_total = d + h + m + s
    return seg_total


def regressao(total_seg):
    result = []
    sub = 0
    d = total_seg / 86400
    result.append(trunc(d))
    sub += trunc(d) * 86400
    h = (total_seg - sub) / 3600
    result.append(trunc(h))
    sub += trunc(h) * 3600
    m = (total_seg - sub) / 60
    result.append(trunc(m))
    sub += trunc(m) * 60
    s = total_seg - sub
    result.append(trunc(s))
    return result


d1 = dia()
h1 = hora()
d2 = dia()
h2 = hora()

seg_total_hora1 = conversao(d1, h1[0], h1[1], h1[2])
seg_total_hora2 = conversao(d2, h2[0], h2[1], h2[2])
total = seg_total_hora2 - seg_total_hora1

final = regressao(total)

print("{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)".format(final[0], final[1], final[2], final[3]))

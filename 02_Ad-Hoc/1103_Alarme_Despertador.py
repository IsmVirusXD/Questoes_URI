#link da Questoes -> https://www.urionlinejudge.com.br/judge/pt/problems/view/1103
from math import fabs
key = True

while key:
    try:
        valor = input('')

        tempo = valor.split()

        h1 = int(tempo[0])
        m1 = int(tempo[1])
        h2 = int(tempo[2])
        m2 = int(tempo[3])

        if h1 == 0 and m1 == 0 and h1 == 0 and m2 == 0:
            key = False
        else:


            mt1 = (h1 * 60) + m1
            mt2 = (h2 * 60) + m2

            if mt1 < mt2:
                min_total = fabs(mt2 - mt1)
            else:
                min_total = 1440 - fabs(mt1 - mt2)

            print("{}".format(int(min_total)))

    except EOFError:
        key = False
        break


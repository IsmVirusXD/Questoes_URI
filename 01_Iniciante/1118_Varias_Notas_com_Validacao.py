#link da Questão: https://www.urionlinejudge.com.br/judge/pt/problems/view/1118

key = True

def validacao():
    while True:
        nota = float(input())
        if 0 <= nota <= 10.0:
            return nota
        else:
            print('nota invalida')

def key_set():
    while True:
        i = input('novo calculo (1-sim 2-nao)\n')

        if i == '2':
            return False
        elif i == '1':
            return True

while key:
    nota1 = validacao()
    nota2 = validacao()

    media = (nota1 + nota2)/2

    print('media = {:.2f}'.format(media))
    key = key_set()




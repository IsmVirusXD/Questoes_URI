#link da Questão: https://www.urionlinejudge.com.br/judge/pt/problems/view/1168

n = int(input())
i = 0

led = {
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6,
    '0': 6
}

while n > i:
    i += 1
    soma = 0
    palavras = input()
    for x in palavras:
        soma += led[x]

    print('{} leds'.format(soma))



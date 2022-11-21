#link da Questão: https://www.beecrowd.com.br/judge/pt/problems/view/1161

def fatorial(x : str):
    valor = int(x) + 1
    fatorial = 1
    for numero in range(1, valor):
        fatorial = fatorial * numero
    return fatorial

while True:
    try:
        x, y = input().split()
        print((fatorial(x)+fatorial(y)))

    except EOFError:
        break


key = True
celulas = [100, 50, 20, 10, 5, 2, 1]


def contagem(valor: int, celula: int) -> int:
    contador = 0
    while True:
        if (valor - celula) <= -1:
            return contador
        else:
            contador += 1
            valor = valor - celula

while(key):
    valor = input()
    try:
        if valor == '':
            key = False
        else:
            valor = int(valor)
            print(str(valor))
            for i in celulas:
                contador = 0
                contador = contagem(valor, i)
                print("{} nota(s) de R$ {},00".format(contador, i))
                valor = valor - (i * contador)

    except EOFError:
        key = False



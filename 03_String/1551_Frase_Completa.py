# Link da Questão: https://www.beecrowd.com.br/judge/pt/problems/view/1551
import string


def contagem(texto: str) -> int:
    num = 0
    conteudo = list(string.ascii_lowercase)
    for i in range(0, 26):
        if -1 != texto.find(conteudo[i]):
            num = num + 1

    return num


if __name__ == '__main__':
    N = int(input())

    for _ in range(0, N):
        texto = input()
        qtd = contagem(texto)

        if qtd == 26:
            print("frase completa")
        elif qtd >= 13:
            print("frase quase completa")
        else:
            print("frase mal elaborada")

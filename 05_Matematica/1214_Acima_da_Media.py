#Link da Questão -> https://www.urionlinejudge.com.br/judge/pt/problems/view/1214
def checagem(Valor : [], N: int, Media : int) -> int:
    contagem = 0
    for i in Valor:
        if i > Media:
            contagem += 1
    
    return contagem/N * 100

def media(Valor : [], I : int) -> int:
    soma = 0
    for i in Valor:
        soma += i
    media = soma/I
    return media

C = int(input())


for i in range(C):
    Soma = 0
    Outros = list(map(int, input().split()))
    N = Outros[0]
    Outros.remove(N)

    valor = checagem(Outros,N,media(Outros,N))
    
    print(f'{valor:.3f}%')

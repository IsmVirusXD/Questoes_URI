#link da Quesstão -> https://www.urionlinejudge.com.br/judge/pt/problems/view/2963

candidatos = int(input())

carlos = 0
votos = 0
oponentes = 0
i = 0

while i < candidatos:
    votos = int(input())

    if i == 0:
        carlos = votos
    elif oponentes <= votos:
        oponentes = votos
    i += 1

if oponentes > carlos:
    print("N")
else:
    print("S")




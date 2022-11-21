#link da Questão -> https://www.beecrowd.com.br/judge/pt/problems/view/3342

N = int(input())

branca = True
b = 0
p = 0

for l in range(N):
    for c in range(N):
        if branca:
            b += 1
            branca = False
        else:
            p += 1
            branca = True

print(f'{b} casas brancas e {p} casas pretas')
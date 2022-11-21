#link da Questao -> https://www.urionlinejudge.com.br/judge/pt/problems/view/2160

nomes = input()

i = 0

for letter in nomes:
    i += 1

if i > 80:
    print("NO")
else:
    print("YES")
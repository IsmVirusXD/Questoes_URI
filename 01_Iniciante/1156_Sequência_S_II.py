#link da Questão -> https://www.beecrowd.com.br/judge/pt/problems/view/1156
s = 1
for n in range(2,21):
    s += (2*n - 1)/(2**(n-1))

print('{:.2f}'.format(s))
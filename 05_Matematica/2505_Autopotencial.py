#link da Questoes -> https://www.urionlinejudge.com.br/judge/pt/problems/view/2505


i = int(input())
valor = pow(i,i)

L = str(i)

palavra = str(valor)

if palavra.endswith(L):
    print('SIM')
else:
    print('NAO')
#Link da Questão -> https://www.urionlinejudge.com.br/judge/pt/problems/view/1929

def checagem(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False

vetor = input()
valores = vetor.split()

A = int(valores[0])
B = int(valores[1])
C = int(valores[2])
D = int(valores[3])

respA = checagem(A, B, C)
respB = checagem(A, B, D)
respC = checagem(A, C, D)
respD = checagem(B, C, D)

if respA: print('S')
elif respB: print('S')
elif respC: print('S')
elif respD: print('S')
else: print('N')
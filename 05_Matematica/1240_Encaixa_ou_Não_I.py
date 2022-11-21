#link da Questão: https://www.beecrowd.com.br/judge/pt/problems/view/1240

N = int(input())

for i in range(N):
    A, B = input().split()
    cont = 0

    try:
        A.index(B)
        A = A[::-1]
        B = B[::-1]

        if len(B) == 1 and B[0] == A[0]:
            cont = 1

        else:
            for i in range(0, len(B)):
                if A[i] != B[i] or B[i] == IndexError:
                    cont = 0
                else:
                    cont += 1

        if cont == (len(B)):
            print('encaixa')
        else:
            print('nao encaixa')
    except:
        print('nao encaixa')


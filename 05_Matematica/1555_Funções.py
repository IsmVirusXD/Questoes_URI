#link da questão: https://www.beecrowd.com.br/judge/pt/problems/view/1555

rafael = lambda x, y : (3*x)**2 + y**2
beto   = lambda x, y : 2*(x)**2 + (5*y)** 2
carlos = lambda x, y : -100*x + y**3

testes = int(input())

for i in range(testes):
    x, y = input().split()
    x = int(x)
    y = int(y)
    R = rafael(x, y)
    B = beto(x, y)
    C = carlos(x, y)

    maior = max(R, B, C)

    if R == maior : print('Rafael ganhou')
    elif B == maior : print('Beto ganhou')
    else : print('Carlos ganhou')


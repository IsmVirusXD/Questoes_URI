#link da Questão -> https://www.beecrowd.com.br/judge/pt/problems/view/2632
from math import fabs

Spells = {
    'fire'  : [200, 20, 30, 50],
    'water' : [300, 10, 25, 40],
    'earth' : [400, 25, 55, 70],
    'air'   : [100, 28, 38, 60]
}

Testes = int(input())

def danoMagia (tipo:str) -> None:
    Dano = Spells[tipo]
    print(Dano[0])

def acerto (w : int, h : int, x0 : int, y0 : int, x : int, y : int, raio : int) -> bool:
    X_inimigo = w + x0
    Y_inimigo = h + y0

    diferença_X = X_inimigo - x
    diferença_Y = Y_inimigo - y

    print(diferença_Y)
    print(diferença_X)
    print(raio)

    if diferença_X >= raio or diferença_Y >= raio:
        
        return True
    else:
        return False






for i in range(Testes):
    W, H, X0, Y0 = list(map(int, input().split()))
    magia, *resto = input().split()
    nivel, CX, CY = list(map(int, resto))

    k = Spells[magia]
    raio = k[nivel]

    acertou = acerto(W,H,X0,Y0,CX,CY,raio)
    if acertou:
        danoMagia(magia)
    else:
        print('0')
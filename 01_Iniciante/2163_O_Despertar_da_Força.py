#link da Questão -> https://www.urionlinejudge.com.br/judge/pt/problems/view/2163

def aredores(matriz,x,y):
    try:
        if matriz[x][y+1] == '7' and matriz[x][y-1] == '7':
            if matriz[x+1][y] == '7' and matriz[x-1][y] == '7':
                if matriz[x+1][y+1] == '7' and matriz[x-1][y-1] == '7':
                    if matriz[x-1][y+1] == '7' and matriz[x+1][y-1] == '7':
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    except:
        return False


i = 0
coordenadas = 'teste'
valores = input()
numeros = valores.split()

linhas = int(numeros[0])
coluna = int(numeros[1])

key = False

matriz = []

if 3 <= linhas and coluna <= 1000:
    while i < linhas:
        valores = input()
        numeros = valores.split()
        matriz.append(numeros)
        i += 1

    for l in range(0, linhas):
        for c in range(0, coluna):
            if matriz[l][c] == '42':
                key = aredores(matriz, l, c)
                coordenadas = str(l+1) + ' ' + str(c+1)
                break
        if key:
            break

    if key == False:
        print('0 0')
    else:
        print(coordenadas)

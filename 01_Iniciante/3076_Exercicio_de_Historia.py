# Link da Questão -> https://www.urionlinejudge.com.br/judge/pt/problems/view/3076

while (1):
    try:
        entrada = int(input())
        if entrada % 100 == 0:
            seculo = (entrada//100)
        else:
            seculo = (entrada//100) + 1
        
        print(f'{seculo}')
        
    except EOFError:
        break
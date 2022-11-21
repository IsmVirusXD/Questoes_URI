#link da Questão: https://www.beecrowd.com.br/judge/pt/problems/view/1049

seletor = input()

if seletor == 'vertebrado':
    seletor = input()

    if seletor == 'ave':
        seletor = input()
        if seletor == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        seletor = input()
        if seletor == 'herbivoro':
            print('vaca')
        else:
            print('homem')

else:
    seletor = input()
    if seletor == 'inseto':
        seletor = input()
        if seletor == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        seletor = input()

        if seletor == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')

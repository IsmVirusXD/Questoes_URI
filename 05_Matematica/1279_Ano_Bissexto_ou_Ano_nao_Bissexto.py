# Link da Questão: https://www.beecrowd.com.br/judge/pt/problems/view/1279


# Ano Bissexto -> Divisivel por 4 e não é divisivel por 100 -> This is an ordinary year
# Ano Huluculu -> Dibisíveis por 15 -> this is huluculu festival Year.
# Ano Bulukulu -> Divisiveis por 55 desde que sejam bissexto -> This is bukulu festival year

def check_Bissexto(ano: int) -> bool:
    if ((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)):
        return True
    else:
        return False


def check_Huluculu(ano: int) -> bool:
    if (ano % 15 == 0):
        return True
    else:
        return False


def check_Bulukulu(ano: int) -> bool:
    if (ano % 55 == 0):
        return True
    else:
        return False


key = True

while key:
    try:
        ano = int(input())
        ordinary = True

        bissexto = check_Bissexto(ano)
        hulukulu = check_Huluculu(ano)
        bulukulu = check_Bulukulu(ano)

        if(bissexto):
            ordinary = False
            if(hulukulu):
                if(bulukulu):
                    print("This is leap year.")
                    print("This is huluculu festival year.")
                    print("This is bulukulu festival year.\n")
                else:
                    print("This is leap year.")
                    print("This is huluculu festival year.\n")
            else:
                print("This is leap year.")


        if(ordinary):
            print("This is an ordinary year.\n")

    except EOFError:
        key = False

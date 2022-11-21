#Link da Questão -> https://www.urionlinejudge.com.br/judge/pt/problems/view/2712

n = int(input())
var = ""
num = ""
for i in range(n):
    placa = input()

    if len(placa) == 8:

        var = placa[0] + placa[1] + placa[2]
        qi = var.isupper()
        num = placa[4] + placa[5] + placa[6] + placa[7]
        x = num.isnumeric()

        if qi and x and placa[3] == "-":

            if placa[7] == "0" or  placa[7] == "9":
                print("FRIDAY")
            elif placa[7] == "1" or placa[7] == "2":
                print("MONDAY")
            elif placa[7] == "3" or placa[7] == "4":
                print("TUESDAY")
            elif placa[7] == "5" or placa[7] == "6":
                print("WEDNESDAY")
            elif placa[7] == "7" or placa[7] == "8":
                print("THURSDAY")
        else:
            print("FAILURE")

    else:
        print("FAILURE")
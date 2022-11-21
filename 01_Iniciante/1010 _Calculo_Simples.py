# Link da Questão -> https://www.urionlinejudge.com.br/judge/pt/problems/view/1010

entrada = input()
item01 = entrada.split()

entrada = input()
item02 = entrada.split()

valortotal = int(item01[1]) * float(item01[2]) + int(item02[1]) * float(item02[2])

print("VALOR A PAGAR: R$ {:.2F}".format((valortotal)))
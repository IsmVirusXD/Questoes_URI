# Link da Questão -> https://www.urionlinejudge.com.br/judge/pt/problems/view/1009

nome = input()
salario = float(input())
vendas = float(input())

total = salario + (vendas * 0.15)

print("TOTAL = R$ {:.2f}".format(total))
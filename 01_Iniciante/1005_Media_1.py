# Link da Questão -> https://www.urionlinejudge.com.br/judge/pt/problems/view/1005

A = input()
B = input()

A = float(A)
B = float(B)

Pa = 3.5
Pb = 7.5

MEDIA = ((A * Pa) + (B * Pb))/(Pa + Pb)

print("MEDIA = {:.5f}".format(MEDIA))
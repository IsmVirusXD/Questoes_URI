# link da Questão: https://www.urionlinejudge.com.br/judge/pt/problems/view/1012

valores = input()
indice = valores.split()

A = float(indice[0])
B = float(indice[1])
C = float(indice[2])
pi = 3.14159

triangulo = (A * C)/2
circulo = pi*C**2
trapezio = ((A + B) * C) / 2
quadrado = B * B
retangulo = A * B

print("TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}".format(triangulo, circulo, trapezio, quadrado, retangulo))
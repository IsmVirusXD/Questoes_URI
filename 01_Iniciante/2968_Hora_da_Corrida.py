#Link da Questão: https://www.urionlinejudge.com.br/judge/pt/problems/view/2968
from math import ceil

entrada = input()
valore = entrada.split()

i = 0
porcent = 0

voltas = int(valore[0])
placas = int(valore[1])
total = placas * voltas

one = ceil((total * 10) / 100)
two = ceil((total * 20) / 100)
the = ceil((total * 30) / 100)
fur = ceil((total * 40) / 100)
fiv = ceil((total * 50) / 100)
six = ceil((total * 60) / 100)
sev = ceil((total * 70) / 100)
eit = ceil((total * 80) / 100)
nin = ceil((total * 90) / 100)

print('{} {} {} {} {} {} {} {} {}'.format(one,two,the,fur,fiv,six,sev,eit,nin))

#Link da Questão: https://www.beecrowd.com.br/judge/pt/problems/view/1024
from math import trunc

def primeira(texto: str):
    new_texto = ''
    for caracter in texto:
        if caracter.isalpha() : new_texto += chr(ord(caracter)+3)
        else : new_texto += caracter

    return new_texto

def terceira(texto: str):
    new_texto = ''
    comeco = trunc(len(texto)/2)
    contador = 0
    for caracter in texto:
        if contador >= comeco: new_texto += chr(ord(str(caracter)) - 1)
        else: new_texto += str(caracter)
        contador += 1
    return new_texto

numero = int(input())

for i in range(0, numero):
    texto = input()
    texto = primeira(texto)[::-1]
    texto = terceira(texto)
    print(texto)

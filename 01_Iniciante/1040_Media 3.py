#Link da Questão -> https://www.urionlinejudge.com.br/judge/pt/problems/view/1040

entrada = input()
valor = entrada.split()

key = False
peso_valor = [2,3,4,1]
media = 0.0
peso = 0.0
i = 0

while i < 4:
    valor[i] = float(valor[i])
    media += (valor[i] * peso_valor[i])
    peso += peso_valor[i]
    i += 1

media = (media)/peso

print("Media: {:.1f}".format(media))

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    key = True

if key:
    nota = input()
    media = (media + float(nota))/2
    print("Nota do exame: {}".format(nota))
    if media >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print("Media final: {:.1f}".format(media))



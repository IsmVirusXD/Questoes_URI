#link da Questão -> https://www.beecrowd.com.br/judge/pt/problems/view/2971

valoresCartas = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'D': 10,
    'Q': 11,
    'J': 12,
    'K': 13,
}

class Jogador:
    #Iniciador da Classe
    def __init__(self, nome : str, maoInicial = [], joker = False):
        self.nome = nome
        self.joker = joker
        self.mao = maoInicial
        self.cartas = {}

        self.update()

    #Deixa a Quantidade de Cartas Atualizado
    def update(self):
        self.mao.sort()
        self.cartas.clear()
        for carta in set(self.mao):
            card = str(carta)
            quantidade = self.mao.count(carta)
            self.cartas[card] = quantidade

    # Adiciona uma Carta na mão
    def adicionarCarta(self, carta:str):
        self.mao.append(carta)
        self.update()

    # Remove uma carta da mão
    def removerCarta(self, carta:str):
        self.mao.remove(carta)
        self.update()

    # Retorna a Carta menos Comum na mão:
    def menorCarta(self):
        menor = ''
        valor = 5

        segundo = ''
        vsegundo = 5

        for item in self.cartas:
            k = self.cartas[item]
            if item == 'Joker':
                continue
            elif valor >= k or menor == '':
                segundo = menor
                vsegundo = valor
                menor = item
                valor = k

        if valor == vsegundo and menor != segundo:
            i = valoresCartas[segundo]
            n = valoresCartas[menor]

            if i < n:
                return str(segundo)
            else:
                return str(menor)
        else:
            return str(menor)

    #Retorna o Valor do Coringa
    def getJoker(self):
        return self.joker

    # Seta o Coringa foi recebido nessa rodada
    def setJoker(self):
        if self.joker:
            self.joker = False
        else:
            self.joker = True

    # Testa se o Coringa esta na nossa mão
    def isJoker(self):

        try:
            n = self.mao.index('Joker')
            return True
        except ValueError:
            return False

    # Testa se Estamos Ganhando:
    def isWining(self):

        carta = self.mao[0]
        if self.mao.count(carta) == len(self.mao):
            return True
        else:
            return False

if __name__ == '__main__':
    participantes = []
    N, Inicial = input().split()

    N = int(N)
    Inicial = int(Inicial) - 1

    for n in range(N):
        mao = list(input())
        jogador = Jogador(n+1, mao)
        participantes.append(jogador)

    primeiro = participantes[Inicial]
    primeiro.adicionarCarta("Joker")
    primeiro.setJoker()

    jogando = primeiro

    while True:
        #input()

        try:
            proximo = participantes[Inicial + 1]
        except IndexError:
            Inicial = len(participantes) - 1
            proximo = participantes[0]

        #print(f"Vez do {jogando.nome} -> Inicio da Rodada: {jogando.mao}")

        if jogando.isJoker():
            if jogando.getJoker():
                #print(f'jogador: {jogando.nome} deve passar a menor carta pois não pode jogar o Coringa')
                jogando.setJoker()
                menor = jogando.menorCarta()
                #print(f'Carta Passada: {menor}')
                jogando.removerCarta(menor)
                proximo.adicionarCarta(menor)
            else:
                #print(f'jogador: {jogando.nome} deve passar o Coringa')
                #print(f'Carta Passada: Joker')
                jogando.removerCarta('Joker')
                proximo.adicionarCarta('Joker')
                proximo.setJoker()
        else:
            #print(f'jogador: {jogando.nome} deve passar a menor carta')
            menor = jogando.menorCarta()
            #print(f'Carta Passada: {menor}')
            jogando.removerCarta(menor)
            proximo.adicionarCarta(menor)


        Inicial = (Inicial + 1) % len(participantes)

        #print(f"Fim do {jogando.nome} -> Final da Rodada: {jogando.mao}")

        if jogando.isWining():
            print(jogando.nome)
            break
        else:
            jogando = proximo

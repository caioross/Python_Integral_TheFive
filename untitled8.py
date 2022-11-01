import time
import random

def montarBaralho():
    baralho = []
    cores = ["Vermelho", "Verde", "Amarelo", "Azul"]
    valores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "+2", "Pular", "Inverter"]
    coringas = ["Escolher", "+4"]
    for cor in cores:
        for valor in valores:
            carta = "{} {}".format(cor, valor)
            #carta = f"{cor} {valor}"
            baralho.append(carta)
    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])
    print(deck)
    return deck

def shuffleDeck(deck):
    for cardPos in range(len(deck)):
        randPos = random.randint(0, 107)
        deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]
    return deck



def drawCards(numCards):
    cardsDrawn = []
    for x in range(numCards):
        cardsDrawn.append(unoDeck.pop(0))
    return cardsDrawn

def showHand(player, playerHand):
    print("Player {}'s Turn".format(players_name[player]))
    time.sleep(10)
    print("Your Hand")
    print("------------------")
    y = 1
    for card in playerHand:
        print("{}) {}".format(y, card))
        y += 1
    print("")

def canPlay(colour, value, playerHand):
    for card in playerHand:
        if "Wild" in card:
            return True
        elif colour in card or value in card:
            return True
    return False


unoDeck = buildDeck()
unoDeck = shuffleDeck(unoDeck)
unoDeck = shuffleDeck(unoDeck)
discards = []

players_name = []
players = []
colours = ["Red", "Green", "Yellow", "Blue"]
numPlayers = int(input("How many players?"))
while numPlayers < 2 or numPlayers > 4:
    numPlayers = int(
        input("Invalid. Please enter a number between 2-4.\nHow many players?"))
for player in range(numPlayers):
    players_name.append(input("Enter player {} name: ".format(player+1)))
    players.append(drawCards(5))


playerTurn = 0
playDirection = 1
playing = True
discards.append(unoDeck.pop(0))
splitCard = discards[0].split(" ", 1)
currentColour = splitCard[0]
if currentColour != "Wild":
    cardVal = splitCard[1]
else:
    cardVal = "Any"

while playing:
    showHand(playerTurn, players[playerTurn])
    print("Card on top of discard pile: {}".format(discards[-1]))
    if canPlay(currentColour, cardVal, players[playerTurn]):
        cardChosen = int(input("Which card do you want to play?"))
        while not canPlay(currentColour, cardVal, [players[playerTurn][cardChosen-1]]):
            cardChosen = int(
                input("Not a valid card. Which card do you want to play?"))
        print("You played {}".format(players[playerTurn][cardChosen-1]))
        discards.append(players[playerTurn].pop(cardChosen-1))
        # cheak if player won
        if len(players[playerTurn]) == 0:
            playing = False
            # winner = "Player {}".format(playerTurn+1)
            winner = players_name[playerTurn]
        else:
            # cheak for special cards
            splitCard = discards[-1].split(" ", 1)
            currentColour = splitCard[0]
            if len(splitCard) == 1:
                cardVal = "Any"
            else:
                cardVal = splitCard[1]
            if currentColour == "Wild":
                for x in range(len(colours)):
                    print("{}) {}".format(x+1, colours[x]))
                newColour = int(
                    input("What colour would you like to choose? "))
                while newColour < 1 or newColour > 4:
                    newColour = int(
                        input("Invalid option. What colour would you like to choose"))
                currentColour = colours[newColour-1]
            if cardVal == "Reverse":
                playDirection = playDirection * -1
            elif cardVal == "Skip":
                playerTurn += playDirection
                if playerTurn >= numPlayers:
                    playerTurn = 0
                elif playerTurn < 0:
                    playerTurn = numPlayers-1
            elif cardVal == "Draw Two":
                playerDraw = playerTurn+playDirection
                if playerDraw == numPlayers:
                    playerDraw = 0
                elif playerDraw < 0:
                    playerDraw = numPlayers-1
                players[playerDraw].extend(drawCards(2))
            elif cardVal == "Draw Four":
                playerDraw = playerTurn+playDirection
                if playerDraw == numPlayers:
                    playerDraw = 0
                elif playerDraw < 0:
                    playerDraw = numPlayers-1
                players[playerDraw].extend(drawCards(4))
            print("")
    else:
        print("You can't play. You have to draw a card.")
        players[playerTurn].extend(drawCards(1))

    playerTurn += playDirection
    if playerTurn >= numPlayers:
        playerTurn = 0
    elif playerTurn < 0:
        playerTurn = numPlayers-1

print("Game Over")
print("{} is the Winner!".format(winner))

import random
import time

def montarBaralho():
    baralho = []
    cores = ["Vermelho", "Verde", "Amarelo", "Azul"]
    valores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "+2", "Pular", "Inverter"]
    coringas = ["Escolher", "+4"]
    for cor in cores:
        for valor in valores:
            carta = "{} {}".format(cor, valor)
            #carta = f"{cor} {valor}"
            baralho.append(carta)
    for i in range(4):
        baralho.append(coringas[0])
        baralho.append(coringas[1])
    return baralho
def embaralharBaralho(baralho):
    for cartaPos in range(len(baralho)):
        random.shuffle(baralho)
    return baralho
def virarCartas(numeroCartas):
    cartaVirada = []
    for x in range(numeroCartas):
        cartaVirada.append(baralhoMonte.pop(0))
    return cartaVirada
def jogada(cor, valor, maoJogador):
    for carta in maoJogador:
        if "Coringas" in carta:
            return True
        elif cor in carta or valor in carta:
            return True
    return False
def mostrarMao(jogador, maoJogador):
    print("Vez de {} jogar: ".format(jogadorNome[jogador]))
    time.sleep(10)
    print("Suas cartas:")
    print("------------------")
    y = 1
    for carta in maoJogador:
        print("{}) {}".format(y, carta))
        y += 1
    print("")
baralhoMonte = montarBaralho()
baralhoMonte = embaralharBaralho(baralhoMonte)
baralhoMonte = embaralharBaralho(baralhoMonte)
descartadas = []
jogadorNome = []
jogadores = []
cores = ["Vermelho", "Verde", "Amarelo", "Azul"]
numeroJogadores = int(input("Quantos jogadores?"))
while numeroJogadores < 2 or numeroJogadores > 5:
    numeroJogadores = int(input("Invalido, Escolha um valor entre 2-4.\nQuantos Jogadores?"))
for jogador in range(numeroJogadores):
    jogadorNome.append(input("Qual o nome do {} jogador? ".format(jogador+1)))
    jogadores.append(virarCartas(5))
vezJogador = 0
direcao = 1
jogando = True
descartadas.append(baralhoMonte.pop(0))
separarCarta = descartadas[0].split(" ", 1)
corAtual = separarCarta[0]
if corAtual != "Coringas":
    valorCarta = separarCarta[1]
else:
    valorCarta = "Qualquer"
while jogando:
    mostrarMao(vezJogador, jogadores[vezJogador])
    print("Carta no topo da Pilha: {}".format(descartadas[-1]))
    if jogada(corAtual, valorCarta, jogadores[vezJogador]):
        cartaEscolhida = int(input("Qual carta você deseja jogar?"))
        while not jogada(corAtual, valorCarta, [jogadores[vezJogador][cartaEscolhida-1]]):
            cartaEscolhida = int(input("Não é uma carta válida? Escolha outra carta!"))
        print("Você escolheu {}".format(jogadores[vezJogador][cartaEscolhida-1]))
        descartadas.append(jogadores[vezJogador].pop(cartaEscolhida-1))
        if len(jogadores[vezJogador]) == 0:
            jogando = False
            vencedor = jogadorNome[vezJogador]
        else:
            separarCarta = descartadas[-1].split(" ", 1)
            corAtual = separarCarta[0]
            if len(separarCarta) == 1:
                valorCarta = "Qualquer"
            else:
                valorCarta = separarCarta[1]
            if corAtual == "Coringas":
                for x in range(len(cores)):
                    print("{}) {}".format(x+1, cores[x]))
                novaCor = int(input("Qual cor você quer? "))
                while novaCor < 1 or novaCor > 4:
                    novaCor = int(input("Errado, Qual cor você quer? "))
                corAtual = cores[novaCor-1]
            if valorCarta == "Inverter":
                direcao = direcao * -1
            elif valorCarta == "Pular":
                vezJogador += direcao
                if vezJogador >= numeroJogadores:
                    vezJogador = 0
                elif vezJogador < 0:
                    vezJogador = numeroJogadores-1
            print("")
    else:
        print("Você não pode jogar.Você deve comprar uma carta.")
        jogadores[vezJogador].extend(virarCartas(1))
    vezJogador += direcao
    if vezJogador >= numeroJogadores:
        vezJogador = 0
    elif vezJogador < 0:
        vezJogador = numeroJogadores-1
print("Fim de Jogo")
print("{} Venceu Esta rodada! Parabéns !".format(winner))

cores = ["Vermelho", "Verde", "Amarelo", "Azul"]

while novaCor < 1 or novaCor > 4:
                    novaCor = int(input("Errado, Qual cor você quer? "))
                corAtual = cores[novaCor-1]

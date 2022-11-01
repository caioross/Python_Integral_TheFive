{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNqo2Oxuk0mwd+KQ6TSlBpU"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "lKRF7iSGQzK9"
      },
      "outputs": [],
      "source": [
        "import random\n",
        "\n",
        "def montarBaralho():\n",
        "    baralho = []\n",
        "    cores = [\"Vermelho\", \"Verde\", \"Amarelo\", \"Azul\"]\n",
        "    valores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, \"+2\", \"Pular\", \"Inverter\"]\n",
        "    coringas = [\"Escolher\", \"+4\"]\n",
        "    for cor in cores:\n",
        "        for valor in valores:\n",
        "            carta = \"{} {}\".format(cor, valor)\n",
        "            #carta = f\"{cor} {valor}\"\n",
        "            baralho.append(carta)\n",
        "\n",
        "montarBaralho()\n",
        "\n",
        "print(baralho[0])\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "    for i in range(4):\n",
        "        deck.append(wilds[0])\n",
        "        deck.append(wilds[1])\n",
        "    print(deck)\n",
        "    return deck\n",
        "\n",
        "def shuffleDeck(deck):\n",
        "    for cardPos in range(len(deck)):\n",
        "        randPos = random.randint(0, 107)\n",
        "        deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]\n",
        "    return deck\n",
        "\n",
        "\n",
        "\n",
        "def drawCards(numCards):\n",
        "    cardsDrawn = []\n",
        "    for x in range(numCards):\n",
        "        cardsDrawn.append(unoDeck.pop(0))\n",
        "    return cardsDrawn\n",
        "\n",
        "def showHand(player, playerHand):\n",
        "    print(\"Player {}'s Turn\".format(players_name[player]))\n",
        "    time.sleep(10)\n",
        "    print(\"Your Hand\")\n",
        "    print(\"------------------\")\n",
        "    y = 1\n",
        "    for card in playerHand:\n",
        "        print(\"{}) {}\".format(y, card))\n",
        "        y += 1\n",
        "    print(\"\")\n",
        "\n",
        "def canPlay(colour, value, playerHand):\n",
        "    for card in playerHand:\n",
        "        if \"Wild\" in card:\n",
        "            return True\n",
        "        elif colour in card or value in card:\n",
        "            return True\n",
        "    return False\n",
        "\n",
        "\n",
        "unoDeck = buildDeck()\n",
        "unoDeck = shuffleDeck(unoDeck)\n",
        "unoDeck = shuffleDeck(unoDeck)\n",
        "discards = []\n",
        "\n",
        "players_name = []\n",
        "players = []\n",
        "colours = [\"Red\", \"Green\", \"Yellow\", \"Blue\"]\n",
        "numPlayers = int(input(\"How many players?\"))\n",
        "while numPlayers < 2 or numPlayers > 4:\n",
        "    numPlayers = int(\n",
        "        input(\"Invalid. Please enter a number between 2-4.\\nHow many players?\"))\n",
        "for player in range(numPlayers):\n",
        "    players_name.append(input(\"Enter player {} name: \".format(player+1)))\n",
        "    players.append(drawCards(5))\n",
        "\n",
        "\n",
        "playerTurn = 0\n",
        "playDirection = 1\n",
        "playing = True\n",
        "discards.append(unoDeck.pop(0))\n",
        "splitCard = discards[0].split(\" \", 1)\n",
        "currentColour = splitCard[0]\n",
        "if currentColour != \"Wild\":\n",
        "    cardVal = splitCard[1]\n",
        "else:\n",
        "    cardVal = \"Any\"\n",
        "\n",
        "while playing:\n",
        "    showHand(playerTurn, players[playerTurn])\n",
        "    print(\"Card on top of discard pile: {}\".format(discards[-1]))\n",
        "    if canPlay(currentColour, cardVal, players[playerTurn]):\n",
        "        cardChosen = int(input(\"Which card do you want to play?\"))\n",
        "        while not canPlay(currentColour, cardVal, [players[playerTurn][cardChosen-1]]):\n",
        "            cardChosen = int(\n",
        "                input(\"Not a valid card. Which card do you want to play?\"))\n",
        "        print(\"You played {}\".format(players[playerTurn][cardChosen-1]))\n",
        "        discards.append(players[playerTurn].pop(cardChosen-1))\n",
        "        # cheak if player won\n",
        "        if len(players[playerTurn]) == 0:\n",
        "            playing = False\n",
        "            # winner = \"Player {}\".format(playerTurn+1)\n",
        "            winner = players_name[playerTurn]\n",
        "        else:\n",
        "            # cheak for special cards\n",
        "            splitCard = discards[-1].split(\" \", 1)\n",
        "            currentColour = splitCard[0]\n",
        "            if len(splitCard) == 1:\n",
        "                cardVal = \"Any\"\n",
        "            else:\n",
        "                cardVal = splitCard[1]\n",
        "            if currentColour == \"Wild\":\n",
        "                for x in range(len(colours)):\n",
        "                    print(\"{}) {}\".format(x+1, colours[x]))\n",
        "                newColour = int(\n",
        "                    input(\"What colour would you like to choose? \"))\n",
        "                while newColour < 1 or newColour > 4:\n",
        "                    newColour = int(\n",
        "                        input(\"Invalid option. What colour would you like to choose\"))\n",
        "                currentColour = colours[newColour-1]\n",
        "            if cardVal == \"Reverse\":\n",
        "                playDirection = playDirection * -1\n",
        "            elif cardVal == \"Skip\":\n",
        "                playerTurn += playDirection\n",
        "                if playerTurn >= numPlayers:\n",
        "                    playerTurn = 0\n",
        "                elif playerTurn < 0:\n",
        "                    playerTurn = numPlayers-1\n",
        "            elif cardVal == \"Draw Two\":\n",
        "                playerDraw = playerTurn+playDirection\n",
        "                if playerDraw == numPlayers:\n",
        "                    playerDraw = 0\n",
        "                elif playerDraw < 0:\n",
        "                    playerDraw = numPlayers-1\n",
        "                players[playerDraw].extend(drawCards(2))\n",
        "            elif cardVal == \"Draw Four\":\n",
        "                playerDraw = playerTurn+playDirection\n",
        "                if playerDraw == numPlayers:\n",
        "                    playerDraw = 0\n",
        "                elif playerDraw < 0:\n",
        "                    playerDraw = numPlayers-1\n",
        "                players[playerDraw].extend(drawCards(4))\n",
        "            print(\"\")\n",
        "    else:\n",
        "        print(\"You can't play. You have to draw a card.\")\n",
        "        players[playerTurn].extend(drawCards(1))\n",
        "\n",
        "    playerTurn += playDirection\n",
        "    if playerTurn >= numPlayers:\n",
        "        playerTurn = 0\n",
        "    elif playerTurn < 0:\n",
        "        playerTurn = numPlayers-1\n",
        "\n",
        "print(\"Game Over\")\n",
        "print(\"{} is the Winner!\".format(winner))"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "import time\n",
        "\n",
        "def montarBaralho():\n",
        "    baralho = []\n",
        "    cores = [\"Vermelho\", \"Verde\", \"Amarelo\", \"Azul\"]\n",
        "    valores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, \"+2\", \"Pular\", \"Inverter\"]\n",
        "    coringas = [\"Escolher\", \"+4\"]\n",
        "    for cor in cores:\n",
        "        for valor in valores:\n",
        "            carta = \"{} {}\".format(cor, valor)\n",
        "            #carta = f\"{cor} {valor}\"\n",
        "            baralho.append(carta)\n",
        "    for i in range(4):\n",
        "        baralho.append(coringas[0])\n",
        "        baralho.append(coringas[1])\n",
        "    return baralho\n",
        "\n",
        "def embaralharBaralho(baralho):\n",
        "    for cartaPos in range(len(baralho)):\n",
        "        aleatorioPos = random.randint(0, 107)\n",
        "        baralho[cartaPos], baralho[aleatorioPos] = baralho[aleatorioPos], baralho[cartaPos]\n",
        "    return baralho\n",
        "\n",
        "def virarCartas(numeroCartas):\n",
        "    cartaVirada = []\n",
        "    for x in range(numeroCartas):\n",
        "        cartaVirada.append(baralhoMonte.pop(0))\n",
        "    return cartaVirada\n",
        "\n",
        "def jogada(cor, valor, maoJogador):\n",
        "    for carta in maoJogador:\n",
        "        if \"Coringas\" in carta:\n",
        "            return True\n",
        "        elif cor in carta or valor in carta:\n",
        "            return True\n",
        "    return False\n",
        "\n",
        "def mostrarMao(jogador, maoJogador):\n",
        "    print(\"Vez de {} jogar: \".format(jogadorNome[jogador]))\n",
        "    time.sleep(10)\n",
        "    print(\"Suas cartas:\")\n",
        "    print(\"------------------\")\n",
        "    y = 1\n",
        "    for carta in maoJogador:\n",
        "        print(\"{}) {}\".format(y, carta))\n",
        "        y += 1\n",
        "    print(\"\")\n",
        "\n",
        "\n",
        "baralhoMonte = montarBaralho()\n",
        "baralhoMonte = embaralharBaralho(baralhoMonte)\n",
        "baralhoMonte = embaralharBaralho(baralhoMonte)\n",
        "descartadas = []\n",
        "jogadorNome = []\n",
        "jogadores = []\n",
        "cores = [\"Vermelho\", \"Verde\", \"Amarelo\", \"Azul\"]\n",
        "numeroJogadores = int(input(\"Quantos jogadores?\"))\n",
        "while numeroJogadores < 2 or numeroJogadores > 5:\n",
        "    numeroJogadores = int(input(\"Invalido, Escolha um valor entre 2-4.\\nQuantos Jogadores?\"))\n",
        "for jogador in range(numeroJogadores):\n",
        "    jogadorNome.append(input(\"Qual o nome do {} jogador? \".format(jogador+1)))\n",
        "    jogadores.append(virarCartas(5))\n",
        "\n",
        "vezJogador = 0\n",
        "direcao = 1\n",
        "jogando = True\n",
        "descartadas.append(baralhoMonte.pop(0))\n",
        "separarCarta = descartadas[0].split(\" \", 1)\n",
        "corAtual = separarCarta[0]\n",
        "if corAtual != \"Coringas\":\n",
        "    valorCarta = separarCarta[1]\n",
        "else:\n",
        "    valorCarta = \"Qualquer\"\n",
        "\n",
        "while jogando:\n",
        "    mostrarMao(vezJogador, jogadores[vezJogador])\n",
        "    print(\"Carta no topo da Pilha: {}\".format(descartadas[-1]))\n",
        "    if jogada(corAtual, valorCarta, jogadores[vezJogador]):\n",
        "        cartaEscolhida = int(input(\"Which card do you want to play?\"))\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "        \n",
        "        while not canPlay(currentColour, cardVal, [players[playerTurn][cardChosen-1]]):\n",
        "            cardChosen = int(\n",
        "                input(\"Not a valid card. Which card do you want to play?\"))\n",
        "        print(\"You played {}\".format(players[playerTurn][cardChosen-1]))\n",
        "        discards.append(players[playerTurn].pop(cardChosen-1))\n",
        "        # cheak if player won\n",
        "        if len(players[playerTurn]) == 0:\n",
        "            playing = False\n",
        "            # winner = \"Player {}\".format(playerTurn+1)\n",
        "            winner = players_name[playerTurn]\n",
        "        else:\n",
        "            # cheak for special cards\n",
        "            splitCard = discards[-1].split(\" \", 1)\n",
        "            currentColour = splitCard[0]\n",
        "            if len(splitCard) == 1:\n",
        "                cardVal = \"Any\"\n",
        "            else:\n",
        "                cardVal = splitCard[1]\n",
        "            if currentColour == \"Wild\":\n",
        "                for x in range(len(colours)):\n",
        "                    print(\"{}) {}\".format(x+1, colours[x]))\n",
        "                newColour = int(\n",
        "                    input(\"What colour would you like to choose? \"))\n",
        "                while newColour < 1 or newColour > 4:\n",
        "                    newColour = int(\n",
        "                        input(\"Invalid option. What colour would you like to choose\"))\n",
        "                currentColour = colours[newColour-1]\n",
        "            if cardVal == \"Reverse\":\n",
        "                playDirection = playDirection * -1\n",
        "            elif cardVal == \"Skip\":\n",
        "                playerTurn += playDirection\n",
        "                if playerTurn >= numPlayers:\n",
        "                    playerTurn = 0\n",
        "                elif playerTurn < 0:\n",
        "                    playerTurn = numPlayers-1\n",
        "            elif cardVal == \"Draw Two\":\n",
        "                playerDraw = playerTurn+playDirection\n",
        "                if playerDraw == numPlayers:\n",
        "                    playerDraw = 0\n",
        "                elif playerDraw < 0:\n",
        "                    playerDraw = numPlayers-1\n",
        "                players[playerDraw].extend(drawCards(2))\n",
        "            elif cardVal == \"Draw Four\":\n",
        "                playerDraw = playerTurn+playDirection\n",
        "                if playerDraw == numPlayers:\n",
        "                    playerDraw = 0\n",
        "                elif playerDraw < 0:\n",
        "                    playerDraw = numPlayers-1\n",
        "                players[playerDraw].extend(drawCards(4))\n",
        "            print(\"\")\n",
        "    else:\n",
        "        print(\"You can't play. You have to draw a card.\")\n",
        "        players[playerTurn].extend(drawCards(1))\n",
        "\n",
        "    playerTurn += playDirection\n",
        "    if playerTurn >= numPlayers:\n",
        "        playerTurn = 0\n",
        "    elif playerTurn < 0:\n",
        "        playerTurn = numPlayers-1\n",
        "\n",
        "print(\"Game Over\")\n",
        "print(\"{} is the Winner!\".format(winner))\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 382
        },
        "id": "FssXWAk-dMaI",
        "outputId": "20e99cca-e2c8-4578-8ce6-ff48abfd437d"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "error",
          "ename": "IndexError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mIndexError\u001b[0m                                Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-19-2350e942ed15>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     52\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     53\u001b[0m \u001b[0mbaralhoMonte\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mmontarBaralho\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 54\u001b[0;31m \u001b[0mbaralhoMonte\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0membaralharBaralho\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mbaralhoMonte\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     55\u001b[0m \u001b[0mbaralhoMonte\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0membaralharBaralho\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mbaralhoMonte\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     56\u001b[0m \u001b[0mdescartadas\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-19-2350e942ed15>\u001b[0m in \u001b[0;36membaralharBaralho\u001b[0;34m(baralho)\u001b[0m\n\u001b[1;32m     20\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mcartaPos\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mbaralho\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     21\u001b[0m         \u001b[0maleatorioPos\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mrandom\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrandint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m107\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 22\u001b[0;31m         \u001b[0mbaralho\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mcartaPos\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbaralho\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0maleatorioPos\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mbaralho\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0maleatorioPos\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbaralho\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mcartaPos\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     23\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mbaralho\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     24\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mIndexError\u001b[0m: list index out of range"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "maoJogador = [\"vermelho 5\", \"Verde 4\",\"azul 7\"]\n",
        "\n",
        "y = 1\n",
        "for carta in maoJogador:\n",
        "  print(\"{}) {}\".format(y, carta))\n",
        "  y += 1\n",
        "  y = y+1\n",
        "#print(\"_____\")\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "spzfhb-PGY3r",
        "outputId": "ae84ec34-3e17-45b6-cf36-a6a851f01a92"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1) vermelho 5\n",
            "3) Verde 4\n",
            "5) azul 7\n"
          ]
        }
      ]
    }
  ]
}
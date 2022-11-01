import random
import time

def construirBaralho():
    baralho = []
    cores = ["vermelho", "verde", "amarelo", "azul"]
    valores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "+2", "pular", "inverter"]
    coringas = ["escolher", "+4"]
    for cor in cores:
        for valor in valores:
            carta = "{} {}".format(cor, valor)
            baralho.append(carta)
    for coringa in range(4):
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
def mostrarMao(jogador, maoJogador):
    print("vez de {} jogar: ".format(jogadorNome[jogador]))
    time.sleep(10)
    print("Suas cartas")
    print("------------")
    y = 1
    for carta in maoJogador:
        print("{}) {}".format(y, carta))
        y = y+1
    print("")
def jogada(cor, valor, maoJogador):
    for carta in maoJogador:
        if "coringas" in carta:
          return True
        elif cor in carta or valor in carta:
          return True
    return False
baralhoMonte = construirBaralho()
baralhoMonte = embaralharBaralho(baralhoMonte)
baralhoMonte = embaralharBaralho(baralhoMonte)
descartadas = []
jogadorNome = []
jogadores = []
cores = ["vermelho", "verde", "amarelo", "azul"]
numeroJogadores = int(input("Quantos jogadores?"))
while numeroJogadores < 2 or numeroJogadores > 5:
    numerojogadores = int(input("Invalido, escolha um valor entre 2-5. \nQuantos Jogadores?"))
for jogador in range(numeroJogadores):
  jogadorNome.append(input("Qual o nome do {} jogador?".format(jogador+1)))
  jogadores.append(virarCartas(5))
vezJogador = 0
direcao = 1
jogando = True
descartadas.append(baralhoMonte.pop(0))
separarCarta = descartadas[0].split(" ",1)
corAtual = separarCarta[0]
if corAtual != "Coringas":
    valorCarta = separarCarta[1]
else:
    valorCarta ="Qualquer"
while jogando:
    mostrarMao(vezJogador, jogadores[vezJogador])
    print("Carta no topo da pilha: {}".format(descartadas[-1]))
    if jogada(corAtual, valorCarta, jogadores[vezJogador]):
        cartaEscolhida = int(input("Qual carta voce quer jogar?"))
        while not jogada(corAtual, valorCarta, [jogadores[vezJogador][cartaEscolhida-1]]):
          cartaEscolhida = int(input("Não é uma carta valida. Escolha outra carta"))
        print("Voce escolheu {}".format(jogadores[vezJogador][cartaEscolhida-1]))
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
                print("{} {}".format(x+1, cores[x]))
            novaCor = int(input("Qual cor voce quer? "))
            while novaCor < 1 or novaCor > 4:
                novaCor = int(input("Opcao invalida. Qual cor voce quer?"))
            corAtual = cores[novaCor -1]
          if valorCarta == "Inverter":
            direcao = direcao * -1
          elif valorCarta == "Pular":
            vezJogador += direcao
            if vezJogador >= numeroJogadores:
              vezJogador = 0
            elif vezJogador < 0:
              vezJogador = numeroJogadores-1
          print(" ")
    else:
      print("Voce nao pode jogar. Voce deve comprar uma carta")
      jogadores[vezJogador].extend(virarCartas(1))
# fim da vez do jogador
    vezJogador += direcao
    if vezJogador >= numeroJogadores:
              vezJogador = 0
    elif vezJogador < 0:
        vezJogador = numeroJogadores-1
print("Game Over")
print("{} é o vencedor!").format(vencedor)

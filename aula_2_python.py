import random
import time

def construirdeck():
  y = []
  cores = ['Vermelho', 'Verde', 'Amarelo' , 'Azul']
  valores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '+2', 'Pula Vez', 'Reverso']
  coringas = ['Escolher', '+ 4']
  for cor in cores:
    for valor in valores:
      carta = f"{cor}{valor}"
      y.append(carta)
  for i in range(4):
    y.append(coringas[0])
    y.append(coringas[1])
  return y

def embaralhardeck(x):
  for cartaPos in range(len(x)):
      random.shuffle(x)
  return x

def compracartas(m):
  cartavirada = []
  for f in range(m):
    cartavirada.append(baralhoMonte.pop(0))
  return cartavirada

def definicaomao(n, o):
  print(f'Vez de {jogador_nome[n]} jogar:')
  time.sleep(10)
  print('Suas cartas:')
  print('--------------')
  g = 1
  for carta in o:
    print(f'{g}) {carta}')
    g = g+1
  print('')

def jogada(z, p, o):
  for carta in o:
    if "Coringas" in carta:
      return True
    elif z in carta or p in carta:
      return True
  return False

baralhoMonte = construirdeck()
baralhoMonte = embaralhardeck(baralhoMonte)
baralhoMonte = embaralhardeck(baralhoMonte)
descartadas = []

jogador_nome = []
jogadores = []
cores = ['Vermelho', 'Verde', 'Amarelo' , 'Azul']

numerojogadores = int(input('Quantos jogadores?'))
while numerojogadores < 2 or numerojogadores > 5:
  numerojogadores = int(input('Invalido, Escolha um valor entre 2-4. \nQuantos jogador?'))
for jogador in range(numerojogadores):
  jogador_nome.append(input(f'Qual o nome do {jogador+1}?'))
  jogadores.append(compracartas(5))

vezjogador = 0
direcao = 1
jogando = True

descartadas.append(baralhoMonte.pop(0))
separarcarta = descartadas[0].split(" ", 1)
coratual = separarcarta[0]

if coratual != 'Coringas':
  valorcarta = separarcarta[1]
else:
  valorcarta = 'Qualquer'

while jogando:
  definicaomao(vezjogador, jogadores[vezjogador])
  print(f'Carta no tipo da pilha: {descartadas[-1]}')
  if jogada(coratual, valorcarta, jogadores[vezjogador]):
    cartaescolhida = int(input('Qual carta voce quer jogar?'))
    while not jogada(coratual, valorcarta, [jogadores[vezjogador][cartaescolhida-1]]):
      cartaescolhida = int(input('Não é uma carta válida? Escolha outra carta!'))
    print(f'Você escolheu{jogadores[vezjogador][cartaescolhida-1]}')
    descartadas.append(jogadores[vezjogador].pop(cartaescolhida-1))


    if len(jogadores[vezjogador]) == 0:
      jogando = False
      vencedor = jogador_nome[vezjogador]
    

    else:
      separarcarta = descartadas[-1].split('', 1)
      coratual = separarcarta[0]
      if len(separarcarta) == 1:
        valorcarta = 'Qualquer'
      else:
        valorcarta = separarcarta[1]
      if coratual == 'Coringas':
        for x in range(len(cores)):
          print(f'{x+1}) {cores[x]}')
        novacor = int(input('Que cor você gostaria de escolher?'))
        while novacor < 1 or novacor > 4:
          novacor = int(input('Opção Inválida. Qual cor você gostaria de escolher?'))
        coratual = cores[novacor-1]
      if valorcarta == 'Inverter':
        direcao = direcao * -1
      elif valorcarta == 'Pular':
        vezjogador += direcao
        if vezjogador >= numerojogadores:
          vezjogador = 0
        elif vezjogador < 0:
            vezjogador = numerojogadores-1
  else:
    print('Você não pode jogar. Você deve comprar uma carta.')
    jogadores[vezjogador].extend(compracartas(1))

  vezjogador += direcao
  if vezjogador >= numerojogadores:
          vezjogador = 0
  elif vezjogador < 0:
            vezjogador = numerojogadores-1

print('fim de jogo')
print(f'{vencedor} Venceu esta rodada! Parabens')
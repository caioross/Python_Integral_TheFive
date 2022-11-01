
**MEGAUNO**
"""

import random
import time

def montarBaralho():
    baralho = []
    cores = ['vermelho' , 'verde' , 'amarelo' , 'azul']
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '+2' , 'pular' , 'reverso']
    coringas = ['escolher' , '+4']
    for cor in cores:
      for numero in numeros:
        carta = '{} {}' .format(cor , numero)
        #carta = f'{cor} {numero}'
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
def mostrarMao(jogador, maoJogador):
  print('Vez de {} jogar'.format(jogadorNome[jogador]))
  #time.sleep(10)
  print('suas cartas:')
  print('------------------')
  y = 1
  for carta in maoJogador:
    print('{}) {}'.format(y, carta))
    y += 1
    #y = y+1
def jogada(cor, numero, maoJogador):
    for carta in maoJogador:
      if 'coringas' in carta:
        return True
      elif cor in carta or valor in carta:
        return True
    return False
baralhoMonte = montarBaralho()
baralhoMonte = embaralharBaralho(baralhoMonte)
baralhoMonte = embaralharBaralho(baralhoMonte)
baralhoMonte = embaralharBaralho(baralhoMonte)
descartadas = []
jogadorNome = []
jogadores = []
cores = ['vermelho' , 'verde' , 'amarelo' , 'azul']
numeroJogadores = int(input('Quantos jogadores vão jogar?'))
while numeroJogadores < 2 or numeroJogadores > 4:
      numeroJogadores=int(input('Invalido, escolha um valor entre 2-4 jogadores.\nQuantos jogaores?'))
for jogador in range(numeroJogadores):
    jogadorNome.append(input('Qual onome do {} jogador?'.format(jogador+1)))
    jogadores.append(virarCartas(5))
vezJogador = 0 
direcao = 1
jogando = True 
descartadas.append(baralhoMonte.pop(0))
separarCarta = descartadas[0].split(' ', 1) 
corAtual = separarCarta[0]
if corAtual != 'coringas':
   valor = separarCarta[1]
else:
    valor = 'qualquer'
while jogando:
      mostrarMao(vezJogador, jogadores[vezJogador])
      print('Carta no topo da pilha: '.format(descartadas[-1]))
      if jogada(corAtual, valorCarta, jogador[vezJogador]):
         cartaEscolhida = int(input('Qual carta voce quer jogar?'))
         while not jogada (corAtual, valorCarta, [jogadores[vezJogador][cartaEscolhida-1]]):
           cartaEscolhida = int(input('Não é uma carta válida? Escolha outra carta'))
         print('Você escolheu {}'.format(jogadores[vezJogador][cartaEscolhida-1]))
         descartadas.append(jogadores[vezJogador].pop(cartaEscolhida-1))
         if len (jogadores[vezJogador]) == 0:
            jogando = Falsevencedor = jogadorNome[vezJogador]
         else:
            separarCarta + descartadas [-1].split('',1)
            corAtual = separarCarta[0]
            if len (separarCarta) == 1:
               valorCarta = 'Qualquer'
            else:
              valorCarta = separarCarta[1]
            if corAtual == 'Coringas':
              for x in range(len(cores)):
                print('{} {}'.format(x+1, cores[x]))
              novaCor =int(input('Qual você quer escolher?'))
              while novaCor < 1 or novaCor > 4:
                novaCor = int(input('Errado qual cor vovê quer escolher? '))
              corAtual = cores[novaCor-1]
            if valorCarta == 'Inverter':
              direcao = direcao * -1
            elif valorCarta == 'Pular':
              vezJogador += direcao
              if vezJogador >= numeroJogadores:
                vezJogador = 0
              elif vezJogador < 0:
                vezJogador = numeroJogadores-1
      else:
        print('Você nao pode ogar. Você deve comprar uma carta')
        jogadores[vezJogador].extend(virarCartas(1))

      vezJogador += direcao
      if vezJogador >= numeroJogadores:
         vezJogador = 0
      elif vezJogador < 0:
         vezJogador = numeroJogadores-1  
print('Fim de jogo')
print('{} é o vencedor! Parabéns')

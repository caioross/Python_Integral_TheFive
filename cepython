import requests

def main():
  print('CEPython')

  cep = input('Digite o CEP para a consulta: ')

  while len(cep) !=  8:
    print('Quantidade de dígito inválida!')
    cep = input('Digite o CEPpara a consulta')

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    endereco = request.json()

  if 'erro' not in endereco:
    print('==> CEP ENCONTRADO <==')
    print('CEP: {}'.format(endereco['cep']))
    print('Cidade: {}'.format(endereco['localidade']))
    print('Estado: {}'.format(endereco['uf']))

  else:
    print('{}: CEP inválido'.format(cep))

  opcao = int(input('Deseja realizar outra consulta?/n Sim/n Sair/n'))
  if opcao == 1:
    main()
  else:
    print('Até mais!!!')

if __name__ == '__main__':
  main()

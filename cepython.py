import requests

def main():
	print('CEPython')

	cep = input('Digite o CEP para a consulta: ')
	
	while len(cep) != 8:
		print('Quantidade de dígitos inválida!')
		cep = input('Digite o CEP para a consulta: ')

	request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
	endereco = request.json()

	if 'erro' not in endereco:
		print('==> CEP ENCONTRADO <==')
		print('CEP: {}'.format(endereco['cep']))
		print('Cidade: {}'.format(endereco['localidade']))
		print(f"Estado: {endereco['uf']}")
		
	else:
		print('{}: CEP inválido.'.format(cep))

	print('---------------------------------')
 
	def validacao():
		opcao = input('Deseja realizar outra consulta ? \n 1. Sim \n 2. Sair \n ')
		if opcao == "1" or opcao == "2":
			if int(opcao) == 1:
				main()
			else:
				print('Até mais!!!')
		else:
			validacao()
	validacao()

if __name__ == '__main__':
	main()
	#	if opcao.upper() == "SIM" or opcao.upper == "NAO" or opcao.upper() == "NÂO":

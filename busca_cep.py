import requests

cep = input('Insira o CEP: ')
cep = cep.replace("-", "").replace(".", "")

if len(cep) == 8:
  link = f'https://viacep.com.br/ws/{cep}/json/'
  
  requisicao = requests.get(link)
  
  print(requisicao)
  
  dic_requisicao = requisicao.json()
  uf = dic_requisicao['uf']
  cidade = dic_requisicao['localidade']
  bairro = dic_requisicao['bairro']
  
  print(dic_requisicao)
else:
  print('CEP Inválido')
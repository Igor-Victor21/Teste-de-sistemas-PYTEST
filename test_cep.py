import requests

def buscar_cep (cep):
    resposta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    if resposta.status_code != 200:
        return 'Cep inválido'
    else:
        cep_encontrado = resposta.json()
        return cep_encontrado
    
cep = input("Informe o cep: ")
resultado = buscar_cep(cep)    

print(f'Região: {resultado['regiao']}' )
print(f'Cidade: {resultado['localidade']}' )
print(f'Estado: {resultado['uf']}' )
print(f'Bairro: {resultado['bairro']}' )
print(f'Rua: {resultado['logradouro']}' )



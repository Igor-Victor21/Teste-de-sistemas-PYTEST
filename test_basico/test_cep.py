import requests
import pytest

@pytest.fixture
def consulta_cep():
    resposta = requests.get(f'https://viacep.com.br/ws/81750390/json/')
    
    if resposta.status_code != 200:
        return 'Cep não encontrado'
    else:
        resposta.status_code = 200
        resposta.json()
        
        return resposta
global resposta

def test_cep_nao_encontrado(consulta_cep):
    resposta = consulta_cep
    
    assert not resposta == 'Cep não encontrado'

def test_buscar_regiao(consulta_cep):
    resposta = consulta_cep
    
    cidade = resposta.json()
    
    assert cidade ['regiao'] 


def test_buscar_cidade(consulta_cep):
    resposta = consulta_cep
    
    cidade = resposta.json()
    
    assert cidade ['localidade'] 

def test_buscar_estado(consulta_cep):
    resposta = consulta_cep
    
    cidade = resposta.json()
    
    assert cidade ['uf'] 
    
def test_buscar_bairro(consulta_cep):
    resposta = consulta_cep
    
    cidade = resposta.json()
    
    assert cidade ['bairro'] 

def test_buscar_logradouro(consulta_cep):
    resposta = consulta_cep
    
    cidade = resposta.json()
    
    assert cidade ['logradouro'] 
    
# cep = input("Informe o cep: ")
# resultado = buscar_cep(cep)    

# print(f'Região: {resultado['regiao']}' )
# print(f'Cidade: {resultado['localidade']}' )
# print(f'Estado: {resultado['uf']}' )
# print(f'Bairro: {resultado['bairro']}' )
# print(f'Rua: {resultado['logradouro']}' )



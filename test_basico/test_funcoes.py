from .funcoes import *

def test_verificar_soma_e_subtrair():
    assert somar(2,3) == 5
    assert subtrair(5,2) == 3
    
def test_verifica_se_numero_par():
         assert eh_par(5) == 'é impar'
         assert eh_par(10) == 'é par'

def test_verificar_email():
         assert verifica_email('pigor.pigor@gmail.com') == 'E-mail válido'
         assert verifica_email('pigor.pigorgmail') == 'E-mail incorreto'
        
def test_validar_senha():
     assert validar_senha('#Sssaaaaiiii') == 'senha cadastrada'
     assert validar_senha('Sssaaaaiiii') == 'senha não contem elementos obrigatorios'

def test_tamanho_string():
     assert tamanho_string('abcdef') == 6
    
def test_maior_idade():
     assert maior_idade(18) == 'Maior idade'
     assert maior_idade(11) == 'Menor Idade'

def test_validar_nota():
     assert validar_nota(80,60) == 'Passou'
     assert validar_nota(40,60) == 'Recuperação'   
     assert validar_nota(10,20) == 'Reprovado'   

    
       
     
     
    
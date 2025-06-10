def eh_par(numero):
    if numero % 2 == 0:
        return 'é par'
    else:
        return 'é impar'
    

def somar (a,b):
    return a+b


def subtrair (a,b):
    return a-b

def test_verificar_soma_e_subtrair():
    assert somar(2,3) == 5
    assert subtrair(5,2) == 3
    
def test_verifica_se_numero_par():
        assert eh_par(5) == 'é impar'
        assert eh_par(10) == 'é par'
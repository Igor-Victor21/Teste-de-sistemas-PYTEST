def verifica_email(email):
    if '@' in email and '.com' in email:
        return 'E-mail válido'
    else:
        return 'E-mail incorreto'
    
def test_verificar_email():
        assert verifica_email('igor.victorcontato@gmail.com') == 'E-mail válido'
        assert verifica_email('igor.victorcontatogmail') == 'E-mail incorreto'
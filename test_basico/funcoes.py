def verifica_email(email):
    if '@' in email and '.com' in email:
        return 'E-mail válido'
    else:
        return 'E-mail incorreto'

def validar_senha(senha):
    caractere = '@#$%&*'
    if len(senha) > 8 and \
        any(c.isdigit()for c in senha) and \
        any(c.isupper () for c in senha) and \
        any(c in caractere for c in senha):
        return 'senha cadastrada'
    else:
        return 'senha não contem elementos obrigatorios'

def tamanho_string(nome):
    tamanho= len(nome)
    return tamanho

def eh_par(numero):
    if numero % 2 == 0:
        return 'é par'
    else:
        return 'é impar'
    

def somar (a,b):
    return a+b


def subtrair (a,b):
    return a-b

def maior_idade(idade):
    if idade >= 18:
        return 'Maior idade'
    else:
        return 'Menor Idade'

def validar_nota(nota1,nota2):
    media = (nota1 + nota2)/2
    if media >= 70:
        return 'Passou'
    elif media < 70 and media >= 40:
        return 'Recuperação'
    else: 
        return 'Reprovado' 


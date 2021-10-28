from datetime import datetime

def voto(ano):
    data = datetime.now().year - ano
    if data == 18 or data > 65:
        print('Voto opcional.')
    elif data > 18 and data <65:
        print('Voto obrigatório.')
    elif data < 18: 
        print('Voto negado.')

voto(int(input('Qual a sua data de nascimento: ')))
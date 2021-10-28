from datetime import datetime
ficha = dict()


ficha['nome']=str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
ficha['idade']=datetime.now().year - nasc
ficha['carteira']=int(input('Carteira de Trabalho (0 não tem): '))
if ficha['carteira'] != 0:
    ficha['contrato']=int(input('Ano de Contratação: '))
    ficha['salario']=int(input('Salário: R$ '))
    ficha['aposentadoria'] = ficha['idade']+((ficha['contrato'] + 35) - datetime.now().year)
print('-=' *30)
for k, v in ficha.items():
    print(f' -{k} tem o valor {v}')
try:
    a = int(input('n1: '))
    b = int(input('n2: '))
    r=a/b
except (ValueError,TypeError):
    print('Tivemos um problema com o tipo de dados.')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os valores.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}')
else:
    print(r)
finally:
    print('Volte semrpre! Muito Obrigado!')
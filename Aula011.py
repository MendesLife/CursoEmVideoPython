#Cor \033[style;text;fontm]
#Cor \033[0;33;44m]

cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m',
    'pretoebranco':'\033[7;30m'
}

print('\033[1;31;43mOlá Mundo!\033[m')

print('{}Olá para todos {}menos para alguns.{}'.format(cores['azul'],cores['amarelo'],cores['limpa']))
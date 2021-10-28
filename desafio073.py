times = ('A','G','I','D','E','F','C','H','B','J')

print(f'Os 5 primeiros times são {times[0:6]}')
print(f'Os 4 ultimos times são {times[-4:]}')
print(f'Os times em ordem alfabética são {sorted(times)}')
print(f'O Chapecoense está na posição {times.index("C")+1}.')
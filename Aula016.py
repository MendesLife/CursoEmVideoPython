 #Tuplas são imutáveis
lanche = ('hambúrguer','suco', 'pizza', 'pudim')
for pos,comida in enumerate(lanche):
     if comida == 'suco':
         print(f'Eu vou beber {comida} na posição {pos}.') 
     else:
         print(f'Eu vou comer {comida} na posição {pos}.') 
print('Vou ficar gordinho.')



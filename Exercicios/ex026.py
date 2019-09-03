"""
Faça um program que leia uma frase pelo teclado e mostre:
quantas vezes aparece a letra 'A'
em que posição ela aparece a primeira vez
em que posição ela aparece a ultima vez
"""
frase = str(input('Digite uma frase: ')).lower().strip()
print('A letra A aparece {} vezes'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a') + 1))
print('A ultima letra A aparece na posição {}'.format(frase.rfind('a') + 1))

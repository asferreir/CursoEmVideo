"""
crie um programaque leia um numero real qualquer pelo teclado
e mostre na tela a sua porção inteira.
ex. digite um numero: 6.127
o numero 6.127 tem a parte inteira 6."""
# from math import floor
from math import trunc


num = float(input('Informe um numero real qualquer: '))
# print('A porção inteira de {} é igual a {}'.format(num, floor(num)))
print('A porção inteira de {} é igual a {}'.format(num, trunc(num)))

"""
# OUTRA SOLUCAO
num = float(input('Infome um numero: '))
print('A porção inteira de {} é igual a {}'.format(num, int(num)))
"""

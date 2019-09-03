# Importa todas as funcionalidades
# import math
# Importanto apenas a funcionalidade sqrt from math
from math import sqrt


num = int(input('Digite um numero: '))
# Chamado diretamenta
raiz = sqrt(num)
# Chamado indiretamenta
# raiz = math.sqrt(num)
# math.ceil aredondar para cima.
# print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
# math.floor aredondar para baixo
# print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

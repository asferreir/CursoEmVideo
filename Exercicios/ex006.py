"""
CRIE UM ALGORITMO QUE LEIA UM NUMERO E
MOSTRE SEU DOBRO, TRIPLO E RAIZ QUADRADA.
"""
n = int(input('Informe um numero: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
# raiz = pow(n, (1/2))  # OUTRA FORMA DE CALCULAR RAIZ QUADRADA
print('O dobro de {} é = {}, o trilo é = {} e sua raiz quadrada é {}'.format(
        n, dobro, triplo, raiz))

"""
OUTRA RESOLUCAO
n = int(input('Informe um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobre de {} é {}'.format(n, d))
print('O triplo de {} é {}'.format(n, t))
print('A raiz quadrada de {} é {:2f}'.format(n, r))
"""

"""
OUTRA RESOLUCAO
n = int(input('Informe um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobre de {} é {}'.format(n, (n*2)))
print('O triplo de {} é {}'.format(n,(n*3)))
print('A raiz quadrada de {} é {:2f}'.format(n, (n**(1/2))))
print('A raiz quadrada de {} é {:2f}'.format(n, pow(n, (1/2))))) #POW
"""

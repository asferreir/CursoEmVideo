"""
FAÇA UM PROGRAMA QUE LEIA NUMERO INTEIRO QUALQUER
E MOSTRE NA TELA SUA TABUADA.
"""
n = int(input('Informe um numero inteiro: '))
for item in range(1, 11, 1):
    print('{} * {} = {}'.format(n, n, item, (n * item)))

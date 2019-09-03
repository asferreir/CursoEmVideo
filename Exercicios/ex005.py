"""
FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E
MOSTRE NA TELA SEU SUCESSOR E SEU ANTECESSOR.
"""
n = int(input('Informe um numero inteiro: '))
s = n + 1
a = n - 1
print('O antecessor de {} é = {} e seu sucesso é = {}'.format(
        n, a, s))

"""
OUTRA RESOLUCAO
n = int(input('Informe um numero inteiro: '))
print('O antecessor de {} é = {} e seu sucesso é = {}'.format(
        n, (n-1), (n+1)))
"""

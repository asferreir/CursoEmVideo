"""
CRIE UM PROGRAMA QUE LEIA QUANDO DINHEIRO UMA PESSOA TEM
NA CARTEIRA E MOSTRE QUANTOS DOLARES ELA PODE COMPRAR.

CONSIDERAR US$ 1,00 = R$ 3,27

1.00        = 3,27
convertido  = carteira

convertido = (carteira x 1 ) / 3,27

"""
carteira = float(input('Dinheiro: R$ '))
convertido = (carteira * 1.00) / 3.27
print('com R$ {} voce compraria US$ {:.2f}.'.format(carteira, convertido))


"""
OUTRA RESOLUCAO
carteira = float(input('Dinheiro: R$ '))
convertido = carteira / 3.27
print('com R$ {:.2f} voce compraria US$ {:.2f}.'.format(carteira, convertido))
"""

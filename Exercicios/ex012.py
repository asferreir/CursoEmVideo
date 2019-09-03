"""
FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUDO
E MOSTRE SEU NOVO PREÇO COM 5% DE DESCONTO.
"""
produto = float(input('Preço: '))
desconto = produto * (5/100)
print('O valor do produto com desconto é = {:.2f}'.format(produto - desconto))

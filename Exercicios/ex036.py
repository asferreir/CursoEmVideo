"""
Escreva um programa para aprovar o emprestimo bancario para
compra de uma casa.O programa vai perguntar o valor da casa,
o salario do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal sabendo que ela nao pode
exceer 30% do salario ou então o emprestimo sera negado.
"""
imóvel = float(input('Informe o valor do imóvel que será financiado: R$ '))
renda = float(input('Informe a renda bruta: R$ '))
parcela = int(input('Informe em quantas parcelas deseja financiar: '))
if imóvel / parcela > renda * 0.30:
    print('Imprestimo será negado!')
else:
    print('Emprestimo será aprovado!')

# casa = float(input('Valor da Casa: R$ '))
# salario = float(input('Salario do Comprador: R$ '))
# anos = int(input('Quantos anos de financiamento: '))
# prestação = casa / (anos * 12)
# minimo = salario * 30 / 100
# print('Para pagar uma casa de R${:.2f} em {} anos'.format(
#     casa, anos), end='')
# print(' a prestação será de R${}'.format(prestação))
# if prestação <= minimo:
#     print('Emprestimo pode ser CONCEDIDO')
# else:
#     print('Emprestimo NEGADO!!')

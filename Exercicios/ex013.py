"""
FAÇA UM ALGORITMO QUE LEIA O SALARIO DE UM
FUNCIONARIO E MOSTRE SEU NOVO SALARIO. COM
15% DE AUMENTO.
"""
salario = float(input('Salario: '))
promoção = salario * 15/100
print('Salario apos promoção: R$ {:.2f}'.format(salario + promoção))

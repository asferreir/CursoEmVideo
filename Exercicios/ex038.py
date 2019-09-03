"""
Escreva um programa que leia dois numeros inteiros
e compare-os mostrando na tela uma mensagem:
O primeiro valor é maior
O segundo valor é maior
Nao existe valor maior, os dois sao iguais
"""
n1 = int(input('Informe o primeiro numero: '))
n2 = int(input('Informe o segundo numero: '))
if n1 == n2:
    print('Os numeros informados são iguais!!')
elif n1 > n2:
    print('O primeiro numero é maior')
else:
    print('O segundo numero é maior')

"""
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
"""
seg01 = float(input('Informe o primeiro segmento: '))
seg02 = float(input('Informe o segundo segmento: '))
seg03 = float(input('Informe o terceiro segmento: '))
if seg01 < seg02 + seg03 and seg02 < seg01 + seg03 and seg03 < seg01 + seg02:
    print('Os segmentos informados podem formar um triangulo!')
else:
    print('Os segmentos informados não podem formar um triangulo')

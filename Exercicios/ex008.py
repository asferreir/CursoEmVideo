"""
ESCREVA UM PROGRAMA QUE LEIA UM VALOR
EM METROS E EXIBA CONVERTIDO EM CENTIMETROS
E MILIMETROS
"""

valorIni = float(input('Informe o valor em metros: '))
cm = valorIni * 100
mm = valorIni * 1000
print('{} metros é igual a {} centimetros e {} milimetros'.format(
    valorIni, cm, mm))

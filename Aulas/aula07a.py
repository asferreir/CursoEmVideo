"""
ORDEM DE PRECEDENCIA
1 - ()
2 - **
3 - *, /, //, %
4 - +, -

5 + 2 * 2 = 11
3 * 5 + 4 ** 2 = 31
3 * (5  + 4) ** 2 = 243
"""
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}!'.format(s, m, d))
print('Divisão inteira {} e Potência {}'.format(di, e))

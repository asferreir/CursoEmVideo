"""
Escreva um programa que leia um numero inteiro qq
e peça para o usuário escolher qual sera a base de
conversão.
1 para binario
2 para octal
3 para hexadecimal
"""
num = int(input('Digite um numero inteiro: '))
print('''Escolha um das bases para conversão:
[1] Converter para BINARIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opção = int(input('Sua Opção: '))
if opção == 1:
    print('{} convertido para BINARIO é igual {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('`{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção Invalida!')

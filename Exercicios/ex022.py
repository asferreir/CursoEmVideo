"""
Crie um programa que leia o nome e completo de uma pessoa e mostre:
O Nome com todas as letras maisculas
o nome com todas as letras minusculas
quantas letras ao todo(sem considerar espaços)
quantas letras tem o primeiro nome
"""
# nome = input(str('Informe seu nome: '))
# print(nome.upper())
# print(nome.lower())
# print(len(''.join(nome.split())))
# print(len(nome.split(' ')[0]))
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu primeiro nome tem ao todo {} letras'.format(
    len(nome) - nome.count(' ')))
print('Seu primeiro nome tem ao todo {} letras'.format(
    len(''.join(nome.split()))))
# print('Seu primeiro nome tem {} letras'.format(len(nome.split(' ')[0])))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(
    separa[0], len(separa[0])))

"""
Faça um program que leia um nome completo de uma pessoa
mostrando em seguida o primeiro e o ultimo nome separadamente.
Ex:Ana Maria de Souza
Primeiro:Ana
Ultimo:Souza
"""
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Analisando seu nome...')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome) - 1]))

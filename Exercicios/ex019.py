"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela
o nome do escolhido.
"""
from random import choice
nomeA = str(input('Informe o nome do aluno: '))
nomeB = str(input('Informe o nome do aluno: '))
nomeC = str(input('Informe o nome do aluno: '))
nomeD = str(input('Informe o nome do aluno: '))
lista = [nomeA, nomeB, nomeC, nomeD]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

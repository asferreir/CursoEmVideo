"""
O mesmo professor do desafio 019 quer sortear a ordem de
apresentação de trabalhos dos alunos. Faça um programa
que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
import random
nomeA = str(input('Informe o nome do aluno: '))
nomeB = str(input('Informe o nome do aluno: '))
nomeC = str(input('Informe o nome do aluno: '))
nomeD = str(input('Informe o nome do aluno: '))
lista = [nomeA, nomeB, nomeC, nomeD]
random.shuffle(lista)
print(lista)

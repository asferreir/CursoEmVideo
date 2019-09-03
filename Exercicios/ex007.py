"""
DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS
NOTAS DE UM ALUNO E MOSTRE SUA MEDIA.
"""
nome = input('Nome do Aluno: ')
n1 = float(input('Informe Nota 1: '))
n2 = float(input('Informe Nota 2: '))
media = (n1 + n2) / 2
print('A media do Aluno {}, é = {}.'.format(
        nome, media))

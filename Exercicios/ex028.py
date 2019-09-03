"""
Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint
from time import sleep
# aleatorio = random.randint(0, 5)
# num = int(input('Digite um numero: '))
# if num == aleatorio:
#     print('Acertou miseravi!!')
# else:
#     print('Errou feio, errou rude!!')
computer = randint(0, 5)
print('-=-' * 20)
print('Vou pensar num número entre 0 e 5.. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computer:
    print('Parabens, você ganhou!!')
else:
    print('Voce perdeu, Eu pensei no numero {} e não no {}'.format(
        computer, jogador))

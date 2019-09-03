"""
Faça um programa que leia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tangente desse ângulo.
"""
from math import radians, sin, cos, tan
angulo = float(input('Digite um angulo que voce deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))

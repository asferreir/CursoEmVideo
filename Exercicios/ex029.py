"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
"""
speed = float(input('Informe a velocidade: '))
if speed > 80:
    multa = (speed - 80) * 7.00
    print('Voce foi multado em R$ {:.2f}'.format(multa))
else:
    print('Dentro da velocidade permitida!')

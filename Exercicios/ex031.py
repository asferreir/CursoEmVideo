"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de
até 200Km e R$0,45 parta viagens mais longas.
"""
distancia = float(input('Informe a distancia da Viagem: '))
#preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
if distancia <= 200:
    preco = distancia * 0.50
    print('Percorrendo a distancia {}KM voce pagara R$ {}'.format(
        distancia, preco))
else:
    preco = distancia * 0.45
    print('Percorrendo a distancia {}KM voce pagara R$ {}'.format(
        distancia, preco))

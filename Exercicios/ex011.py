"""
FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE
EM METROS, CALCULE SUA AREA E QUANTIDADE DE TINTA NECESSARIA
PARA PINTA-LA, SABENDO QUE CADA LITRO DE TINTA PINTA UMA AREA
DE 2M²
"""
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2
print('Area é {:.2f} m². Para pintar voce ira precisa de {:.2f} litros'.format(
        area, tinta))

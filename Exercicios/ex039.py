"""
Faca um programa que leia o ano de nascimento
de um jovem e informe de acordo com sua idade:
se ele ainda vai se alistar no servico militar
se é a hora de se alistar
se ja passou o tempo do alistamento

OBS: o programa tambem devera mostrar o tempo
que falta ou que passou o prazo
"""
from datetime import date

anonasc = int(input('Informe o ano de nascimento: '))
anoatual = date.today().year
if anoatual - anonasc == 18:
    print('Você deve procurar o serviço de alistamento!')
elif anoatual - anonasc < 18:
    print('Ainda não esta no momento de se alistar!')
else:
    print('Você ja passou pelo alistamento.')
